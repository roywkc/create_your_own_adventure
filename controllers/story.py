"""Resource controller for Story events"""

from flask_restful import reqparse, Resource, request
from models.db_story import DbStory

class Story(Resource):
    """Resource to get story events"""


    def get(self, story_id):
        result = DbStory.find(story_id)
        return result

    def put(self, story_id):
        story = DbStory.find(story_id)

        story['summary'] = request.form['summary']

        return story