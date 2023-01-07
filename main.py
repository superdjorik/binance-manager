from datetime import datetime
import uvicorn
from fastapi import FastAPI
from app.bybit import bybit_http_endpoints, bybit_websockets_endpoints
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = FastAPI()
app.include_router(bybit_http_endpoints.router)
app.include_router(bybit_websockets_endpoints.router)

# Scheduler configs and start
scheduler = AsyncIOScheduler()
scheduler.start()


# Healthcheck
@app.get("/hc", tags=["default"])
async def healthcheck():
    print(f'{str(datetime.now().isoformat())} Healthcheck ok!')
    return {"hc": "ok"}

# Healthcheck job, run every 5 minutes
job = scheduler.add_job(func=healthcheck, trigger='cron', minute='*/5')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
