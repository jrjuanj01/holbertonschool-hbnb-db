"""
User related functionality
"""

import os
from src.models.base import Base
from sqlalchemy import Column, String, Boolean, DateTime, func
from flask_bcrypt import Bcrypt as bcrypt

if os.getenv("REPOSITORY_ENV_VAR") == "db":
    from src.persistence.db import DBRepository
    repo = DBRepository()
else:
    repo = Base

class User(Base):
    """User representation"""

    __tablename__ = "User"  # Ensure this matches your actual table name
    
    id = Column(String(36), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    password_hash = Column(String(128), nullable=False)  # Ensure secure storage
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())

    def __init__(self, email: str, first_name: str, last_name: str, **kw):
        """Initialize the user"""
        super().__init__(**kw)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """Representation of the user"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password: str):
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def create(user_data: dict) -> "User":
        """Create a new user"""
        # users: list["User"] = repo.get_all(User)

        # for u in users:
        #     if u.email == user_data["email"]:
        #         raise ValueError("User already exists")

        new_user = User(
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password_hash=bcrypt().generate_password_hash(user_data["password"]).decode('utf-8')
        )

        repo.save(new_user)

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        """Update an existing user"""
        user: User | None = repo.get(User, user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password_hash = bcrypt.generate_password_hash(data["password"]).decode('utf-8')

        repo.update(user)

        return user
