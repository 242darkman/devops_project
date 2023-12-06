from fastapi import FastAPI
import uvicorn

app = FastAPI()


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
    return {"message": f"Hello {name}"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)