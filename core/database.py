import os
from dotenv import load_dotenv 
from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
if ENVIRONMENT == "development":
    DATABASE_URL = os.getenv("DEV_DATABASE_URL")
else: 
    DATABASE_URL = os.getenv("PROD_DATABASE_URL")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
