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
from sqlalchemy import text
from flask import current_app as app


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
        
        # self.useData = app.config['SQLALCHEMY_DATABASE_URI']

    def get_all(self, model_name: str) -> list:
        """Gets all values of a given model"""
        # if self.useData:
        return app.db.query(text(model_name)).all()
        # else:
            # return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Retrieves the data of a given model with it's ID"""
        if self.useData:
            return app.db.session.query(model_name).filter_by(id=obj_id).first()
        else:
            return None


    def save(self, obj: Base) -> None:
        """Saves an instance of a given model """
        if self.useData:
            app.db.session.add(obj)
            app.db.session.commit()
        else:
            pass
    def reload(self) -> None:
        """Not implemented"""
        pass
    
    def update(self, obj: Base) -> Base | None:
        """Updates the data of a given model instance"""
        if self.useData:
            app.db.session.add(obj)
            app.db.session.commit()
            return obj
        else:
            return None
        
    def delete(self, obj: Base) -> bool:
        """Deletes the data of a given model instance"""
        if self.useData:
            app.db.session.delete(obj)
            app.db.session.commit()
            return True
        else:
            return False
