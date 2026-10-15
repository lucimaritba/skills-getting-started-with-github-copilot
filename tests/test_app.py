from urllib.parse import quote


def test_root_redirects_to_static_page(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_current_activities(client, activity_data):
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.json() == activity_data


def test_signup_adds_participant(client):
    email = "new@mergington.edu"
    response = client.post("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}
    assert email in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "existing@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_returns_404_for_unknown_activity(client):
    response = client.post(
        "/activities/Unknown Club/signup",
        params={"email": "new@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_updates_activity(client):
    activity = quote("Chess Club", safe="")
    email = quote("existing@mergington.edu", safe="")
    response = client.delete(f"/activities/{activity}/participants/{email}")

    assert response.status_code == 200
    assert response.json() == {"message": "Removed existing@mergington.edu from Chess Club"}
    assert "existing@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]


def test_remove_participant_returns_404_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown Club/participants/student%40mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_returns_404_when_not_registered(client):
    activity = quote("Chess Club", safe="")
    email = quote("missing@mergington.edu", safe="")
    response = client.delete(f"/activities/{activity}/participants/{email}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
