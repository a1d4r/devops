import pytest
from fastapi.testclient import TestClient

from app.db import VisitsStorage
from app.dependencies import get_db
from app.main import app


@pytest.fixture()
def db() -> VisitsStorage:
    return VisitsStorage('test_visits.json')


@pytest.fixture()
def client(db: VisitsStorage) -> TestClient:
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as client:
        return client
