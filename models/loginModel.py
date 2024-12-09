import json

file ="data/user.json"

def loadUser():
    with open(file, "r") as f:
        data = json.load(f)
        return data.get("users", [])
    
def validateUser(username, password):
    users = loadUser()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False