## Fonctionnalités

### Étudiant

- Ajouter de l'argent à son compte
  - saisir la somme à ajouter
  - ajouter somme à account de l'etudiant
  - enregistre l'ajout
- Consulter le solde
  - recuperer le account de l'etudiant
  - afficher le account
- Acheter un cours
  - selectionnercours() -> Cours (listeCours(cours , True))
  - validerAchat() --> crtl
  - mettre a jour le compte de l'etudiant
  - ajouter l'etudiant au tableau des inscrits du cours
- Lister mes cours
  - recuperer les cours auxquelles l'etudiant s'est inscrit
  - afficher ces cours
  * Lire un cours
    - choisir un cours
    - afficher le content
  * Passer une évaluation (quizz /test)
    - choisir le cours
    - boucler sur la liste des quizz pour qu'il reponde atoutes questions
    - verifier s'il a valider ou pas
    - si oui generer certificat sinon recommencer
- Lister mes certificats
  - recuperer ces certificats
  - afficher ces certificats

### Professeur

- Créer un cours
  - sasirCours(): Cours (CourView)
  - addCours() (Cours)
- Lister ses cours
  - recuperer les cours du prof connecté
  - afficher ces cours
- Lister les étudiants par cours
  - recuperer les cours du profs
  - choisir un cours
  - recuper la liste des etudiant inscrits a ce cours // GETTER
  - afficher ces etudiants
- Ajouter un quiz à un cours
  - saisir la question (type, question, propositions, reponse)
  - ajouter le quiz au cours
- Éditer un cours
  - selectionner le cours à modifer
  - saisir les infos à modidier
  - mettre à le cours
- Tableau de bord
  - resume de tout

### Administrateur

- Bloquer un utilisateur
  - recuperer tous les users
  - choisir un user
  - mettre à jour le user avec un etat 0
- Lister les utilisateurs
  - recuperer tous les users
  - afficher les users
- Tableau de bord

## ce qu j'ai ajouter

- j'ai ajouter utils et jel'ai utiliser dans student_ctrl our les questions de oui ou non

## Architecture

```
├── controllers/     # Contrôleurs (logique métier)
├── models/         # Modèles de données
├── views/          # Vues et interfaces
├── database/       # Gestion de la base de données
├── utils/          # Utilitaires
└── main.py         # Point d'entrée
```
