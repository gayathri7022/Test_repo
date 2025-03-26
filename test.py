from login import log, dic

def test_log():
    assert log("Arun","Arun@134") == True

    assert log() == False

    