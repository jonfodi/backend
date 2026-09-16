from sqlalchemy import Column, Integer, String, Enum
from database import Base
from enum import Enum as PyEnum


class SpecialtyEnum(str, PyEnum):
    eating_disorder = "eating_disorder"
    athlete = "athlete"
    weight_loss = "weight_loss"


class Dietitian(Base):
    __tablename__ = "dietitian"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(Enum(SpecialtyEnum)) 

