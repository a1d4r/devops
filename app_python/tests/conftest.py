from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.db import VisitsStorage
from app.dependencies import get_db
from app.main import app


@pytest.fixture()
def db() -> VisitsStorage:
    storage = VisitsStorage(Path('test_visits.json'))
    storage.clear()
    return storage


@pytest.fixture()
def client(db: VisitsStorage) -> TestClient:
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as client:
        return client
