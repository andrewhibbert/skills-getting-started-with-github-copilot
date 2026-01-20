"""
Pytest configuration and fixtures
"""
import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original state
    original_activities = {
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
        "Soccer Team": {
            "description": "Join the varsity soccer team for practices and matches",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["james@mergington.edu", "lily@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Competitive swimming training and meets",
            "schedule": "Tuesdays and Thursdays, 6:00 AM - 7:30 AM",
            "max_participants": 15,
            "participants": ["sarah@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and mixed media art",
            "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
            "max_participants": 18,
            "participants": ["emily@mergington.edu", "alex@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting, theater production, and performing arts",
            "schedule": "Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 22,
            "participants": ["isabella@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop argumentation skills and compete in debates",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["ryan@mergington.edu", "ava@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Compete in science and engineering challenges",
            "schedule": "Mondays, 3:30 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["ethan@mergington.edu", "mia@mergington.edu"]
        }
    }
    
    # Reset before test
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Reset after test
    activities.clear()
    activities.update(original_activities)
