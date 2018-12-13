from flask_restful import Resource, reqparse
from datetime import date, timedelta

from models.slot import SlotModel

class SlotResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "tutor_id",
        type=int,
        required=True,
        help="Missing tutor id."
    )
    parser.add_argument(
        "number_of_dates",
        type=int,
        required=True,
        help="Missing number of dates."
    )

    def post(self, daytime):
        weekday, timeslot = [int(x) for x in daytime.split("-")]
        data = self.parser.parse_args()

        first_date = date.today()
        for i in range(0, 7):
            first_date = date.today() + timedelta(days=i)
            if first_date.weekday() == weekday:
                break
        print(first_date.isoformat())

        #generate and insert n slot objects
        for i in range(0, data["number_of_dates"]):
            datum = first_date + timedelta(weeks = i)
            slot = SlotModel(datum, weekday, timeslot, data["tutor_id"])
            try:
                slot.save_to_db()
            except:
                return {"message": "An internal error occured while creating slot on {}.".format(datum.isoformat())}, 500

        return {"message": "Created slots on {} at {}:00 for the next {} weeks.".format(
            datum.strftime("%A"), str(timeslot), str(data["number_of_dates"])
        )}, 201

        #need to prevent double slots


class SlotList(Resource):
    def get(self):
        return {"slots": [slot.json() for slot in SlotModel.query.all()]}

class SlotTest(Resource):
    def post(self):
        slot = SlotModel(date.today(), 3, 14, 1)
        slot.save_to_db()
        return slot.json()
