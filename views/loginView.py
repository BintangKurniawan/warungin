from controllers.login.login import login_controller
def login():
    attempts = 3
    while attempts > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if login_controller(username, password):
            print("Login successful! Welcome!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Login gagal. Anda memiliki {attempts} kesempatan lagi.")
            else:
                print("Anda telah kehabisan kesempatan. Silakan coba lagi nanti.")
                exit()

