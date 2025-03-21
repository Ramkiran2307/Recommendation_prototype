from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./soulverse1.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Mood-Based Resource Table
class MoodResource(Base):
    __tablename__ = "mood_resources"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    mood = Column(String, nullable=False)
    type = Column(String, nullable=False)  # "youtube", "article", or "podcast"
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)

# Mood-Based Activities Table
class MoodActivity(Base):
    __tablename__ = "mood_activities"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    mood = Column(String, nullable=False)
    activity = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
