"""Pytest fixtures for testing the Mergington High School API"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


# Store the initial activities data for resetting between tests
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball team and practice sessions",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn and practice tennis skills",
        "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["sarah@mergington.edu", "alex@mergington.edu"]
    },
    "Drama Club": {
        "description": "Explore theater, acting, and stage performance",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["jessica@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, sculpture and visual arts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["maya@mergington.edu", "david@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop argumentation and public speaking skills",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["ryan@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu", "grace@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state after each test"""
    # Reset before test
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)
    
    yield
    
    # Reset after test
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)
