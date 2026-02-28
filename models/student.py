from models.user import User
from database.db import db, Query

class Student(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, role="ETUDIANT")
        self.courses = []
        self.certifs = []
        self.account = 0
        
    def addAccount(self,amount):
        self.account += amount

    def save(self):
        """Sauvegarder l'utilisateur dans la base de donnees"""
        users_table = db.table('users')
        users_table.insert({
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'etat':self.etat,
            "courses": [],
            "certifs": [],
            "account":self.account,
        })
    
    def get_account(self):
        user_table = db.table("users")
        query = Query()
        amount = user_table.get(query.email == self.email)["account"]
        return amount

    def get_courses(self):
        pass

    def get_certifs(self):
        pass