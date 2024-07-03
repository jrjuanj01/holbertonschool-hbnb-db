"""
City related functionality
"""
import os
from src.models.base import Base
from src.models.country import Country
from sqlalchemy import Column, String, DateTime, ForeignKey, func

if os.getenv("REPOSITORY_ENV_VAR") == "db":
    from src.persistence.db import DBRepository
    repo = DBRepository
else:
    repo = Base
    
class City(Base):
    """City representation"""

    name: str
    country_code: str

    __tablename__ = "Cities"
    
    id = Column(String(36), primary_key=True)
    name = Column(String(256), nullable=False)
    country_code = Column(String(2), ForeignKey("country.code"), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())
    
    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)

        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        from src.persistence import repo

        country = Country.get(data["country_code"])

        if not country:
            raise ValueError("Country not found")

        city = City(**data)

        repo.save(city)

        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """Update an existing city"""
        from src.persistence import repo

        city = City.get(city_id)

        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        repo.update(city)

        return city
