from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://postgres:user@localhost:5432/speed"
db = create_engine(db_string)
base = declarative_base()
