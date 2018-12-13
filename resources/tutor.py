from flask_restful import Resource, reqparse

from models.tutor import TutorModel

class TutorResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "first_name",
        type=str,
        required=True,
        help="Please enter your first name"
    )
    parser.add_argument(
        "last_name",
        type=str,
        required=True,
        help="Please enter your last name"
    )
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help="Please enter your email address"
    )
    parser.add_argument(
        "subject",
        type=str,
        required=True,
        help="Please enter your main subject"
    )

    def get(self, name):
        tutor = TutorModel.get_by_name(name)
        if tutor:
            return tutor.json()
        return {"message": "No tutor by that name"}, 404

    def post(self, name):
        if TutorModel.get_by_name(name):
            return {"message": "A tutor named {} already exists.".format(name)}, 400
        data = self.parser.parse_args()
        new_tutor = TutorModel(name, data["first_name"], data["last_name"], data["email"], data["subject"])
        try:
            new_tutor.save_to_db()
        except:
            return {"message": "A server error occured while trying to save the tutor data to the database."}, 500
        return new_tutor.json(), 201

    def put(self, name):
        data = parser.parse_args()
        tutor = TutorModel.get_by_name(name)

        if not tutor:
            tutor = TutorModel(name, data["first_name"], data["last_name"], data["email"], data["subject"])
        else:
            tutor.first_name = data["first_name"]
            tutor.last_name = data["last_name"]
            tutor.email = data["email"]
            tutor.subject = data["subject"]
        try:
            tutor.save_to_db()
        except:
            return {"message": "A server error occured while trying to update the tutor data."}, 500
        return tutor.json()

    def delete(self, name):
        tutor = TutorModel.get_by_name(name)
        if tutor:
            tutor.delete_from_db()
        return {"message": "Tutor named {} has been removed from the database."}.format(name)
