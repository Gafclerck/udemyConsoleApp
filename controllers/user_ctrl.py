from models.student import Student
from models.admin import Admin
from models.prof import Prof
from models.user import User
from models.course import Course
from views.CourseView import CourseView

class UserCtrl:
    @staticmethod
    def create():
        """Permet de creer un utilisateur"""
        name = input("Nom ? ")
        email = input("Email ? ")
        password = input("Mot de passe ? ")
        role = input("Role (Etudiant/Professeur/Admin) ? ")
        
        if role.lower() == "etudiant":
            user = Student(name,email,password)
        elif role.lower() == "professeur":
            user = Prof(name,email,password)
        elif role.lower() == "admin":
            user = Admin(name,email,password)
        else:
            print("Role invalide!!!")
            return
        user.save()
        print(f"{role.capitalize()} {name} ajouté avec succès !")
        
    @staticmethod
    def connection():
        """Permet à l'utilisateur de se connecter"""
        email = input("Email ? ")
        password = input("Mot de passe ? ")
        
        user = User.findByEmail(email)
        if user and user["password"] == password:
            print(f"Bienvenue {user['name']} !")
            return user
        else:
            print("Email ou mot de passe incorrect.")
            return None