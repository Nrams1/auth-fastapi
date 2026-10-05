# User Authentication Service
A secure, asynchronous RESTful backend service providing robust user authentication, registration, and session management. Built using a modern Python microservices architecture.

## Tech Stack
- Core : Python 3.14 , FastAPI 0.135.3
- Database & Migration : PostgreSQL ,SQLAlchemy ORM
- Security : PyJWT , Bcrypt
- DevOps : Pytest , Docker 

## Architecture & Design Decisions
### 1. System Design:
Structured the application into clear layers (API, service, and data access), ensuring business logic is decoupled from external frameworks and infrastructure components.

### 2. Authentication & Authorization:
Implemented secure authentication using Bcrypt for password hashing and JSON Web Tokens (JWT) via PyJWT for secure token-based authorization.

### 3. Database Integration:
Implemented a custom data access layer using raw SQL queries with PostgreSQL, ensuring full control over query performance and database interactions without relying on an ORM. Database schema changes are managed using Alembic.

### 4. Comprehensive Testing:
Built a full test suite using Pytest, covering unit and integration tests with isolated test environments for reliable validation of database and API logic.

### 5. Containerization:
Used Docker and Docker Compose to containerize the application and PostgreSQL database, ensuring consistent environments across development and deployment.



