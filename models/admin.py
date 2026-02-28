from models.user import User

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, role="ADMIN")
