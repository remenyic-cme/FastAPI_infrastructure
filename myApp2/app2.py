from fastapi import FastAPI

app = FastAPI()

@app.get("/response")
async def my_api_name():
    return {"message": "This is second app response"}