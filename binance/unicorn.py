import django_unicorn
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
import asyncio
from binance import AsyncClient, BinanceSocketManager

def process_new_receives(stream_data, stream_buffer_name=False):
    print(str(stream_data))

ubwa = BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream('trade', ['ethbtc', 'btcusdt', 'bnbbtc', 'ethbtc'], process_stream_data=process_new_receives)

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.trade_socket('BTCBUSD')
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)
    await client.close_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    

