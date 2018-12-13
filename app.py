from flask import Flask
from flask_restful import Api

from resources.tutor import TutorResource
from resources.slot import SlotResource, SlotList, SlotTest

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "1234"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(TutorResource, "/tutors/<string:name>")
api.add_resource(SlotResource, "/slots/<string:daytime>")
api.add_resource(SlotList, "/slots")
api.add_resource(SlotTest, "/test")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
