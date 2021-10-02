import json
from datetime import datetime
from pathlib import Path

from app.settings import settings


class VisitsStorage:
    """Persistent storage for visits."""

    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath

    def clear(self) -> None:
        """Clear the storage."""
        self.filepath.parent.mkdir(exist_ok=True, parents=True)
        with self.filepath.open('w') as f:
            json.dump([], f)

    def get_timestamps(self) -> list[str]:
        """Get all timestamps from storage."""
        try:
            with self.filepath.open('r') as f:
                return json.load(f)  # type: ignore
        except FileNotFoundError:
            self.clear()
            return []

    def add_timestamp(self, timestamp: datetime) -> None:
        """Add timestamp to storage"""
        timestamps = self.get_timestamps()
        timestamps.append(timestamp.strftime(settings.datetime_format))
        with self.filepath.open('w') as f:
            json.dump(timestamps, f)


db = VisitsStorage(settings.filepath)
