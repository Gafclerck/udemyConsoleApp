from tinydb import Query
from database.db import db
class Payement:
    def __init__(self, student_email, amount):
        self.student_email = student_email
        self.amount = amount
        
    def save(self):
        """Ajouter un paiement dans la base de donnees"""
        student_table = db.table("users")
        StudentQuery = Query()
        student = student_table.get(StudentQuery.email == self.student_email)

        if student:
            # Enregistrer le paiment
            payment_table = db.table("payments")
            payment_table.insert({
                "student_email": self.student_email,
                "amount": self.amount
            })
            # Mettre a jour le solde de l'etudiant
            newAccount = student["account"] + self.amount
            student_table.update({"account":newAccount},StudentQuery.email == self.student_email)
            print(f"✅ Dépot réussi! Nouveau solde : {newAccount} Fcfa")
        else:
            print("❌ Etudiant non trouvé")