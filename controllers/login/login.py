from models.loginModel import validateUser

def login_controller (username, password): 
    credentials_valid = False

    while not credentials_valid:
        if validateUser(username, password):
            print("Login successful! Welcome!")
            credentials_valid = True
        else:
            print("Password atau username salah. Silakan coba lagi.")
            # Prompt for new username and password
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
