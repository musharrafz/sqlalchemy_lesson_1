from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

Base = declarative_base()


db_url = os.getenv("DB_URL")
engine = create_engine(db_url)

Session = sessionmaker(engine)
session = Session()