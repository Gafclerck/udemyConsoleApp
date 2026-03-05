from models.user import User
from models.course import Course
from database.db import db, Query
from tinydb import where

class Student(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, role="ETUDIANT")
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
            "certifs": [],
            "account":self.account,
        })

    def get_account(self):
        user_table = db.table("users")
        query = Query()
        amount = user_table.get(query.email == self.email)["account"]
        return amount

    def get_courses(self):
        course_table = db.table("courses")
        courses = course_table.search(where('enrolled_students').test(lambda x: self.email in x))
        return [Course(
                i["title"], 
                i["content"],
                int(i["price"]),
                i["prof_email"],
                i["id"],
                i["enrolled_students"]
            ) for i in courses
            ]

    def get_certifs(self):
        pass