import uvicorn
from fastapi import FastAPI
from pybit import spot


app = FastAPI()
session = spot.HTTP(endpoint='https://api.bybit.com')


# Healthcheck
@app.get("/hc")
async def healthcheck():
    return {"hc": "ok"}

@app.get('/simbols')
def get_all_symbols():
    info = session.query_symbol()
    if info["ret_code"] == 0:
        symbol_counter = 0
        for i in info["result"]:
            symbol_counter += 1
        return symbol_counter, info["result"]
    else:
        return info["ret_msg"]

@app.get('/orderbook')
def get_orderbook(symbol: str = 'BTCUSDT'):
    symbol = session.orderbook(symbol=symbol)
    if symbol["ret_code"] == 0:
        return symbol["result"]
    else:
        return symbol["ret_msg"]


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)