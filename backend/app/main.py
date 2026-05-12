from fastapi import FastAPI
from app.routers import users #imports users file from routers

app = FastAPI()
app.include_router(users.router)

@app.get("/")

def health_check():
    return {"status": "ok"}