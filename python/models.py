# This file contains the model of our application
# We will be using SQLite with SQLALCHEMy for our database operations

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()       # This is the base class for all our models

# The SQLIite engine
engine = create_engine('sqlite:///app.db', echo=True)

# Patient model
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String)
    phone_number = Column(String)



class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key =True)
    name = Column(String)
    age = Column(Integer)
    specialty = Column(String)
    phone_number = Column(String)
    email = Column(String)



class Nurse(Base):
    __tablename__ = 'nurses'
    id = Column(Integer, primary_key =True)
    name = Column(String)
    age = Column(Integer)
    specialty = Column(String)
    phone_number = Column(String)
    email = Column(String)

class Department(Base):






class Appointment(Base):
