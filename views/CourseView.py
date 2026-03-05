from utils.io import Io

class CourseView:
    @staticmethod
    def listCourse(courses, with_select=False):
        for index, course in enumerate(courses, 1):
            print(f"{index} - {course.title} - {course.price}")
        if with_select:
            choice = Io.get_int("Choix : ")
            if 1 <= choice <= len(courses):
                return courses[choice-1]
            
    @staticmethod
    def saisirCours(): 
        # retourne le cours saisi
        title = input("Titre du cours: ")
        content = input("Contenu du cours: ")
        price = input("Prix du cours: ")
        return {
            "title": title,
            "content": content,
            "price": price
        }

    @staticmethod
    def afficherCours(cours):
        CourseView.listCourse([cours], with_select=False)

    @staticmethod
    def saisirQuizzs():
        #cf readme
        # une questiion est un dictionnaire
        # Ex : {"type": "multiple", "question": "question?", "options": ["option1", "option2", "option3"], "reponse": "option1"}
        # Ou : {"type": "text", "question": "question?", "reponse": "reponse"}
        #retourne une liste de questions
        quizzs = []
        while True:
            print("\n--- Ajouter une question ---")
            question = Io.get_string("Question: ")
            
            # Demander le type de question
            type_question = Io.yes_or_no("Est-ce une question à choix multiple?")
            
            if type_question == "yes":
                # Question à choix multiple
                options = []
                while True:
                    option = Io.get_string(f"Option {len(options) + 1}: ")
                    options.append(option)
                    if Io.yes_or_no("Ajouter une autre option?") != "yes":
                        break
                
                reponse = Io.get_string("Réponse correcte (numéro ou texte): ")
                
                quiz = {
                    "type": "multiple",
                    "question": question,
                    "options": options,
                    "reponse": reponse
                }
            else:
                # Question à réponse à saisir
                reponse = Io.get_string("Réponse correcte: ")
                
                quiz = {
                    "type": "text",
                    "question": question,
                    "reponse": reponse
                }
            
            quizzs.append(quiz)
            
            if Io.yes_or_no("Ajouter une autre question?") != "yes":
                break
        
        return quizzs
    
    @staticmethod
    def updateCours(cours):
        # retourne un dictionnaire ayant comme clés les attributs modifiés
        # et valeurs les nouvelles valeurs
        updated_values = {}
        print(f"\nCours actuel: {cours.title}")
        
        if Io.yes_or_no("Modifier le titre?") == "yes":
            updated_values["title"] = Io.get_string("Nouveau titre: ")
        
        if Io.yes_or_no("Modifier le contenu?") == "yes":
            updated_values["content"] = Io.get_string("Nouveau contenu: ")
        
        if Io.yes_or_no("Modifier le prix?") == "yes":
            updated_values["price"] = Io.get_int("Nouveau prix: ")
        
        return updated_values