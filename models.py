# models.py

from pydantic import BaseModel

from pydantic import BaseModel
from typing import List

class TokenRequest(BaseModel):
    patient_id: str
    department_id: str
    slot: str
    source: str

class DoctorCreate(BaseModel):
    doctor_id: str
    department_id: str
    available_slots: List[str]

class TokenRequest(BaseModel):
    patient_id: str
    department_id: str
    slot: str
    source: str
