from typing import Iterator

from app.db import VisitsStorage, db


def get_db() -> Iterator[VisitsStorage]:
    yield db
