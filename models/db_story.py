"""Resource controller for Story events"""


class DbStory():
	"""Resource to get story events"""
	# str author_id;
	# list event_ids;
	# str start_event;
	# str synopsis;

	def find_all():
		return [{
			'author_id': 1,
			'event_ids': [1, 42, 666],
			'start_event': 1,
			'synopsis': "This a description of the story"
		}]

	def find(story_id):
		return {
			'author_id': 1,
			'event_ids': [1, 42, 666],
			'start_event': 1,
			'synopsis': "This a description of the story",
			'default_char_id': 1
		}
