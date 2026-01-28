# OPD Token Allocation Engine

A backend service for hospital OPD token allocation that supports **elastic capacity management**, **doctor load balancing**, and **priority-based scheduling**. This project is designed as a real-world backend system suitable for an intern / junior backend engineer assignment.

---

## 🚀 Objective

The goal of this system is to efficiently allocate OPD tokens across doctors and time slots while handling real-world scenarios such as:

* Limited per-slot capacity
* Multiple token sources with different priorities
* Cancellations and no-shows
* Emergency patient insertions
* Dynamic reallocation of waitlisted patients

---

## 🏥 Problem Context

* Doctors work in **fixed time slots** (e.g. `09:00–10:00`)
* Each doctor has a **hard per-slot capacity**
* Patients request tokens from multiple sources:

  * Emergency
  * Paid Priority
  * Follow-up
  * Online booking
  * Walk-in

The system must ensure fairness, enforce limits, and still allow emergency overrides.

---

## 🧠 High-Level Design

* Doctors are the **source of truth** (department + available slots)
* Tokens are dynamically assigned to the **least-loaded doctor**
* When capacity is exceeded:

  * Lower-priority tokens are waitlisted
  * Emergency tokens can preempt existing tokens
* On cancellation, the **highest-priority waitlisted token** is promoted

---

## ⚙️ Tech Stack

* **Language:** Python 3.11
* **Framework:** FastAPI
* **API Docs:** Swagger (OpenAPI)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Storage:** In-memory (for simulation purposes)

---

## 📁 Project Structure

```
opd-token-engine/
│
├── main.py            # App entry point
├── routes.py          # API routes
├── logic.py           # Core allocation logic
├── data.py            # In-memory data stores
├── models.py          # Pydantic models
├── simulate_day.py    # OPD day simulation
├── requirements.txt
├── Dockerfile
└── .github/workflows/ci.yml
```

---

## 🔁 Token Prioritization Logic

Priority order (1 = highest):

1. EMERGENCY
2. PAID
3. FOLLOW_UP
4. ONLINE
5. WALK_IN

Rules:

* Emergency tokens can **replace the lowest-priority confirmed token**
* Non-emergency tokens are waitlisted if capacity is full
* On cancellation, highest-priority waitlisted token is promoted

---

## 🔌 API Endpoints

### Token APIs

* `POST /tokens` → Create a token
* `POST /tokens/{token_id}/cancel` → Cancel token
* `GET /tokens` → List all tokens

### Doctor APIs

* `POST /doctors` → Add doctor (hospital/admin use)
* `GET /doctors` → List doctors

Swagger UI available at:

```
http://localhost:8000/docs
```

---

## 🧪 Simulation

The `simulate_day.py` script simulates:

* Multiple doctors
* Multiple departments
* Random patient arrivals
* Emergency insertions
* Cancellations

This helps validate real-world OPD behavior.

---

## 🐳 Running with Docker

### Build image

```bash
docker build -t opd-token-engine .
```

### Run container

```bash
docker run -p 8000:8000 opd-token-engine
```

---

## 🔄 CI/CD

A GitHub Actions pipeline automatically:

* Installs dependencies
* Performs sanity import checks
* Runs on every push / PR to `main`

---

## ⚠️ Edge Cases Handled

* Slot capacity overflow
* Emergency preemption
* Multiple doctors per department
* Token cancellation and reallocation
* Empty department / unavailable slot

---

## 📌 Trade-offs

* Uses in-memory storage for simplicity
* No authentication persistence (can be extended)
* Designed for clarity over scale

---

## 🔮 Future Improvements

* Database integration (PostgreSQL)
* Role-based authentication (JWT)
* Doctor availability management UI
* Metrics & monitoring
* Rate limiting

---

## 👤 Author

Backend Intern Assignment Project

---

## ✅ Status

✔ Core logic implemented
✔ Dockerized
✔ CI/CD enabled
✔ Simulation included

This project demonstrates **practical backend system design** with real-world constraints.

<img width="1881" height="843" alt="Screenshot 2026-01-29 035229" src="https://github.com/user-attachments/assets/61218bdd-019e-4083-9553-395bb5b9d6d7" />
<img width="1848" height="684" alt="Screenshot 2026-01-29 035257" src="https://github.com/user-attachments/assets/6e7168d2-00d8-42c5-a79b-ac4a221c638b" />
<img width="1821" height="586" alt="Screenshot 2026-01-29 035316" src="https://github.com/user-attachments/assets/bf07db27-2aa9-4d03-bb43-d25cf99b6af5" />
<img width="1835" height="908" alt="Screenshot 2026-01-29 035335" src="https://github.com/user-attachments/assets/a104c9c4-f1bc-443c-8d61-462b199e8c56" />
<img width="1823" height="913" alt="Screenshot 2026-01-29 035357" src="https://github.com/user-attachments/assets/df4e7a9e-59b0-48bf-a79a-c6d0daa99430" />
<img width="1819" height="695" alt="Screenshot 2026-01-29 035410" src="https://github.com/user-attachments/assets/09f6bc04-522b-4758-a908-c99fe57a5173" />

