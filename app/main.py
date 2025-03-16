import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from app.routes import contacts, users, auth  # 👈 Додаємо auth

app = FastAPI(title="Contacts API with Authentication")

# Налаштування OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Увімкнення CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволяємо запити з усіх джерел (можна змінити на конкретні домени)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключаємо маршрути
app.include_router(contacts.router)
app.include_router(users.router)
app.include_router(auth.router)

# Головна сторінка API
@app.get("/")
def root():
    return {"message": "Welcome to Contacts API"}

# Перевірка токена (для Swagger UI)
@app.get("/secure-endpoint/")
def secure_endpoint(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid"}
