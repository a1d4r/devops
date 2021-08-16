from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def current_time() -> str:
    """Return current time in Moscow."""
    local_dt = datetime.now(ZoneInfo('Europe/Moscow'))
    return local_dt.time().strftime('%H:%M:%S')
