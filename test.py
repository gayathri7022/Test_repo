from login import log

def test_valid_login():
    assert log("Arun", "Arun@134") == True

def test_invalid_username():
    assert log("hdjds", "Arun@134") == "Invalid user"

def test_wrong_password():
    assert log("Navya", "27362872") == False

def test_short_password():
    assert log("Asha", "grfijkjh") == "Password length must be of 8 characters long."