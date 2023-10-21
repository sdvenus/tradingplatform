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


print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

if not mt5.initialize() :
    print("initialize() failed, error code =", mt5.last_error())
    quit()

print(mt5.version())


account= 5017569722
authorized = mt5.login(5017569722, password = "Y.d.s.m03", server="MetaQuotes-Demo")
if authorized:
    print(mt5.account_info())
    print("show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print(" {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

mt5.shutdown()
    
