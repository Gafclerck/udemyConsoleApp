class CourseView:
    @staticmethod
    def listCourse(courses, with_select=False):
        for index, course in enumerate(courses, 1):
            print(f"{index} - {course.title} - {course.price}")
        if with_select:
            choice = int(input("Choix : "))
            if 1 <= choice <= len(courses):
                return courses[choice-1]
            
    @staticmethod
    def saisirCours(): 
        # retourne le cours saisi
        pass

    @staticmethod
    def afficherCours(cours):
        pass

    @staticmethod
    def sasirQuizzs():
        #cf readme
        # une questiion est un dictionnaire
        # Ex : {"question": "question?", "options": ["option1", "option2", "option3"], "reponse ": "option1"}
        #retourne une liste de questions
        pass
    
    @staticmethod
    def updateCours(cours):
        # retourne un dictionnaire ayant comme clés les attributs modifiés
        # et valeurs les nouvelles valeurs
        pass