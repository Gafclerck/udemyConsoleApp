from models.user import User
from database.db import db

class Prof(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, role="PROFESSEUR")
        self.courses = []

    def save(self):
        """Sauvegarder l'utilisateur dans la base de donnees"""
        users_table = db.table('users')
        users_table.insert({
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'courses' : self.courses,
            'etat': self.etat
        })