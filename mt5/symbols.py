from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pytz

# Definir la variable TIMEOUT (asegúrate de que esté definida antes de usarla)
TIMEOUT = 10000  

# Inicializar MetaTrader 5
if not mt5.initialize(
    path="C:\\Program Files\\MetaTrader 5\\terminal64.exe",
    login=5017569722,
    password="",
    server="MetaQuotes-Demo",
    timeout=TIMEOUT,
    portable=False
):
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Imprimir información de la terminal y la versión
print(mt5.terminal_info())
print(mt5.version())

print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

print(mt5.version())

account = 5017569722
authorized = mt5.login(5017569722, password="Y.d.s.m03", server="MetaQuotes-Demo")
if authorized:
    print(mt5.account_info())
    print("show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print(" {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# Obtenemos todos los símbolos
symbols = mt5.symbols_get()
print('Symbols: ', len(symbols))
count = 0

# Establecemos el huso horario en UTC
timezone = pytz.timezone("Etc/UTC")

# Obtenemos la hora actual en el huso horario UTC
utc_now = datetime.now(timezone)

# Iteramos a través de todos los símbolos y obtenemos datos para cada uno
for symbol in symbols:
    # Obtenemos 10 barras de cada símbolo H4 a partir de la hora actual en el huso horario UTC
    rates = mt5.copy_rates_from(symbol.name, mt5.TIMEFRAME_H4, utc_now, 10)

    # Mostramos cada elemento de los datos obtenidos en una nueva línea
    print("\nMostramos los datos obtenidos para el símbolo {} como son".format(symbol.name))
    for rate in rates:
        print(rate)

    # Creamos un DataFrame de los datos obtenidos
    rates_frame = pd.DataFrame(rates)

    # Convertimos la hora en segundos al formato datetime
    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

    # Mostramos los datos
    print("\nMostramos el frame de datos con la información para el símbolo {}".format(symbol.name))
    print(rates_frame)

mt5.shutdown()
