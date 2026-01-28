from fastapi import FastAPI
from routes import router

app = FastAPI(title="OPD Token Allocation Engine")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "OK"}
