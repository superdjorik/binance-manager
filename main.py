import uvicorn
from fastapi import FastAPI
from app.bybit import bybit_http_endpoints, bybit_websockets_endpoints

app = FastAPI()


app.include_router(bybit_http_endpoints.router)
# app.include_router(bybit_websockets_endpoints.router)


# Healthcheck
@app.get("/hc", tags=["default"])
async def healthcheck():
    return {"hc": "ok"}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
