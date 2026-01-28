# logic.py

from data import doctors, tokens, MAX_CAPACITY, PRIORITY_ORDER
from fastapi import Header, HTTPException
from data import HOSPITAL_ADMIN_KEY

def verify_hospital_admin(x_admin_key: str = Header(...)):
    if x_admin_key != HOSPITAL_ADMIN_KEY:
        raise HTTPException(
            status_code=403,
            detail="Only hospital admin can perform this action"
        )

def get_confirmed_count(doctor_id: str, slot: str) -> int:
    """
    Returns number of CONFIRMED tokens for a doctor in a slot
    """
    return sum(
        1 for t in tokens
        if t["doctor_id"] == doctor_id
        and t["slot"] == slot
        and t["status"] == "CONFIRMED"
    )


def select_doctor(department_id: str, slot: str):
    """
    Selects the least-loaded available doctor
    from a department for a given slot.
    """
    eligible = []

    for doctor in doctors:
        if (
            doctor["department_id"] == department_id
            and slot in doctor["available_slots"]
        ):
            load = get_confirmed_count(doctor["doctor_id"], slot)
            if load < MAX_CAPACITY:
                eligible.append((doctor["doctor_id"], load))

    if not eligible:
        return None

    # Least loaded doctor first
    eligible.sort(key=lambda x: x[1])
    return eligible[0][0]


def find_lowest_priority_token(doctor_id: str, slot: str):
    """
    Finds the lowest priority CONFIRMED token
    for emergency displacement.
    """
    confirmed_tokens = [
        t for t in tokens
        if t["doctor_id"] == doctor_id
        and t["slot"] == slot
        and t["status"] == "CONFIRMED"
    ]

    if not confirmed_tokens:
        return None

    confirmed_tokens.sort(
        key=lambda t: PRIORITY_ORDER[t["source"]],
        reverse=True
    )

    return confirmed_tokens[0]
