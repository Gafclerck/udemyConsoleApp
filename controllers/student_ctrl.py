from models.payement import Payement
from models.course import Course
from views.StudentView import StudentView
from views.ProfView import ProfView
from views.CourseView import CourseView

class StudentCtrl:
    @staticmethod
    def acheter_credit(student):
        montant = StudentView.acheter_credit()
        payement = Payement(student.email, montant)
        payement.save()

    @staticmethod
    def consulter_solde(student):
        # apller le getter de amount
        # appeler le view pour l'afficher
        pass
   
    @staticmethod
    def acheter_cours(student):
        pass
        # valider l'achat
        # ajouter le cours au cours de l'etudiant
        # ajouter l'etudiant a la liste de etudiant inscrits a ce cours 
        # course = CourseView.listCourse(Course.get_all(), with_select=True)
        # if student and course:
        #     if student.get_account() >= course.price and yes_or_no("Confirmer l'abonnement a ce cours") == "yes":
        #         student.update({
        #             "account" : student.get_account() - course.price,
        #             "courses" : student.get_courses() + [course]
        #         })
        #         student.update({"account" : student.get_account() - course.price}) 
        #         course.enrolled_students.append(student.email)
        #         course.update({"enrolled_students":course.enrolled_students})
        #     else:
        #         print("Votre solde est insuffisant pour effectué ce abonnement !")

    def passer_certification():
        pass
