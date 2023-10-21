import MetaTrader5 as mt5

# Definir la variable TIMEOUT (asegúrate de que esté definida antes de usarla)
TIMEOUT = 10000  # Este es un valor de ejemplo, puedes ajustarlo según tus necesidades

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


