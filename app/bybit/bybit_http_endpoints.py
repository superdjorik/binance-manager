from fastapi import APIRouter
from pybit import spot


router = APIRouter()
session = spot.HTTP(endpoint='https://api.bybit.com')


@router.get('/http/simbols', tags=['http'])
async def get_all_symbols():
    info = session.query_symbol()
    if info["ret_code"] == 0:
        return info["result"]
    else:
        return info["ret_msg"]


@router.get('/http/count_simbols', tags=['http'])
async def count_symbols_at_stock():
    info = session.query_symbol()
    if info["ret_code"] == 0:
        symbol_counter = 0
        for i in info["result"]:
            symbol_counter += 1
        return symbol_counter
    else:
        return info["ret_msg"]


@router.get('/http/orderbook', tags=['http'])
async def get_orderbook(symbol: str = 'BTCUSDT'):
    try:
        symbol = session.orderbook(symbol=symbol)
        if symbol["ret_code"] == 0:
            return symbol["result"]
        else:
            return symbol
    except Exception as e:
        return e.message


@router.get('/http/public_trading_records', tags=['http'])
async def public_trading_records(symbol: str = 'BTCUSDT'):
    try:
        symbol = session.public_trading_records(symbol=symbol)
        if symbol["ret_code"] == 0:
            return symbol["result"]
        else:
            return symbol
    except Exception as e:
        return e.message


