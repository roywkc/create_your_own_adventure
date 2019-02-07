"""Resource controller for Story events"""

from flask_restful import reqparse, Resource
from models.db_story import DbStory

class Story(Resource):
    """Resource to get story events"""


    def get(self, story_id):
        result = DbStory.find(story_id)
        return result

