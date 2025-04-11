from login import log

def test_cases():
    assert log("Arun", "Arun@134") == True

    assert log("hdjds", "Arun@134") == "Invalid user"

    assert log("Navya", "27362872") == False

    assert log("Asha", "grfijkjh") == False