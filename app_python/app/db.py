import json
from datetime import datetime

from app.settings import settings


class VisitsStorage:
    """Persistent storage for visits."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.clear()

    def clear(self) -> None:
        """Clear the storage."""
        with open(self.filename, 'w') as f:
            json.dump([], f, default=str)

    def get_timestamps(self) -> list[str]:
        """Get all timestamps from storage."""
        with open(self.filename) as f:
            return json.load(f)  # type: ignore

    def add_timestamp(self, timestamp: datetime) -> None:
        """Add timestamp to storage"""
        timestamps = self.get_timestamps()
        timestamps.append(timestamp.strftime(settings.datetime_format))
        with open(self.filename, 'w') as f:
            json.dump(timestamps, f)


db = VisitsStorage('visits.json')