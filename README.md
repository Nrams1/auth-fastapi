****Developed a production-grade REST API from scratch using Python and FastAPI, designed with a clean layered architecture to ensure separation of concerns, maintainability, and testability. The project demonstrates modern backend engineering best practices, including:**** 

**System Design:**
Structured the application into clear layers (API, service, and data access), ensuring business logic is decoupled from external frameworks and infrastructure components.

**Configuration Management:**
Used Pydantic Settings with environment variables for type-safe and centralized configuration management.

**API Framework & Validation:**
Built high-performance RESTful APIs using FastAPI with automatic request validation, serialization, and OpenAPI documentation.

**Database Integration:**
Implemented a custom data access layer using raw SQL queries with PostgreSQL, ensuring full control over query performance and database interactions without relying on an ORM. Database schema changes are managed using Alembic.

**Authentication & Authorization:**
Implemented secure authentication using Passlib for password hashing and JSON Web Tokens (JWT) via python-jose for secure token-based authorization.

**Dependency Management:**
Leveraged FastAPI dependency injection to manage services and data access components, ensuring modular and testable code.

**Containerization:**
Used Docker and Docker Compose to containerize the application and PostgreSQL database, ensuring consistent environments across development and deployment.

**Asynchronous Processing:**
Utilized FastAPI’s async capabilities to handle concurrent requests efficiently and improve API throughput.

**Comprehensive Testing:**
Built a full test suite using Pytest, covering unit and integration tests with isolated test environments for reliable validation of database and API logic.

**Asynchronous Messaging (Optional):**
Integrated Apache Kafka for event-driven communication and background processing where applicable.

**API Monitoring & Observability:**
Integrated Prometheus to expose key metrics such as request counts, latency, and error rates for real-time system observability.


**CI/CD Automation:**
Configured pipelines using GitHub Actions to automate testing, linting, and build processes on every commit.
