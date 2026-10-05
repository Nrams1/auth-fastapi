



from app.data_access.users_db import retrieve_user_by_email
from app.routers.users import create_user
from app.data_access.model import User



"""

def test_register_user_unit():
    
    # 1. Arrange: Fake the database session completely
    mock_db = MagicMock()
    
    # Configure the mock to return None (simulating that the email doesn't exist yet)
    mock_db.query.return_method().filter.return_method().first.return_value = None
    
    # Prepare mock input data
    test_input = User(email="test@example.com", password="password123")
    
    # 2. Act: Call the endpoint function directly like a standard Python function
    response = create_user(user= test_input, db=mock_db)
    
    # 3. Assert: Verify the business logic and database interactions
    assert response.status_code == 400
    
    # Verify that the function actually tried to save the user to the database
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()

"""

def test_create_user_success(client):
    """Verifies that a new user is successfully written to the database via HTTP."""

    payload = {"email": "testuser@example.com", "password": "supersecurepassword"}
    
    response = client.post("/users", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == "testuser@example.com"


def test_create_user_duplicate_email(client, db_session):
    """Tests that registering an already existing email returns a 400 error."""
    # 1. ARRANGE: Manually inject an "already existing" user into the test database
    existing_user = User(email="duplicate@example.com", password="hashed_password123")
    db_session.add(existing_user)
    db_session.commit()  # Save it permanently for this specific test run

    # 2. ACT: Attempt to register a new user using the exact same email via the API
    payload = {"email": "duplicate@example.com", "password": "newpassword123"}
    response = client.post("/users", json=payload)
    
    # 3. ASSERT: Verify that your FastAPI application rejects the request safely
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this email already exist"

def test_retrieve_user_by_email_success(db_session ):

    existing_user = User(email="test@gmail.com", password="hashed_password123")
    db_session.add(existing_user)
    db_session.commit()  # Save it permanently for this specific test run
    
        # 2. ACT: Attempt to register a new user using the exact same email via the API
    response = retrieve_user_by_email(db_session,"test@gmail.com")

    assert isinstance(response ,User)