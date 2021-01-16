from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://postgres:user@localhost:5432/speed"
db = create_engine(db_string)
base = declarative_base()

def copy_fields(source, desitnation, fields):
    for field in fields:
        if hasattr(source, field):
            setattr(desitnation, field, getattr(source, field))