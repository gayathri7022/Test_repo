dic = {"Arun": "Arun@134", "Navya":"Navya@37", "Asha":"Asha8838"}

def log(name,pas):
    if name in dic:
        if len(pas) == 8:
            if pas == dic[name]:
                return True
            else:
                return False

        else:
            print("Password length should be 8 characters long.")


res = log("Asha","Asha8838")
print(res)