from fastapi import APIRouter
import secr
from pybit import inverse_perpetual
from pybit import spot


api_key = secr.api_key
api_secret = secr.api_secret

ws_inverse = inverse_perpetual.WebSocket(
    api_key=api_key,
    api_secret=api_secret,
    test=True
)


router = APIRouter()


@router.get('/ws/handle_orderbook', tags=['websocket'])
def handle_orderbook(message):
    # I will be called every time there is new orderbook data!
    print(message["data"])
    orderbook_data = message["data"]

# ws_inverse.orderbook_25_stream(handle_orderbook, "BTCUSD")
