from sqlalchemy import Column, Integer, String
from database import Base


class Dietitian(Base):
    __tablename__ = "dietitian"

    id = Column(Integer, primary_key=True)
    name = Column(String)

