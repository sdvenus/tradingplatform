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


  
# mostramos la información sobre las órdenes activas en el símbolo GBPUSD 
orders=mt5.orders_get(symbol="GBPUSD") 
if orders is None: 
    print("No orders on GBPUSD, error code={}".format(mt5.last_error())) 
else: 
    print("Total orders on GBPUSD:",len(orders))
    # mostramos todas las órdenes activas 
    for order in orders: 
        print(order) 
print() 
  
# obtenemos la lista de órdenes en los símbolos cuyos nombres contienen "*GBP*" 
gbp_orders=mt5.orders_get(group="*GBP*") 
if gbp_orders is None: 
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error())) 
else: 
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders))) 
    # mostramos estas órdenes en forma de recuadro con la ayuda de pandas.DataFrame 
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys()) 
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True) 
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s') 
    print(df) 
  
# finalizamos la conexión con el terminal MetaTrader 5 
mt5.shutdown() 