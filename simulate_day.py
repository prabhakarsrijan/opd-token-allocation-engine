# routes.py

from fastapi import APIRouter
import uuid

from models import TokenRequest
from data import tokens, PRIORITY_ORDER
from logic import (
    select_doctor,
    get_confirmed_count,
    find_lowest_priority_token
)

router = APIRouter()


@router.post("/tokens")
def create_token(request: TokenRequest):
    doctor_id = select_doctor(request.department_id, request.slot)

    status = "CONFIRMED" if doctor_id else "WAITLISTED"

    token = {
        "token_id": str(uuid.uuid4()),
        "patient_id": request.patient_id,
        "department_id": request.department_id,
        "doctor_id": doctor_id,
        "slot": request.slot,
        "source": request.source,
        "status": status
    }

    # Emergency handling
    if request.source == "EMERGENCY" and doctor_id:
        if get_confirmed_count(doctor_id, request.slot) >= 5:
            victim = find_lowest_priority_token(doctor_id, request.slot)
            if victim:
                victim["status"] = "WAITLISTED"
        token["status"] = "CONFIRMED"

    tokens.append(token)
    return token


@router.post("/tokens/{token_id}/cancel")
def cancel_token(token_id: str):
    for t in tokens:
        if t["token_id"] == token_id and t["status"] == "CONFIRMED":
            t["status"] = "CANCELLED"

            # Promote highest priority waitlisted token
            waitlisted = [
                w for w in tokens
                if w["doctor_id"] == t["doctor_id"]
                and w["slot"] == t["slot"]
                and w["status"] == "WAITLISTED"
            ]

            if waitlisted:
                waitlisted.sort(key=lambda w: PRIORITY_ORDER[w["source"]])
                waitlisted[0]["status"] = "CONFIRMED"

            return {"message": "Token cancelled and reallocated"}

    return {"message": "Token not found or already inactive"}


@router.get("/tokens")
def list_tokens():
    return tokens
