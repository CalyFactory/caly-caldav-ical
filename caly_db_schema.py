import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Refer site : http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/

Base = declarative_base()

class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class Address(Base):
	__tablename__ = 'address'
	id = Column(Integer, primary_key=True)
	treet_name = Column(String(250))
	street_number = Column(String(250))
	post_code = Column(String(250), nullable=False)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship(Person)

# If echo=True, You can see a log about tutorial.db
engine = create_engine('sqlite:///tutorial.db', echo=False)
Base.metadata.create_all(engine)
