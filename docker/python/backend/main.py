import uvicorn
import configparser
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, MetaData, Table, select, update
from sqlalchemy.orm import sessionmaker, Session

config = configparser.ConfigParser()
config.read('properties/config.properties')

app = FastAPI()

DATABASE_URL = f"mysql://{config['DEFAULT']['DB_USER']}:{config['DEFAULT']['DB_PASSWORD']}@localhost/{config['DEFAULT']['DB_NAME']}"

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

@app.get("/get")
async def get_iterator(db: Session = Depends(get_db)):
    """
    Retrieves an iterator from the database.

    Parameters:
        db (Session): The database session object obtained from the dependency injection.

    Returns:
        dict: A dictionary containing the status of the operation and the retrieved iterator value. If no iterator is found, the value will be "No value".
    """
    result = db.execute(select(iterator)).first()
    return {"status": "OK", "iterator": result[0] if result else "No value"}

@app.post("/add", status_code=201)
async def add_iterator(value: int, db: Session = Depends(get_db)):
    """
    Updates the state of an iterator in the database with the specified value.

    Parameters:
        value (int): The value to update the iterator state with.
        db (Session, optional): The database session. Defaults to the result of the `get_db` dependency.

    Returns:
        dict: A dictionary with the status and message of the update operation.
    """
    db.execute(iterator.update().values(state=value))
    db.commit()
    return {"status": "ok", "message": "Iterator value update successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host=config['DEFAULT']['APP_HOST'], port=int(config['DEFAULT']['PORT']))