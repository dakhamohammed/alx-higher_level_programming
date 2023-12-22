#!/usr/bin/python3
"""class definition of a State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

_metadata = MetaData()
Base = declarative_base(metadata=_metadata)


class State(Base):
    """class State."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
