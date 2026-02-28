from views.ProfView import ProfView
from models.course import Course
from views.CourseView import CourseView

class AdminCtrl:
    @staticmethod
    def blockUser():
        # appeler getAll de User
        # appeler listUser de UserView(pour choisir le user à bloquer)
        # mettre a jour le user via user.update()
        pass

    @staticmethod
    def showUsers():
        # appeler getAll de User (recuperation de tous les users)
        # appeler listUser de UserView(pour afficher le user)
        pass