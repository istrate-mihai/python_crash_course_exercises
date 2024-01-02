from user import User

class Admin(User):
    def __init__(self, last_name, first_name, email, age, privileges):
        super().__init__(last_name, first_name, email, age)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print('Privilege: ' + privilege)
