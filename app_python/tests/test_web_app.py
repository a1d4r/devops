from datetime import datetime

import time_machine
from fastapi.testclient import TestClient

from app.settings import settings

fixed_datetime = datetime(2010, 10, 26, 1, 24, tzinfo=settings.timezone)


@time_machine.travel(fixed_datetime)
def test_current_time(client: TestClient):
    """Test that app returns current moscow time in specified format."""
    response = client.get('/')
    assert response.status_code == 200
    assert fixed_datetime.strftime(settings.datetime_format) == response.text


def test_visits(client: TestClient):
    """Test that visits are tracked correctly."""
    timestamps = [
        datetime(2010, 10, 10, 10, 10, tzinfo=settings.timezone),
        datetime(2011, 11, 11, 11, 11, tzinfo=settings.timezone),
        datetime(2012, 12, 12, 12, 12, tzinfo=settings.timezone),
    ]
    for timestamp in timestamps:
        with time_machine.travel(timestamp):
            response = client.get('/')
            assert response.status_code == 200
    response = client.get('/visits')
    expected = [
        timestamp.strftime(settings.datetime_format) for timestamp in timestamps
    ]
    assert response.json() == expected
