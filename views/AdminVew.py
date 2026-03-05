from utils.io import get_string, yes_or_no

class AdminView:
    @staticmethod
    def menu():
        # menu du admin
        # doit retourner le choix fait par l'admin (int)
        menus = [
            "Bloquer un utilisateur",
            "Afficher tous les utilisateurs",
            "Afficher les statistiques",
            "Quitter"
        ]
        for i in range(len(menus)):
            print(f"{i+1} - {menus[i]}")
        choix = int(input("Choix : "))
        if 1 <= choix <= len(menus):
            return choix
        
    @staticmethod
    def listUser(users, with_select=False):
        # afficher les users si withselect est à false
        # selectionner après affichage sinon
        if not users:
            print("Aucun utilisateur trouvé.")
            return None
        
        print("\n--- Liste des utilisateurs ---")
        for index, user in enumerate(users, 1):
            etat = "Actif" if user["etat"] == 1 else "Bloqué"
            print(f"{index}. {user['name']} ({user['email']}) - Role: {user['role']} - État: {etat}")
        
        if with_select:
            choice = int(input("\nChoix : "))
            if 1 <= choice <= len(users):
                return users[choice-1]
            return None
        print()

    
            