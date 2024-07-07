from fastapi import FastAPI

from db.db_setup import engine
from api import admin, questions, student
from models import admin_model, questions_models

admin_model.Base.metadata.create_all(bind=engine)
questions_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router)
app.include_router(questions.router)
app.include_router(student.router)

@app.get("/")
async def root():
    return {"message": "Hello World, Welcome to Csc202"}