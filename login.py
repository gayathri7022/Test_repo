dic = {"Arun": "Arun@134", "Navya":"Navya@37", "Asha":"Asha8838"}

def log(name,pas):
    if name in dic:
        if len(pas) == 8:
            if pas == dic[name]:
                return True
            else:
                return False

        else:
            return "Password length must be of 8 characters long."

    else:
        return "Invalid user"

log("Arun","Arun@134")
log("hdjds","Arun@134")
log("Navya", "27362872")
log("Asha", "grfijkjh")

