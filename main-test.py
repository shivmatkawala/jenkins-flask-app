import pytest
from main import app
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_template_data(client):
    response = client.get('/')
    html = response.data.decode()

    # Check for feature titles
    assert "Personalized Learning" in html
    assert "World-class Mentors" in html
    assert "Hands-on Projects" in html

    # Check for metrics
    assert "1M+" in html
    assert "2K+" in html
    assert "150+" in html

    # Check for current year
    current_year = str(datetime.now().year)
    assert current_year in html
