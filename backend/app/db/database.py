from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. Create the SQLAlchemy "engine"
# This is the main connection point to our database.
# The "check_same_thread" is only needed for SQLite.
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 2. Create a "SessionLocal" class
# Each instance of SessionLocal will be a single database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create a "Base" class
# This is what our database model classes (like the User model)
# will "inherit" from.
Base = declarative_base()