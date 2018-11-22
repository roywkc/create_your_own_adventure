"""Resource controller for Story events"""

from flask_restful import reqparse, Resource


class StoryEvent(Resource):
    """Resource to get story events"""


    def get(self, story_id, event_id):
        """
        Get an event for a story, with its subsequent event_ids
        @param story_id the id of a story
        @param event_id the id of the event
        @return dictionary with the story content and the subsequent events
        """
        #arg_parser = reqparse.RequestParser()
        #arg_parser.add_argument("format", type=str, default="json")
        #args = arg_parser.parse_args()
        return {
          "event_id": 1,
          "story_content": "This is a story snippet, authors will write their pages here.",
          "subsequent_events": {
            #resolution now is based on character morality
            "good": 2,
            "bad": 3,
            "death": 42,
            "end": 666
          }
        }
