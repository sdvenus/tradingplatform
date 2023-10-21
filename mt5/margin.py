import MetaTrader5 as mt5
import pandas as pd 
# Definir la variable TIMEOUT (asegúrate de que esté definida antes de usarla)
TIMEOUT = 10000  # Este es un valor de ejemplo, puedes ajustarlo según tus necesidades

pd.set_option('display.max_columns', 500) # cuántas columnas mostramos 
pd.set_option('display.width', 1500)      # máx. anchura del recuadro para la muestra 
# mostramos los datos sobre el paquete MetaTrader5 

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


account_currency=mt5.account_info().currency
print("Account сurrency:",account_currency)
 
# creamos la lista de símbolos 
symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")
print("Symbols to check margin:", symbols)
action=mt5.ORDER_TYPE_BUY
lot=0.1
for symbol in symbols: 
    symbol_info=mt5.symbol_info(symbol) 
    if symbol_info is None: 
        print(symbol,"not found, skipped") 
        continue 
    if not symbol_info.visible: 
        print(symbol, "is not visible, trying to switch on") 
        if not mt5.symbol_select(symbol,True): 
            print("symbol_select({}}) failed, skipped",symbol) 
            continue
    ask=mt5.symbol_info_tick(symbol).ask
    margin=mt5.order_calc_margin(action,symbol,lot,ask) 
    if margin != None:
        print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency)); 
    else: 
        print("order_calc_margin failed: , error code =", mt5.last_error()) 


mt5.shutdown()