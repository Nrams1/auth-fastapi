
import pytest
from app import security
from unittest.mock import patch

from app.data_access import users_db
from app.schema import User, UserResponse
from app.services.user_service import create_new_user



"""
Password hashing Test Cases:
1: Password is Hashed
2: Empty Password
"""
def test_hash_password_success():
    """Check password is hashed successfully"""

    user_pass = "This_is_a_mock_pass"
    hash_pass =  security.hash_password(user_pass)

    assert hash_pass != user_pass


def test_hash_password_empty_pass_exception():
    """Check empty password is not hashed"""

    user_pass = ""
   

    with pytest.raises(ValueError, match="Password cannot be empty!"):security.hash_password(user_pass)


"""
Password Verification Test Cases:
1: verify plain pass against valid hashed pass
2: verify plain pass against invalid hashed pass
"""

def test_verify_valid_password():

    user_pass = "verify_pass"
    hash_pass =  security.hash_password(user_pass)

    assert security.verify_password (user_pass,hash_pass)

def test_verify_invalid_password():

    user_pass = "verify_pass"
    hash_pass =  security.hash_password(user_pass)
    wrong_pass = "wrong_pass"
    
    assert security.verify_password (wrong_pass,hash_pass) is False


"""
Token Creation Test Cases:
1: New Token Created
2: Token Not created , return is None
"""

def test_new_token_created():

    dict_data = {"sub":"1"}

    assert len(security.create_access_token(dict_data)) != 0
    assert isinstance(security.create_access_token(dict_data),str)

""""
def test_new_token_not_created():

    dict_data = {}

    with pytest.raises(ValueError,match="Could not generate authentication token."):security.create_access_token(1) 

"""

#
# @patch("app.services.user_service.hashpassword")
def test_create_new_user(mock_db,mocker):

    user = User(email="test@gmail.com",password ="pass")
    return_user = {"id":"1","email":"test@gmail.com"}
    # Optional: If your function checks for existing users via a query first:
    mock_retr = mocker.patch.object(mock_db, "app.services.user_service.retrieve_user_by_email")
    mock_retr.return_value.filter_by.return_value.first.return_value = None

    mock_hash = mocker.patch("app.services.user_service.hash_password")
    mock_hash.return_value = "Hashed_pass"


    def mock_refresh_side_effect(obj):
        obj.id = "1"

    mock_db.refresh.side_effect = mock_refresh_side_effect

    result = create_new_user(mock_db,user)

    assert result is not None
    assert result is not None
    assert result.id == "1"
    mock_db.add.assert_called_once_with(user)
    mock_db.commit.assert_called_once()





    