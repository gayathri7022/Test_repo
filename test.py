from login import log

name = "Arun"
pas = "Arun@134"

name1 = "Ar"
pas1 = "Arun@134"


assert log(name, pas) == True

assert log(name1,pas1) == "Invalid user"  

