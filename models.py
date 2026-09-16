from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum


class SpecialtyEnum(enum.Enum):
    eating_disorder = "eating_disorder"
    athlete = "athlete"
    weight_loss = "weight_loss"


class Dietitian(Base):
    __tablename__ = "dietitian"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(Enum(SpecialtyEnum)) 

