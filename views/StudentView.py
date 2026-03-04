class StudentView:
    @staticmethod
    def menu():
        menus = [
            "Acheter de credit",
            "Consulter solde",
            "Acheter un cours", 
            "lister mes cours",
            "Lister mes certificats", 
            "Quitter"
        ]
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
        pass

    @staticmethod
    def afficherStudents(students):
        #afficher les etudiants
        pass     
   




        
    
        