"""
Review related functionality
"""
import uuid, os
from src.models.base import Base
from src.models.place import Place
from src.models.user import User
from sqlalchemy import Column, String, DateTime, Float, ForeignKey, func

if os.getenv("REPOSITORY_ENV_VAR") == "db":
    from src.persistence.db import DBRepository
    repo = DBRepository
else:
    repo = Base

class Review(Base):
    """Review representation"""

    place_id: str
    user_id: str
    comment: str
    rating: float
    
    __tablename__ = "Reviews"
    
    id = Column(String(36), primary_key=True)
    place_id = Column(String(36), ForeignKey("place.id"), nullable=False)
    user_id = Column(String(36), ForeignKey("user.id"), nullable=False)
    comment = Column(String(420), nullable=False)
    ratng = Column(Float(), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())

    def __init__(
        self, place_id: str, user_id: str, comment: str, rating: float, **kw
    ) -> None:
        """Dummy init"""
        super().__init__(**kw)

        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Review":
        """Create a new review"""
        from src.persistence import repo

        user: User | None = User.get(data["user_id"])

        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")

        place: Place | None = Place.get(data["place_id"])

        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")

        if data.user_id == place.host_id:
            raise ValueError("Cannot review own place")
        
        new_review = Review(**data)

        repo.save(new_review)

        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> "Review | None":
        """Update an existing review"""
        from src.persistence import repo

        review = Review.get(review_id)

        if not review:
            raise ValueError("Review not found")
    
        if data.user_id != review.user_id:       #Checks if og poster is the new poster
            raise ValueError("Review cannot be edited by a different poster")

        for key, value in data.items():
            setattr(review, key, value)

        repo.update(review)

        return review
