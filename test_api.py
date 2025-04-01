import re
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_current_time():
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert "current_time" in data
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", data["current_time"])