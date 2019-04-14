"""Resource controller for Story events"""


class DbStoryEvent():
	"""Resource to get story events"""
	# str event_id
	# str story_content
	# dict subsequent_events # good, bad, death, end

	def find(story_id, event_id):
		result = {}
		if event_id == "42":
			result = {
				"event_id": 42,
				"story_content": "YOU HAVE DIED",
				"available_actions": None
			}
		elif event_id == "666":
			result = {
				"event_id": 666,
				"story_content": "The End",
				"available_actions": None
			}
		else:
			result = {
				"event_id": event_id,
				"story_content": "This is a story snippet, authors will write their pages here.",
				"available_actions": {
					'1': {
						"action": "Say Hello",
						"next_event": 2,
						"stat_modifier": {
							"morality": 1
						},
					},
					'2': {
						"action": "Ignore",
						"next_event": 2,
						"stat_modifier": {
							"morality": -1
						}
					}
				}
			}
		return result
