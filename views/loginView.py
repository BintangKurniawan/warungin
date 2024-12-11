from controllers.login.login import login_controller
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    login_controller(username, password)

