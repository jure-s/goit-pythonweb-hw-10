
# 📞 Contacts API (FastAPI + PostgreSQL + Docker + Auth)

## 📌 Опис проєкту
Цей проєкт – повноцінний REST API для **керування контактами з аутентифікацією, авторизацією**, обробкою **днів народження**, **пошуком**, а також підтримкою **завантаження аватара** та **верифікації email**.

### 🔹 **Функціонал API:**
✅ CRUD для контактів  
✅ Пошук за іменем, прізвищем, email  
✅ Контакти з днями народження на 7 днів уперед  
✅ Аутентифікація (JWT-токени)  
✅ Реєстрація користувача з email-підтвердженням  
✅ Авторизація користувача (доступ лише до своїх контактів)  
✅ Обмеження запитів до `/auth/me`  
✅ Завантаження аватара  
✅ Підтримка CORS  
✅ Swagger / Redoc документація  

---

## ⚙️ **Встановлення та запуск**
### **🔹 1️⃣ Клонування репозиторію**
```bash
git clone https://github.com/jure-s/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

### **🔹 2️⃣ Створення та активація віртуального середовища**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### **🔹 3️⃣ Встановлення залежностей**
```bash
pip install -r requirements.txt
```

### **🔹 4️⃣ Налаштування `.env` файлу**
Створи файл `.env` у корені проєкту та додай:
```
DATABASE_URL=postgresql://postgres:твій_пароль@localhost:5433/contacts_db
SECRET_KEY=твій_секретний_ключ
MAILGUN_API_KEY=ключ_від_mailgun
MAILGUN_DOMAIN=тестовий_домен
MAILGUN_SENDER=email_відправника
BASE_URL=http://127.0.0.1:8000
REDIS_URL=redis://localhost:6379
AVATAR_STORAGE_PATH=app/static/avatars
```

---

## 🐳 **Docker запуск**
### **🔹 Запуск усіх сервісів**
```bash
docker-compose up --build
```

> Запускається:
- PostgreSQL (порт 5433)
- FastAPI (порт 8000)

---

## 🚀 **Swagger документація**
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)  
🔗 [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛡️ **Аутентифікація / Авторизація**
### 🔐 Реєстрація користувача
**POST /auth/signup**
```json
{
  "username": "myuser",
  "email": "user@example.com",
  "password": "strongpassword"
}
```

📧 На email надійде посилання для підтвердження акаунта `/auth/verify/{token}`

### 🔐 Логін
**POST /auth/login** (формат `x-www-form-urlencoded`)
```
username=user@example.com
password=strongpassword
```

📥 Отриманий `access_token` додається як Bearer токен до усіх запитів

---

## 👤 **Профіль користувача**
### `GET /auth/me`  
(використано обмеження: 5 запитів/хвилину)

### `POST /auth/avatar`  
Завантаження зображення (тип: `multipart/form-data`)

---

## 👥 **Контакти (авторизовані запити)**
CRUD + фільтри

- `POST /contacts/`
- `GET /contacts/`
- `GET /contacts/{id}`
- `PUT /contacts/{id}`
- `DELETE /contacts/{id}`
- `GET /contacts/search/?name=...&email=...`
- `GET /contacts/upcoming_birthdays/`

---

## 🧪 **Тестування API**
```bash
http POST http://localhost:8000/auth/signup username=test email=test@mail.com password=123456
http POST http://localhost:8000/auth/login username=test@mail.com password=123456
http GET http://localhost:8000/contacts/ "Authorization: Bearer <token>"
```

---

## 🗄️ **База даних**
📌 Створити локально:
```sql
CREATE DATABASE contacts_db;
```

📌 Якщо через Docker — буде створено автоматично.

---

## 📁 **Структура проєкту (основне)**
```
app/
├── main.py
├── config.py
├── database/
├── routes/
├── services/
├── static/
│   └── avatars/
```

---

## 🛡️ **Безпека**
✅ Хешування пароля через `passlib`  
✅ Токенізація через `JWT`  
✅ Всі паролі/ключі — у `.env`

---

## 🧼 **Style та CI**
✅ Валідація Pydantic  
✅ CORS  
✅ Dockerized  
✅ Swagger UI  
✅ PostgreSQL + Redis підтримка  
✅ Розширюваність структури

---

## 📬 **Підтвердження Email**
🔗 Працює через Mailgun API.  
⚠️ Не забудь активувати тестовий домен та додати API ключ.

---

## 🏁 Завершення
📌 Ти можеш повноцінно керувати своїми контактами після реєстрації та верифікації email.

🤝 Усі запити захищені, всі дані — твої.

---

> Проєкт виконаний у рамках курсу **"FullStack Web Development with Python"** від **GoIT**.  
 
