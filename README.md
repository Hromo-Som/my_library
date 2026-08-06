# 📚 MyLibrary

**MyLibrary** — это RESTful API-сервис для управления библиотекой книг.  
Проект написан на **FastAPI** с использованием асинхронной **SQLAlchemy 2.0** и **SQLite** в качестве базы данных.

---

## 🚀 🛠 Стек технологий которые использовал
* **Python 3.11+**
* **FastAPI** — высокопроизводительный веб-фреймворк
* **SQLAlchemy 2.0** — ORM для работы с базой данных
* **SQLite + aiosqlite** — легкая асинхронная база данных
* **Pydantic V2** — валидация данных и схемы
* **Сервер** — Uvicorn

---

## 📋 Основные возможности

- ✅ Получение списка книг
- 📖 Получение книги по ID
- ➕ Добавление новой книги
- ✏️ Полное обновление книги (PUT)
- 🗑️ Удаление книги

---

## 📂 Структура проекта

my_library/
├── main.py              # Запуск приложения, подключение роутеров
├── database.py          # Настройка движка (Engine) и сессий
├── models/              # SQLAlchemy модели (Таблицы)
│   └── books.py
├── schemas/             # Pydantic схемы (Валидация)
│   └── books.py
├── routers/             # Эндпоинты (HTTP логика)
│   └── books.py
└── repository.py        # Логика работы с БД (SQL-запросы)

---

## 🛠️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/yourusername/MyLibrary.git
cd MyLibrary
```

### 2. Создать виртуальное окружение

Windows (CMD):
```bash
python -m venv venv
venv\Scripts\activate
```

Windows (Git Bash):
```bash
python -m venv venv
source venv/Scripts/activate
```

MacOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить сервер

```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу:
👉 http://127.0.0.1:8000

### 5. Интерактивная документация

FastAPI автоматически генерирует документацию:

| Документация  | Ссылка                                   |
|---------------|------------------------------------------|
| **Swagger UI** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)   |
| **ReDoc**      | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

---

## 📚 Эндпоинты API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `GET` | `/books` | Получить список всех книг |
| `GET` | `/books/{id}` | Получить книгу по ID |
| `POST` | `/books` | Создать новую книгу |
| `PUT` | `/books/{id}` | Полностью обновить книгу |
| `DELETE` | `/books/{id}` | Удалить книгу |

> Подробные примеры запросов и ответов доступны в интерактивной документации Swagger по адресу `/docs`.

---

## 👨‍💻 Автор

**Хайдаров Темур**  
- GitHub: [@Hromo-Som](https://github.com/Hromo-Som)