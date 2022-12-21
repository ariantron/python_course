class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == 'admin' and self.password == '123456':
            print("Login is successful")
        else:
            print("Error in login")


u = User("admin", "123456")
u.login()
