import asyncio
import matplotlib.pyplot as plt
import pandas as pd
from mplfinance.original_flavor import candlestick_ohlc
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

# Listas para almacenar los datos de velas
candlestick_data = []

# Inicializa la gráfica
plt.ion()  # Habilita el modo interactivo de matplotlib
fig, ax = plt.subplots()
ax.set_xlabel('Tiempo')
ax.set_ylabel('Precio de Cierre')
ax.set_title('Gráfico de Precio de Cierre en Tiempo Real')

# Función para actualizar la gráfica
def update_plot():
    global candlestick_data

    df = pd.DataFrame(candlestick_data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')  # Convertir el timestamp a formato datetime

    ax.clear()  # Limpiar la gráfica antes de actualizar
    candlestick_ohlc(ax, df.values, width=0.0005, colorup='g', colordown='r')
    ax.xaxis_date()
    plt.xticks(rotation=45)
    plt.pause(0.01)  # Pausa para permitir que la gráfica se actualice

async def process_new_receives(msg):
    global candlestick_data

    k_data = msg['k']

    if all(key in k_data for key in ['t', 'o', 'h', 'l', 'c']):
        timestamp = k_data['t']
        open_price = k_data['o']
        high_price = k_data['h']
        low_price = k_data['l']
        close_price = k_data['c']

        candlestick_data.append((
            timestamp,
            open_price,
            high_price,
            low_price,
            close_price
        ))

        # Limitar la lista de datos para mostrar las últimas N muestras
        num_samples_to_display = 100
        candlestick_data = candlestick_data[-num_samples_to_display:]

        # Actualizar la gráfica
        update_plot()

async def main():
    try:
        # Inicializar el gestor de WebSocket de Binance
        bm = BinanceWebSocketApiManager()

        # Crear un WebSocket para el par de trading que desees (por ejemplo, BTCBUSD)
        bm.create_stream(['btcusdt@trade'], stream_buffer_name='btcusdt@trade', custom_callback=process_new_receives)

        while True:
            await asyncio.sleep(0.1)
    except Exception as e:
        print(f"Error de WebSocket: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
