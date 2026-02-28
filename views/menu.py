class Menu:
    @staticmethod
    def main():
        while True:
            print("\n=== Platefome de Cours en Ligne ===")
            print("1....................... Se connecter")
            print("2......................... S'inscrire")
            print("3............................ Quitter\n")
            choice = input("Faites votre choix ? ")
            if choice in ["1","2","3"]:
                return choice
            else:
                print("Choix invalide, essayez à nouveau.")