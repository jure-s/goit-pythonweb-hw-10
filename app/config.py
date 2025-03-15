import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Завантажуємо змінні середовища
load_dotenv()

# Отримуємо URL бази даних
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Using database: {DATABASE_URL}")  # Додаємо вивід для перевірки

# Створюємо двигун бази даних
engine = create_engine(DATABASE_URL)

# Створюємо фабрику сесій
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей SQLAlchemy
Base = declarative_base()
