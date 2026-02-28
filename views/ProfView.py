
class ProfView:
    @staticmethod
    def menu():
        menus = ["Ajouter un cours", "modifier un cours", "Supprimer un cours", "Quitter"]
        for i in range(len(menus)):
            print(f"{i+1} - {menus[i]}")
        choix = int(input("Choix : "))
        if 1 <= choix <= len(menus):
            return choix