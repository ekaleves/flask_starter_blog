# 📝 Flask Starter Blog

A simple but professional blogging platform built with **Flask**, designed to demonstrate clean architecture, the application factory pattern, and modular CRUD separation using SQLAlchemy.

This project is ideal for showcasing Flask fundamentals while following real-world design patterns.

---

## 🚀 Features

✅ Create, edit, and delete blog posts  
📅 Posts are timestamped and ordered by newest  
🧱 Modular architecture with `crud.py` separation  
📦 Uses the application factory pattern  
🛡️ Environment variables handled via `.env`  
🎯 SQLite for easy setup (can be replaced with PostgreSQL)

---

## 🔧 Tech Stack

| Tool           | Purpose                             |
|----------------|-------------------------------------|
| Flask          | Web framework                       |
| SQLAlchemy     | ORM for database modeling           |
| SQLite         | Lightweight local database          |
| Python-dotenv  | Environment variable management     |
| Jinja2         | HTML templating engine (Flask core) |

---

## 💡 Design Notes

- Use the Application Factory Pattern for clean initialization.
- Follows the Separation of Concerns principle: routes and business logic live in different files.
- Prepares the project for easy extension (user auth, admin panel, etc.)
- Can be swapped to use PostgreSQL or MySQL just by changing the database URL.

