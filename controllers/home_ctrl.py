from views.menu import Menu
from controllers.user_ctrl import UserCtrl
from views.ProfView import ProfView
from controllers.prof_ctrl import ProfCtrl
from views.StudentView import StudentView
from controllers.student_ctrl import StudentCtrl
from models.student import Student
from models.prof import Prof
from views.AdminVew import AdminView

class HomeCtrl:
    @staticmethod
    def main():
        while True:
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
                                choix = ProfView.menu()
                                match(choix):
                                    case 1:
                                        print("Vous aller créer un cours !")
                                        ProfCtrl.addCourse(user.email)
                                    case 2:
                                        # appeler le showCours de profCtrl
                                        pass
                                    case 3:
                                        # appeler le addQuizz de profCtrl
                                        pass
                                    case 4:
                                        # appeler le updateCours de profCtrl
                                        pass
                                    case 5:
                                        # dashboard
                                        pass

                        case "ETUDIANT":
                            user = Student(user["name"], user["email"], user["password"])
                            while True:
                                choix = StudentView.menu()
                                match(choix):
                                    case 1:
                                        StudentCtrl.acheter_credit(user)
                                    case 2:
                                        StudentCtrl.consulter_solde(user)
                                    case 3:
                                        StudentCtrl.acheter_cours(user)
                                    
                        case "ADMIN":
                            choix = AdminView.menu()
                            match(choix):
                                case 1:
                                    # appler blockUser() de adminCtrl
                                    pass
                                case 2:
                                    # appeller showUsers() de   adminCtrl  
                                    pass
                                case 3:
                                    # tableau
                                    pass                    
            elif choice == "2":
                UserCtrl.create()  
            elif choice == "3":
                print("Merci d'avoir utilisé notre plateforme. À bientôt!")
                break