from sqlalchemy.orm import Session
from app.database.models import Contact, User
from app.database.schemas import (
    ContactCreate, ContactUpdate,
    UserCreate, UserResponse
)
from app.services.security import hash_password, verify_password as verify_password_service  # Оновлюємо імпорт

# 🔹 Операції з користувачами (User)
def create_user(db: Session, user: UserCreate) -> UserResponse:
    """Створення нового користувача з хешуванням пароля"""
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserResponse(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email,
        is_verified=db_user.is_verified,
        avatar_url=db_user.avatar_url,
        created_at=db_user.created_at,
        updated_at=db_user.updated_at
    )

def get_user_by_email(db: Session, email: str):
    """Отримання користувача за email"""
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    """Отримання користувача за ID"""
    return db.query(User).filter(User.id == user_id).first()

# 🔹 Операції з контактами (Contact)
def create_contact(db: Session, contact: ContactCreate, user_id: int):
    """Створення нового контакту"""
    db_contact = Contact(
        **contact.dict(),
        user_id=user_id
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, user_id: int):
    """Отримання всіх контактів користувача"""
    return db.query(Contact).filter(Contact.user_id == user_id).all()

def get_contact_by_id(db: Session, contact_id: int, user_id: int):
    """Отримання контакту за ID (тільки якщо він належить користувачеві)"""
    return db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == user_id).first()

def update_contact(db: Session, contact_id: int, contact: ContactUpdate, user_id: int):
    """Оновлення контакту"""
    db_contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == user_id).first()
    if db_contact:
        for key, value in contact.dict(exclude_unset=True).items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int, user_id: int):
    """Видалення контакту"""
    db_contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == user_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact

# 🔹 Функція для перевірки паролю
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Перевіряє, чи введений пароль відповідає збереженому хешу."""
    return verify_password_service(plain_password, hashed_password)  # Викликаємо правильну функцію

