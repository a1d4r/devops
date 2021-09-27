from datetime import datetime

from app.db import VisitsStorage
from app.settings import settings


def test_add_timestamps(db: VisitsStorage):
    """Test that a timestamp can be added to storage."""

    timestamp = datetime.now()
    db.add_timestamp(timestamp)
    assert db.get_timestamps() == [timestamp.strftime(settings.datetime_format)]


def test_clear_method(db: VisitsStorage):
    """Test that clear method remove all the records."""
    assert db.get_timestamps() == []
    db.add_timestamp(datetime.now())
    db.add_timestamp(datetime.now())
    db.add_timestamp(datetime.now())
    assert db.get_timestamps() != []
    db.clear()
    assert db.get_timestamps() == []
