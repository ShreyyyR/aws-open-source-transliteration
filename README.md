# AWS / Open Source Transliteration/Translation Service

A FastAPI-based web application that provides **English → Kannada transliteration/translation** using two methods:

1. **Open Source Transliteration** (`indic-transliteration`)
2. **AWS Translate API**

It also stores user profile data (name and address) in both English and Kannada using a database.

---

## 🚀 Features

* Web form for user input (name, address).
* Real-time transliteration via API (`/transliterate`).
* Option to choose between **open-source** and **AWS Translate**.
* Stores English + Kannada data in database.
* FastAPI + SQLAlchemy + Jinja2Templates integration.

---

## 📂 Project Structure

```
AWS-Translation-Service/
│── main.py                # FastAPI app
│── models.py              # Database models
│── database.py            # Database connection
│── transliterate.py       # Transliteration methods (open source + AWS)
│── templates/
│    └── form.html         # HTML form for input
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AWS-Translation-Service.git
cd AWS-Translation-Service
```

2. Create virtual environment & activate:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠 Dependencies

Add these to **requirements.txt**:

```
fastapi
uvicorn
jinja2
sqlalchemy
pydantic
indic-transliteration
boto3
```

---

## 🔑 AWS Setup

1. Go to [AWS Console](https://console.aws.amazon.com/).
2. Create an **IAM user** with `AmazonTranslateFullAccess`.
3. Download Access & Secret keys.
4. Configure AWS credentials:

```bash
aws configure
# Provide Access Key, Secret Key, region (ap-south-1)
```

---

## ▶️ Running the App

Start the server:

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints

### 1. Home Form

```
GET /
```

Displays form to enter **Name** and **Address**.

### 2. Submit Form

```
POST /submit
```

Stores user data (English + Kannada) in DB.

### 3. Transliteration API

```
POST /transliterate
```

Request body:

```json
{
  "text": "Bengaluru",
  "method": "aws"
}
```

Response:

```json
{
  "translated": "ಬೆಂಗಳೂರು"
}
```

---

## 🗄 Database

* Using **SQLAlchemy ORM** with SQLite/MySQL.
* Model: `UserData` with fields: `id, name_en, name_kn, address_en, address_kn`.

---

## ✨ Future Improvements

* Add support for more Indian languages.
* Add JWT auth for API endpoints.
* Frontend improvements (real-time preview).

---

## 📜 License

MIT License
