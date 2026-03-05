from utils.io import get_int, get_string
class StudentView:
    main_menu = [
        "Acheter de credit",
        "Consulter solde",
        "Acheter un cours", 
        "lister mes cours",
        "Lister mes certificats", 
        "Quitter"
    ]
    sub__menu = [
        "lire un cours",
        "passer une certification",
        "Quitter"
    ]
    @staticmethod
    def menu(menus):
        for i in range(len(menus)):
            print(f"{i+1} - {menus[i]}")
        choix = int(input("Choix : "))
        if 1 <= choix <= len(menus):
            return choix
    
    @staticmethod
    def saisi_amount():
        amount = int(input("Montant: "))
        return amount 

    @staticmethod
    def afficher_account(account):
        print(f"Votre solde actuelle est de {account} fcfa")

    @staticmethod
    def details_cours(course):
        print(f"Titre : {course.title}")
        print(f"Content : {course.content}")

    @staticmethod
    def afficherStudents(students):
        #afficher les etudiants
        if not students:
            print("Aucun étudiant inscrit à ce cours.")
            return
        
        print("\n--- Liste des étudiants ---")
        for idx, student in enumerate(students, 1):
            print(f"{idx}. {student.name} ({student.email})")
        print()     

    @staticmethod
    def passer_test(course):
        score = 0
        questions = course.get_quizzs()
        if questions:
            for qst in questions:
                print(f"Question :  {qst.get("question")}")
                if qst["type"] == "multiple":
                    for index, option in enumerate(qst["options"], 1):
                        print(f"{index} - {option}")
                    choix = get_int("Reponse : ")
                    reponse = qst["options"][choix] 
                else:
                    reponse = get_string("Reponse : ")
                if reponse == qst["reponse"]: score += 1
        else :
            print("Il n'y a pas encore de test de certification pour ce cours !")
        
    @staticmethod
    def passer_test(course):
        score = 0
        questions = course.get_quizzs()
        if questions:
            for qst in questions:
                print(f"Question : {qst.get('question')}")
                if qst["type"] == "multiple":
                    for index, option in enumerate(qst["options"], 1):
                        print(f"{index} - {option}")
                    choix = get_int("Reponse : ")
                    reponse = qst["options"][choix-1]  # Correction index
                else:
                    reponse = get_string("Reponse : ")
                if reponse == qst["reponse"]: 
                    score += 1
            
            percentage = (score / len(questions)) * 100
            print(f"\n Test terminé ! Score: {score}/{len(questions)} ({percentage}%)")
            return percentage
        else:
            print("Il n'y a pas encore de test de certification pour ce cours !")
            return 0
   




        
    
        