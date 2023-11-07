#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


def on_close(_):
    print("CLOSED")


my_client = SpotWebsocketStreamClient(
    on_message=message_handler,
    on_close=on_close,
    is_combined=True,
    timeout=None
)


# subscribe btcusdt 1m kline
my_client.kline(symbol="btcusdt", interval="1m")

time.sleep(5)

# subscribe ethusdt 3m kline
my_client.kline(symbol="ethusdt", interval="3m")

time.sleep(10)

# unsubscribe btcusdt 1m kline
my_client.kline(
    symbol="btcusdt", interval="1m", action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE
)

time.sleep(5)

logging.debug("closing ws connection")
my_client.stop()

time.sleep(20)
