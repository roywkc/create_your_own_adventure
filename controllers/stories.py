"""Resource controller for Story events"""

from flask_restful import reqparse, Resource, request
from models.db_story import DbStory

class Stories(Resource):
    """Resource to get story events"""


    def get(self):
        result = DbStory.find_all()
        result += [{"dummy": "steven likes watermelon"}]
        return result

    def post(self):
        return request.form