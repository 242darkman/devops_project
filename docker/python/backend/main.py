from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, MetaData, Table, select, update
from sqlalchemy.orm import sessionmaker, Session
import uvicorn

app = FastAPI()

DATABASE_URL = "mysql://user:password@localhost/iterator-db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
iterator = Table('iterator', metadata, autoload_with=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    """
    This function is the root endpoint for the API.
    
    Parameters:
        None
    
    Returns:
        dict: A dictionary containing the message "Hello World"
    """
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    An asynchronous function that takes a string parameter `name` and returns a dictionary with a single key-value pair. 

    Parameters:
        name (str): The name to be included in the returned message.

    Returns:
        dict: A dictionary with the key "message" and the value "Hello {name}", where {name} is the input parameter.
    """
    return {"message": f"Hello {name}"}

@app.get("/health")
async def get_health():
    """
    A function that handles the GET request for the "/health" endpoint.

    Returns:
        A dictionary with the status of the API.
    """
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)