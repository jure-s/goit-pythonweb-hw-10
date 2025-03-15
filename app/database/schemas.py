from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# Схема для створення контакту
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: Optional[date] = None
    extra_info: Optional[str] = None

# Схема для оновлення контакту (всі поля необов'язкові)
class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    birthday: Optional[date] = None
    extra_info: Optional[str] = None

# Схема для відображення контакту
class ContactResponse(ContactCreate):
    id: int

    class Config:
        from_attributes = True
