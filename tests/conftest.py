import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def activity_data():
    return {
        "Chess Club": {
            "description": "Learn chess strategies",
            "schedule": "Fridays, 3:30 PM",
            "max_participants": 12,
            "participants": ["existing@mergington.edu"],
        },
        "Art Club": {
            "description": "Explore visual arts",
            "schedule": "Wednesdays, 3:30 PM",
            "max_participants": 15,
            "participants": [],
        },
    }


@pytest.fixture
def client(monkeypatch, activity_data):
    monkeypatch.setattr(app_module, "activities", activity_data)
    with TestClient(app_module.app) as test_client:
        yield test_client
