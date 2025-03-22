import os
import uvicorn

# Run database and seed scripts before starting FastAPI
os.system("python database1.py")
os.system("python seed1.py")

from fastapi import FastAPI
from models1 import MoodInput
from recommendation1 import get_recommendations

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hey There!! Welcome to Nirvaha"}

@app.post("/recommend")
def recommend_resources(input_data: MoodInput):
    return {"recommendations": get_recommendations(input_data.mood.lower())}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Use Render's assigned port
    uvicorn.run(app, host="0.0.0.0", port=port)
