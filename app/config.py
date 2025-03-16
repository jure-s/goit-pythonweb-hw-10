import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Завантажуємо змінні середовища з .env
load_dotenv()

# Перевірка, чи завантажено DATABASE_URL та SECRET_KEY
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")

# Отримуємо URL бази даних
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Якщо змінна не була знайдена, вивести повідомлення
if SQLALCHEMY_DATABASE_URL is None:
    print("ERROR: DATABASE_URL is not set.")
else:
    print(f"Using database: {SQLALCHEMY_DATABASE_URL}")  # Додаємо вивід для перевірки

# Створюємо двигун бази даних
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Створюємо фабрику сесій
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей SQLAlchemy
Base = declarative_base()

# Імпортуємо всі моделі, щоб Alembic бачив їх
from app.database import models
