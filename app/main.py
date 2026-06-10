from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Memory Engine Running!"}