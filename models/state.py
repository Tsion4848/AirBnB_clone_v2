#!/usr/bin/python3
"""implementation of class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                              cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """
            get list of City instances with state_id
            equals to the current State.id
            """
            list_cities = []
            for city_obj in list(models.storage.all(City).values()):
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return city_list
