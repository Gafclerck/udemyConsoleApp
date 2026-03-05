from views.AdminVew import AdminView
from models.user import User
from utils.io import Io

class AdminCtrl:
    @staticmethod
    def blockUser():
        # appeler getAll de User
        # appeler listUser de UserView(pour choisir le user à bloquer)
        # mettre a jour le user via user.update()
        users = User.getAll()
        selected_user = AdminView.listUser(users, with_select=True)
        
        if selected_user:
            print(f"\nUtilisateur sélectionné: {selected_user['name']} ({selected_user['email']})")
            
            # Déterminer l'action
            if selected_user["etat"] == 1:
                # L'utilisateur est actif, le bloquer
                if Io.yes_or_no(f"Bloquer {selected_user['name']}?") == "yes":
                    User.update(selected_user["email"], {"etat": 0})
                    print(f"{selected_user['name']} a été bloqué !")
            else:
                # L'utilisateur est bloqué, le débloquer
                if Io.yes_or_no(f"Débloquer {selected_user['name']}?") == "yes":
                    User.update(selected_user["email"], {"etat": 1})
                    print(f"{selected_user['name']} a été débloqué !")

    @staticmethod
    def showUsers():
        # appeler getAll de User (recuperation de tous les users)
        # appeler listUser de UserView(pour afficher le user)
        users = User.getAll()
        AdminView.listUser(users, with_select=False)