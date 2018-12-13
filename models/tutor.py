from db import db

class TutorModel(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    #unique full name
    name = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    subject = db.Column(db.String(32))

    def __init__(self, name, first_name, last_name, email, subject):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.subject = subject

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            "name": self.name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "subject": self.subject
        }

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
