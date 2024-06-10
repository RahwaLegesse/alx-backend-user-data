#!/usr/bin/env python3
"""Module for Users.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """A class

    Attributes:
        __tablename__ (str): The name of the table.
        id (int): id
        email (str): The email .
        hashed_password (str): The hashed password
        session_id (str): The session ID of the user,
        reset_token (str): The reset token
        resets.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
