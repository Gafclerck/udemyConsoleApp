from tinydb import Query
from database.db import db

class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.etat = 1
        
    def save(self):
        """Sauvegarder l'utilisateur dans la base de donnees"""
        users_table = db.table('users')
        users_table.insert({
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            "etat":self.etat
        })
        
    @staticmethod
    def findByEmail(email):
        """Trouver un utilisateur par son email"""
        users_table = db.table('users')
        UserQuery = Query()
        return users_table.get(UserQuery.email == email)
    
    @classmethod
    def getAll():
        #recuperer et renvoyer tous les users
        pass

    def update(self , updated_values):
        # mettreajour le user avec les nouvelles values (updated values)
        pass