from models.student import Student
from models.prof import Prof

from views.menu import Menu
from views.AdminVew import AdminView
from views.ProfView import ProfView
from views.StudentView import StudentView

from controllers.user_ctrl import UserCtrl
from controllers.prof_ctrl import ProfCtrl
from controllers.student_ctrl import StudentCtrl
from controllers.admin_ctrl import AdminCtrl

from utils.ux import Ux

class HomeCtrl:
    @staticmethod
    def main():
        while True:
            Ux.clear()
            choice = Menu.main()
            if choice == "1":
                user = UserCtrl.connection()
                if not user:
                    print("Mot de pass ou email incerrect !")
                elif user["etat"] == 0:
                    print("Hoho mon gar t'es bloqué !! sort !!")
                else:
                    match(user["role"]):
                        case "PROFESSEUR":
                            user = Prof(user["name"], user["email"], user["password"])
                            while True:
                                Ux.clear()
                                choix = ProfView.menu()
                                match(choix):
                                    case 1:
                                        print("Vous allez créer un cours !")
                                        ProfCtrl.addCourse(user.email)
                                    case 2:
                                        ProfCtrl.showCourses(user.email)
                                    case 3:
                                        ProfCtrl.addQuizz(user.email)
                                    case 4:
                                        ProfCtrl.updateCours(user.email)
                                    case 5:
                                        ProfCtrl.showEtudiantByCourse(user.email)
                                    case 6:
                                        print("Au revoir professeur !")
                                        break
                                Ux.pause()

                        case "ETUDIANT":
                            user = Student(user["name"], user["email"], user["password"])
                            while True:
                                Ux.clear()
                                choix = StudentView.menu(StudentView.main_menu)
                                match(choix):
                                    case 1:
                                        StudentCtrl.acheter_credit(user)
                                    case 2:
                                        StudentCtrl.consulter_solde(user)
                                    case 3:
                                        StudentCtrl.acheter_cours(user)
                                    case 4:
                                        StudentCtrl.lister_cours(user)
                                        while (True):
                                            Ux.clear()
                                            choix = StudentView.menu(StudentView.sub__menu)
                                            match(choix):
                                                case 1:
                                                    StudentCtrl.lire_cours(user)
                                                case 2:
                                                    StudentCtrl.passer_certification(user)
                                                case 3:
                                                    break
                                            Ux.pause()
                                        
                                    case 5:
                                        pass
                                    case 6:
                                        break
                                Ux.pause()
                        case "ADMIN":
                            while True:
                                Ux.clear()
                                choix = AdminView.menu()
                                match(choix):
                                    case 1:
                                        AdminCtrl.blockUser()
                                        # appler blockUser() de adminCtrl
                                    case 2:
                                        # appeller showUsers() de   adminCtrl  
                                        AdminCtrl.showUsers()
                                        pass
                                    case 3:
                                        # tableau
                                        pass  
                                    case 4:
                                        break   
                                Ux.pause()               
            elif choice == "2":
                UserCtrl.create()  
            elif choice == "3":
                print("Merci d'avoir utilisé notre plateforme. À bientôt!")
                break