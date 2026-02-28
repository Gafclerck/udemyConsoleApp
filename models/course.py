from database.db import db, Query

class Course:
    def __init__(self, title, content, price, prof_email):
        self.title = title
        self.content = content
        self.price = price
        self.prof_email = prof_email
        self.enrolled_students = []
        self.quizzs = []
        self.id = Course.next_id()

    @classmethod
    def next_id(klas):
        course_table = db.table("courses")
        courses = course_table.all()
        return courses[-1]["id"] + 1 if courses else 1

    def save(self):
        """Ajouter un cours dans la base de donnees"""
        course_table = db.table("courses")
        course_table.insert({
            'id':self.id,
            'title': self.title,
            'content': self.content,
            'price': self.price,
            'prof_email': self.prof_email,
            'enrolled_students': self.enrolled_students,
            "quizzs":self.quizzs
        })

    @classmethod
    def get_all(klas):
        course_table = db.table("courses")
        courses = course_table.all()
        return [klas(i["title"], i["content"], int(i["price"]), i["prof_email"]) for i in courses]
    
    # def update(self, updated_values):
    #     course_table = db.table("courses")
    #     query = Query()
    #     course_table.update(updated_values, query.id == self.id)

    @classmethod
    def getCoursesByMail(klas, email): 
        # recuperer les cours du prof
        # instancier les cours recuperer
        pass

    def get_enrolled_students(self):
        # recuper les etudiants incrits ce cours
        # instancier les etudiant recuperer en objet etudiant
        pass
    
    def update(self, updated_values):
        # mettre a jour la liste de quizzs dans le cours
        pass


    
    
