"""
Main file for Flask app.
Handles flask routing and initializes the logger.
"""
from flask import Flask
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
from controllers.stories import Stories
from controllers.story import Story
from controllers.story_event import StoryEvent
from controllers.story_character import StoryCharacter
# from controllers.user import User
# from controllers.conflict import conflict

def create_app():
	APP = Flask(__name__)
	API = Api(APP)
	# db = SQLAlchemy(APP)

	API.add_resource(Stories, "/v1/stories")
	API.add_resource(Story, "/v1/stories/<string:story_id>")
	API.add_resource(StoryCharacter, "/v1/stories/<string:story_id>/characters/<string:character_id>")
	API.add_resource(StoryEvent, "/v1/stories/<string:story_id>/characters/<string:character_id>/events/<string:event_id>")

	return APP


if __name__ == "__main__":
	APP = create_app()
	APP.run()
