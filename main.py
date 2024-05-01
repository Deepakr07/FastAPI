
# importing fast api
from fastapi import FastAPI

#creating an instance of fastapi
app = FastAPI()

@app.get("/")
async def root():
    return{"message":"hello world"}