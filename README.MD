# Blog API

A RESTful API for managing blog posts and users, built with FastAPI and SQLAlchemy.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Features

- CRUD operations for blog posts
- Search functionality across post content
- PostgreSQL database integration
- Alembic for database migrations
- Pydantic data validation
- CORS support

## Prerequisites

- Python 3.10+
- PostgreSQL
- pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Noka993/blog-api.git
   cd blog-api
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the environment variables**:

   Create a `.env` file in the root directory and add the necessary environment variables, such as:

   ```env
   DATABASE_URL=sqlite:///./blog.db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```
   
## Migrations

To generate and apply Alembic migrations:

```bash
alembic revision --autogenerate -m "Migration message"
alembic upgrade head
```

## API Documentation

FastAPI provides interactive API documentation available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint       | Description                          |
|--------|----------------|--------------------------------------|
| GET    | `/posts`       | Get all posts (with optional search) |
| GET    | `/posts/{id}`  | Get a single post by ID              |
| POST   | `/posts`       | Create a new post                    |
| PUT    | `/posts/{id}`  | Update an existing post              |
| DELETE | `/posts/{id}`  | Delete a post                        |

## License

This project is licensed under the MIT License.