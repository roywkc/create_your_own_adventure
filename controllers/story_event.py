"""Resource controller for Story events"""

from flask_restful import reqparse, Resource
from models.db_story_event import DbStoryEvent
from models.db_story_character import DbStoryCharacter


class StoryEvent(Resource):
    """Resource to get story events"""


    def get(self, story_id, character_id, event_id):
        """
        Get an event for a story, with its subsequent event_ids
        @param story_id the id of a story
        @param event_id the id of the event
        @return dictionary with the story content and the subsequent events
        """
        #arg_parser = reqparse.RequestParser()
        #arg_parser.add_argument("format", type=str, default="json")
        #args = arg_parser.parse_args()
        event = DbStoryEvent.find(story_id, event_id)
        
        return event

    def patch(self, story_id, character_id, event_id, action_id):
        event = DbStoryEvent.find(story_id, event_id)

        if event.available_actions[action_id] != None:
            stat_modifier = event.available_actions[action_id][stat_modifier]
            event = DbStoryCharacter.update(story_id, character_id, stat_modifier)

        return 