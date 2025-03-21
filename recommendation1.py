from database1 import SessionLocal, MoodResource, MoodActivity
from fastapi import HTTPException
import pandas as pd

# Load Data from DB
db = SessionLocal()
resources = db.query(MoodResource).all()
activities = db.query(MoodActivity).all()
db.close()

# Convert to DataFrame
resources_df = pd.DataFrame([r.__dict__ for r in resources])
activities_df = pd.DataFrame([a.__dict__ for a in activities])

def get_recommendations(mood):
    if mood not in resources_df["mood"].unique():
        raise HTTPException(status_code=404, detail="Invalid mood. Please enter a valid mood category.")

    recommendations = {
        "youtube_videos": resources_df[(resources_df["mood"] == mood) & (resources_df["type"] == "youtube")][["title", "url"]].to_dict(orient="records"),
        "articles": resources_df[(resources_df["mood"] == mood) & (resources_df["type"] == "article")][["title", "url"]].to_dict(orient="records"),
        "podcasts": resources_df[(resources_df["mood"] == mood) & (resources_df["type"] == "podcast")][["title", "url"]].to_dict(orient="records"),
        "activities": activities_df[activities_df["mood"] == mood]["activity"].tolist()
    }
    return recommendations
