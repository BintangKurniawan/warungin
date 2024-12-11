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
            print(f"Password atau username salah. Anda memiliki {attempts} kesempatan lagi.")

        if attempts == 0:
            print("Anda telah gagal login 3 kali. Silakan coba lagi nanti.")
            exit()

