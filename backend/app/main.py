from fastapi import FastAPI
from app.routers import users #imports users file from routers
from app.database import engine, Base

Base.metadata.create_all(bind=engine) #creates tables in database based on models defined in Base

app = FastAPI()
app.include_router(users.router)

@app.get("/")

def health_check():
    return {"status": "ok"}