from pydantic import BaseModel
from models import SpecialtyEnum


class DietitianResponse(BaseModel):
    id: int
    name: str
    specialty: SpecialtyEnum

    class Config:
        from_attributes = True
