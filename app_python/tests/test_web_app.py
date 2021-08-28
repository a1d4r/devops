from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.testclient import TestClient
from freezegun import freeze_time

from app.main import app

client = TestClient(app)


@freeze_time()
def test_current_time():
    response = client.get('/')
    assert response.status_code == 200
    current_time = datetime.now(ZoneInfo('Europe/Moscow')).time()
    assert current_time.strftime('%H:%M:%S') in response.text
