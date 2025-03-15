from fastapi import FastAPI
from app.routes import contacts

app = FastAPI(title="Contacts API")

# Підключаємо маршрути
app.include_router(contacts.router)

# Головна сторінка API
@app.get("/")
def root():
    return {"message": "Welcome to Contacts API"}
