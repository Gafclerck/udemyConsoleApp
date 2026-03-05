from models.payement import Payement
from models.course import Course
from views.StudentView import StudentView
from views.CourseView import CourseView
from utils.io import yes_or_no

class StudentCtrl:
    @staticmethod
    def acheter_credit(student):
        montant = StudentView.saisi_amount()
        payement = Payement(student.email, montant)
        payement.save()

    @staticmethod
    def consulter_solde(student):
        # apller le getter de amount
        # appeler le view pour l'afficher
        print(f"Votre solde actuel est de {student.get_account()} fcfa")
   
    @staticmethod
    def acheter_cours(student):
        pass
        # valider l'achat
        # ajouter le cours au cours de l'etudiant
        # ajouter l'etudiant a la liste de etudiant inscrits a ce cours 

        course = CourseView.listCourse(Course.get_all(), with_select=True)
        if course:
            if student.get_account() >= course.price and yes_or_no("Confirmer l'abonnement à ce cours") == "yes":
                student.update({"account" : student.get_account() - course.price})
                enrolled = course.enrolled_students
                enrolled.append(student.email)
                print(course.id)
                course.update({"enrolled_students":enrolled})
            else:
                print("Votre solde est insuffisant pour effectué ce abonnement !")

    def lister_cours(student):
        CourseView.listCourse(student.get_courses())

    def lire_cours(student):
        course = CourseView.listCourse(student.get_courses(), with_select=True)
        StudentView.details_cours(course)

    def passer_certification(student):
        course = CourseView.listCourse(student.get_courses(), with_select=True)
        StudentView.passer_test(course)