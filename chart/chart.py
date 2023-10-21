from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
 
# conectamos con MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
 
# solicitamos el estado y los parámetros de conexión
print(mt5.terminal_info())
# obtenemos la información sobre la versión de MetaTrader 5
print(mt5.version())
 
# solicitamos ticks de EURAUD
mt5.symbol_select("EURAUD", True)
euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime.now(), 1000, mt5.COPY_TICKS_ALL)

# solicitamos ticks de AUDUSD 
mt5.symbol_select("AUDUSD", True)
audusd_ticks = mt5.copy_ticks_from("AUDUSD", datetime.now(), 1000, mt5.COPY_TICKS_ALL)

# solicitamos ticks de EURUSD 
mt5.symbol_select("EURUSD", True)
eurusd_ticks = mt5.copy_ticks_from("EURUSD", datetime.now(), 1000, mt5.COPY_TICKS_ALL)

# solicitamos ticks de EURGBP 
mt5.symbol_select("EURGBP", True)
eurgbp_ticks = mt5.copy_ticks_from("EURGBP", datetime.now(), 1000, mt5.COPY_TICKS_ALL)
 
# obtenemos con distintos métodos las barras de diferentes instrumentos
eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime.now(), 1000)
eurgbp_rates = mt5.copy_rates_from("EURGBP", mt5.TIMEFRAME_M1, datetime.now(), 1000)
eurcad_rates = mt5.copy_rates_from("EURCAD", mt5.TIMEFRAME_M1, datetime.now(), 1000)
euraud_rates = mt5.copy_rates_from("EURCAD", mt5.TIMEFRAME_M1, datetime.now(), 1000)
audusd_rates = mt5.copy_rates_from("EURCAD", mt5.TIMEFRAME_M1, datetime.now(), 1000)

#DATA

print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)
 
print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)

print('eurusd_ticks(', len(eurusd_ticks), ')')
for val in eurusd_ticks[:10]: print(val)

print('eurgbp_ticks(', len(eurgbp_ticks), ')')
for val in eurgbp_ticks[:10]: print(val)


print('audusd_rates(', len(audusd_rates), ')')
for val in audusd_rates[:10]: print(val)

print('euraud_rates(', len(euraud_rates), ')')
for val in euraud_rates[:10]: print(val)
 
print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)
 
print('eurgbp_rates(', len(eurgbp_rates), ')')
for val in eurgbp_rates[:10]: print(val)
 
print('eurcad_rates(', len(eurcad_rates), ')')
for val in eurcad_rates[:10]: print(val)
 
#PLOT
# creamos un DataFrame de los datos obtenidos
ticks_frame = pd.DataFrame(eurgbp_ticks)
ticks_frame['time'] = ticks_frame['time'].apply(mdates.date2num)
# dibujamos los ticks en el gráfico
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
 
# mostramos los rótulos
plt.legend(loc='upper left')
 
# añadimos los encabezados
plt.title('Chart de prueba')
 
# mostramos el gráfico
plt.show()