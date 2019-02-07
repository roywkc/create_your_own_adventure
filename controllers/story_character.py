"""Resource controller for Story events"""

from flask_restful import reqparse, Resource

class StoryCharacter(Resource):
	"""Resource to get story events"""

	def get(self, story_id, character_id):
		# result = DbCharacter.find(character_id)
		return {
			"character_id": 2,
			"name": "Morpheus",
			"story_id": story_id,
			"stats": {
				"morality": 50,
				"strength": 10,
				"intelligence": 5,
				"agility": 3
			}
		}

	