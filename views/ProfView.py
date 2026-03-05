from utils.io import Io

class ProfView:
    @staticmethod
    def menu():
        menus = [
            "Ajouter un cours",
            "Afficher mes cours",
            "Ajouter des quizzes",
            "Modifier un cours",
            "Voir les étudiants d'un cours",
            "Quitter"
        ]
        for i in range(len(menus)):
            print(f"{i+1} - {menus[i]}")
        choix = Io.get_int("Choix : ")
        if 1 <= choix <= len(menus):
            return choix