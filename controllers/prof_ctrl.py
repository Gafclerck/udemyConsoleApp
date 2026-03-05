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
        courses = Course.getCoursesByMail(prof_email)
        if not courses:
            print("Vous n'avez aucun cours.")
            return
        
        print("\n--- Mes cours ---")
        for course in courses:
            CourseView.afficherCours(course)

    @staticmethod
    def showEtudiantByCourse(prof_email):
        # recuperer les cours du prof via Cours.getCoursByMail()
        # selectionne un cours
        # recuperer les etudiant de ce cours via cours.get_enrolled_students()
        # affficher les etudiant via StudentVies.affciherEtudiant()
        from views.StudentView import StudentView
        
        courses = Course.getCoursesByMail(prof_email)
        if not courses:
            print("Vous n'avez aucun cours.")
            return
        
        print("\n--- Sélectionnez un cours ---")
        selected_course = CourseView.listCourse(courses, with_select=True)
        
        if selected_course:
            students = selected_course.get_enrolled_students()
            StudentView.afficherStudents(students)
    
    @staticmethod
    def addQuizz(prof_email):
        # sasi les quizz via Coursview.saisirQuizzs()
        # met ajour le cours via cours.update()
        courses = Course.getCoursesByMail(prof_email)
        if not courses:
            print("Vous n'avez aucun cours.")
            return
        
        print("\n--- Sélectionnez un cours ---")
        selected_course = CourseView.listCourse(courses, with_select=True)
        
        if selected_course:
            quizzs = CourseView.saisirQuizzs()
            selected_course.update({"quizzs": quizzs})
            print("Quizzes ajoutés avec succès !")

    @staticmethod
    def updateCours(prof_email):
        # recuperer les cours du prof via Cours.getCoursByMail()
        # selectionne un cours
        # appler le method updateCours de courView 
        # mettre ajour le cours via cours.update()
        courses = Course.getCoursesByMail(prof_email)
        if not courses:
            print("Vous n'avez aucun cours.")
            return
        
        print("\n--- Sélectionnez un cours à modifier ---")
        selected_course = CourseView.listCourse(courses, with_select=True)
        
        if selected_course:
            updated_values = CourseView.updateCours(selected_course)
            if updated_values:
                selected_course.update(updated_values)
                print("Cours mis à jour avec succès !")
            else:
                print("Aucune modification effectuée.")

    

