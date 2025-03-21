from fastapi import FastAPI
from models1 import MoodInput
from recommendation1 import get_recommendations
import uvicorn

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hey There!! Welcome to Nirvaha"}

@app.post("/recommend")
def recommend_resources(input_data: MoodInput):
    return {"recommendations": get_recommendations(input_data.mood.lower())}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
