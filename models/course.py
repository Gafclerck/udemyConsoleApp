from database.db import db, Query

class Course:
    def __init__(self, title, content, price, prof_email, id=None, enrolled_students = []):
        self.title = title
        self.content = content
        self.price = price
        self.prof_email = prof_email
        self.enrolled_students = enrolled_students
        self.quizzs = []
        self.id = id if id else Course.next_id()

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
        return [klas(i["title"], i["content"], int(i["price"]), i["prof_email"], i["id"], i["enrolled_students"]) for i in courses]
    
    def get_quizzs(self):
        course_table = db.table("courses")
        query = Query()
        course = course_table.get(query.id == self.id)
        return course["quizzs"]

    def update(self, updated_values):
        course_table = db.table("courses")
        query = Query()
        course_table.update(updated_values, query.id == self.id)

    @classmethod
    def getCoursesByMail(klas, email):
        # recuperer les cours du prof
        # instancier les cours recuperer
        course_table = db.table("courses")
        query = Query()
        courses = course_table.search(query.prof_email == email)
        return [klas(c["title"], c["content"], int(c["price"]), c["prof_email"], c["id"], c["enrolled_students"]) for c in courses]

    def get_enrolled_students(self):
        # recuper les etudiants incrits ce cours
        # instancier les etudiant recuperer en objet etudiant
        from models.student import Student
        users_table = db.table("users")
        query = Query()
        students = []
        for email in self.enrolled_students:
            user = users_table.get(query.email == email)
            if user:
                students.append(Student(user["name"], user["email"], user["password"]))
        return students

    
    
