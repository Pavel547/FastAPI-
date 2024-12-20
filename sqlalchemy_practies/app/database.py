import os 
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DateBase_URL = os.getenv("DB_URL")

engine = create_engine(DateBase_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
