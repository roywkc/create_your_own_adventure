import pytest
from controllers.story import Story

class TestStory:
    def test_get(self, client):
        response = client.get('/story/1')
        assert response == {
          'author_id':1,
          'event_ids': [1],
          'start_event': 1,
          'synopsis': "This a description of the story!"
        }
