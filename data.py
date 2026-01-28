# data.py

# Maximum patients allowed per doctor per slot
MAX_CAPACITY = 5

HOSPITAL_ADMIN_KEY = "HOSPITAL_SECRET_123"

# Doctors are the source of truth
doctors = [
    {
        "doctor_id": "DOC_1",
        "department_id": "GENERAL_OPD",
        "available_slots": ["09:00-10:00", "10:00-11:00"]
    },
    {
        "doctor_id": "DOC_2",
        "department_id": "GENERAL_OPD",
        "available_slots": ["09:00-10:00"]
    },
    {
        "doctor_id": "DOC_3",
        "department_id": "ORTHO",
        "available_slots": ["10:00-11:00"]
    },
    {
        "doctor_id": "DOC_4",
        "department_id": "ORTHO",
        "available_slots": ["10:00-11:00"]
    }
]

# In-memory token storage
tokens = []

# Priority order (lower number = higher priority)
PRIORITY_ORDER = {
    "EMERGENCY": 1,
    "PAID": 2,
    "FOLLOW_UP": 3,
    "ONLINE": 4,
    "WALK_IN": 5
}
