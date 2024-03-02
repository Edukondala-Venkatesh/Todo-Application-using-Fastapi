# FastAPI Todo Application

This is a simple Todo application built using FastAPI, showcasing CRUD operations, database integration, user authentication, and more.

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Edukondala-Venkatesh/Todo-Application-using-Fastapi.git
   cd Todo-Application-using-Fastapi
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
```bash
uvicorn main:app --reload
```

The app will be running at `http://127.0.0.1:8000`.

## Database Integration

### Schema Design
- Database: SQLite/PostgreSQL/Your Choice
- Schema:
  - `id`: Todo item ID (integer)
  - `title`: Todo item title (string)
  - `description`: Todo item description (string)
  - `created_at`: Timestamp of creation (datetime)
  - `completed`: Completion status (boolean)

## CRUD Operations

### API Endpoints
- **Create Todo**: `POST /todos`
- **Read Todo List**: `GET /todos`
- **Read Todo by ID**: `GET /todos/{todo_id}`
- **Update Todo by ID**: `PUT /todos/{todo_id}`
- **Delete Todo by ID**: `DELETE /todos/{todo_id}`

## Data Validation
- Pydantic models for request and response validation.

## Authentication
- Basic user authentication.
- Secure CRUD operations for authenticated users.

## Error Handling
- Custom error handling for scenarios like invalid requests, unauthorized access, and server errors.

## Additional Features
- Project Structure: Consistent & predictable
- Validations using Pydantic
- Security
  - Authentication of API
  - CORS
- Resource Naming
- Versioning Capabilities
- Pagination (First, last next, pre)
- Exception/Error Handling
- Retry option.
- Translations
- Basic filtration where you can pass filtration for any field.
- Async Calls
- Sorting
- Coding Best practices/Documentation

## Contributing
Feel free to contribute to the project. Create a pull request, report issues, or suggest features.
