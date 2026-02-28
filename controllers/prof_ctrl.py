from views.ProfView import ProfView
from models.course import Course
from views.CourseView import CourseView
class ProfCtrl:
    @staticmethod
    def addCourse(prof_email):
        # appelr saisirCours de CourView
        # appeller la methode save le l'objet cours
        course = CourseView.saisirCours()
        c = Course(
            course["title"],
            course["content"],
            course["price"],
            prof_email
        )
        c.save()
        print("Cours crée avec succes !")

    @staticmethod
    def showCourses(prof_email):
        # recuperer les cours du prof via Cours.getCoursByMail()
        # affficher les cours via Courviews.affciherCours()
        pass

    @staticmethod
    def showEtudiantByCourse(prof_email):
        # recuperer les cours du prof via Cours.getCoursByMail()
        # selectionne un cours
        # recuperer les etudiant de ce cours via cours.get_enrolled_students()
        # affficher les etudiant via StudentVies.affciherEtudiant()
        pass
    
    @staticmethod
    def addQuizz(prof_email):
        # sasi les quizz via Coursview.saisirQuizzs()
        # met ajour le cours via cours.update()
        pass

    @staticmethod
    def updateCours(prof_email):
        # recuperer les cours du prof via Cours.getCoursByMail()
        # selectionne un cours
        # appler le method updateCours de courView 
        # mettre ajour le cours via cours.update()
        pass

    

