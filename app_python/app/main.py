from datetime import datetime

from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator

from app.db import VisitsStorage
from app.dependencies import get_db
from app.settings import settings

app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get('/', response_class=PlainTextResponse)
async def current_time(db: VisitsStorage = Depends(get_db)) -> str:
    """Return current time in Moscow."""
    local_dt = datetime.now(settings.timezone)
    db.add_timestamp(local_dt)
    return local_dt.time().strftime(settings.datetime_format)


@app.get('/visits', response_class=JSONResponse)
async def get_visits(db: VisitsStorage = Depends(get_db)) -> list[str]:
    """Return visits for root path."""
    return db.get_timestamps()
