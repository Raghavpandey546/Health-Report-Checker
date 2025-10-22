from sqlalchemy import Column, Integer, String, Boolean
from .database import Base  # Import the Base from our database.py

class User(Base):
    """
    This is the User model.
    It tells SQLAlchemy what the "users" table should look like.
    """
    __tablename__ = "users"

    # Define the columns for the "users" table
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # We can add more fields here later, like "full_name", etc.