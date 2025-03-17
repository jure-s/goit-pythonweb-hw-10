import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi_limiter.depends import RateLimiter
from app.config import init_limiter  # Ініціалізація Rate Limiter
from app.routes import contacts, users, auth  # Додаємо auth

app = FastAPI(title="Contacts API with Authentication")

# Налаштування OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# 🔹 Увімкнення CORS (дозволяє запити з різних джерел)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволяє всі домени (замінити на список для обмежень)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Підключаємо маршрути
app.include_router(contacts.router)
app.include_router(users.router)
app.include_router(auth.router)

# 🔹 Головна сторінка API
@app.get("/")
def root():
    return {"message": "Welcome to Contacts API"}

# 🔹 Перевірка токена (для Swagger UI)
@app.get("/secure-endpoint/")
def secure_endpoint(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid"}

# 🔹 Ініціалізація Rate Limiter при старті сервера
@app.on_event("startup")
async def startup():
    await init_limiter()

