import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.debug = True
    return app.test_client()
