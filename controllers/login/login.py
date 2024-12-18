from models.loginModel import validateUser

def login_controller (username, password): 
    return validateUser(username, password)
            
