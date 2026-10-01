import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
SessionLOocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()





