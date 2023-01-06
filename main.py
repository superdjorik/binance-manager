import uvicorn
from fastapi import FastAPI
from app import bybit_endpoints

app = FastAPI()


app.include_router(bybit_endpoints.router)


# Healthcheck
@app.get("/hc", tags=["default"])
async def healthcheck():
    return {"hc": "ok"}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)