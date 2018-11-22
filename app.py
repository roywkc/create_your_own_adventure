"""
Main file for Flask app.
Handles flask routing and initializes the logger.
"""
from flask import Flask
from flask_restful import Api
from controllers.story_event import StoryEvent

APP = Flask(__name__)
API = Api(APP)

# Route Handling
API.add_resource(StoryEvent, "/v1/story/<string:story_id>/event/<string:event_id>")

if __name__ == "__main__":

    APP.run()
