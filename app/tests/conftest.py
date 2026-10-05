# conftest.py (The Easier, Docker-Free SQLite Alternative)
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker


from app.data_access.db import Base, get_db
from app.main import app

# Import components from your main application


@pytest.fixture(scope="session")
def db_engine():
    """No Docker required. Creates a transient database entirely in Python memory."""
    # 'sqlite:///:memory:' signals SQLAlchemy to build the DB inside RAM
    # StaticPool prevents SQLite from closing and deleting connections between steps
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    Base.metadata.create_all(bind=engine)
    return engine

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Provides an isolated database session and clears it out afterward."""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Wipe tables clean after every test function
        with db_engine.connect() as connection:
            with connection.begin():
                for table in reversed(Base.metadata.sorted_tables):
                    connection.execute(table.delete())

@pytest.fixture(scope="function")
def client(db_session):
    """Overrides the real database link with our running SQLite session."""
    def _get_db_override():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_db_override
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def mock_db():
    return MagicMock()


