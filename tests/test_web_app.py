from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.testclient import TestClient
from freezegun import freeze_time

from app_python.main import app

client = TestClient(app)


@freeze_time('2012-01-14 10:21:34')
def test_current_time():
    response = client.get('/')
    assert response.status_code == 200
    current_time = datetime.now(ZoneInfo('Europe/Moscow')).time()
    assert datetime.strptime(response.text, '%H:%M:%S').time() == current_time
