'''Resource controller for Story events'''


class DbStoryCharacter():
	'''Resource to get story events'''
	# str event_id
	# str story_content
	# dict subsequent_events # good, bad, death, end

	def find(story_id, character_id):
		return {
			'name': 'Morpheus',
			'story_id': story_id,
			'stats': {
				'morality': 50,
				'strength': 10,
				'intelligence': 5,
				'agility': 3
			}
		}

	def update(story_id, character_id, stat_modifiers):
		character = {
			'name': 'Morpheus',
			'story_id': story_id,
			'stats': {
				'morality': 50,
				'strength': 10,
				'intelligence': 5,
				'agility': 3
			}
		}
		for stat in stat_modifiers:
			character['stats'][stat] = character['stats'][stat] + stat_modifiers[stat]

		return character

	def create(char):
		return char