"""Resource controller for Story events"""

from flask_restful import reqparse, Resource
from models.db_story import DbStory

class Stories(Resource):
    """Resource to get story events"""


    def get(self):
        result = DbStory.find_all()
        return result

