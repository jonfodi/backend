from pydantic import BaseModel
from enum import Enum


class SpecialtyEnum(str, Enum):
    eating_disorder = "eating_disorder"
    athlete = "athlete"
    weight_loss = "weight_loss"


class DietitianResponse(BaseModel):
    id: int
    name: str
    specialty: SpecialtyEnum

    class Config:
        from_attributes = True
