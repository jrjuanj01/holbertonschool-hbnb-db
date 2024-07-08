"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from datetime import datetime
from typing import Optional
import uuid
from src.persistence.repository import Repository
from flask import current_app as app
from sqlalchemy.orm import Session


class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(
        self,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        
        """Sets configuration for the app"""    
        
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    continue
                setattr(self, key, value)

        self.id = str(id or uuid.uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        
    def get_all(self, model):
        """Gets all values of a given model"""
        session: Session = app.db
        return session.query(model).all()

    def get(self, model, obj_id: str) -> Base | None:
        """Retrieves the data of a given model with its ID"""
        session: Session = app.db
        return session.query(model).filter_by(id=obj_id).first()

    def save(self, obj: Base) -> None:
        """Saves an instance of a given model"""
        session: Session = app.db
        session.add(obj)
        session.commit()

    def update(self, obj: Base) -> Base | None:
        """Updates the data of a given model instance"""
        session: Session = app.db
        session.add(obj)
        session.commit()
        return obj

    def delete(self, obj: Base) -> bool:
        """Deletes the data of a given model instance"""
        session: Session = app.db
        session.delete(obj)
        session.commit()
        return True

    
    def reload(self) -> None:
        """Not implemented"""
        pass
