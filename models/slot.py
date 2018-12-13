from datetime import date, timedelta

from db import db

class SlotModel(db.Model):
    __tablename__ = "slots"

    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date)
    weekday = db.Column(db.Integer)
    timeslot = db.Column(db.Integer)

    tutor_id = db.Column(db.Integer, db.ForeignKey("tutors.id"))
    tutor = db.relationship("TutorModel")

    def __init__(self, datum, weekday, timeslot, tutor_id):
        self.datum = datum
        self.weekday = weekday
        self.timeslot = timeslot

        self.tutor_id = tutor_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "datum": self.datum.isoformat(),
            "weekday": self.weekday,
            "timeslot": self.timeslot,
            "tutor_id": self.tutor_id
            }

    @classmethod
    def get_by_date(cls, datum):
        return cls.query.filter_by(datum=datum).first()
