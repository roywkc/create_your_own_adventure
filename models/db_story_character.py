'''Resource controller for Story events'''


class DbStoryCharacter():
	'''Resource to get story events'''
	# str event_id
	# str story_content
	# dict subsequent_events # good, bad, death, end

	def find(character_id):
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

	def update(character_id, stats):
		return {
			'name': 'Morpheus',
			'story_id': story_id,
			'stats': stats
		}

	def create(char)
		return char