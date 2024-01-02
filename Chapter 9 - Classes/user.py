class User:
    def __init__(self, last_name, first_name, email, age):
        self.last_name      = last_name
        self.first_name     = first_name
        self.email          = email
        self.age            = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'''The user\'s data:\n
                LastName: {self.last_name}\n
                FirstName: {self.first_name}\n
                Email: {self.email}\n
                Age: {self.age}.
            ''')

    def greet_user(self):
        print(f'Hello {self.last_name} {self.first_name}.\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
