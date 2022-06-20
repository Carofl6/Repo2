"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2.                                                                                     -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author:                                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:                                                                                         -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import ccxt
import numpy as np
import pandas as pd
import datetime as dt
import time

def downloadData(crypto : "Nombre de la criptodivisa", n : "Número de datos a leer"):
    """
    downloadData descarga información en tiempo real para la criptodivisa ingresada con la librería ccxt.
     
    """
    data = pd.DataFrame(index = range(n - 1), columns = ["Timestamp", "Bid", "Ask", "Spread", "Close"])
    bitso = ccxt.bitso()
    
    for i in range(n):
        try:
            orderBook = bitso.fetch_order_book(crypto)
            ohlc = bitso.fetch_ohlcv(crypto, timeframe = "1m", limit = 1)
            date = pd.to_datetime(dt.datetime.now())

            data.loc[i, "Timestamp"] = date
            data.loc[i, "Bid"] = orderBook["bids"][0][0]
            data.loc[i, "Ask"] = orderBook["asks"][0][0]
            data.loc[i, "Spread"] = data.loc[i, "Ask"] - data.loc[i, "Bid"]
            data.loc[i, "Close"] = ohlc[0][4]
        
        except:
            pass
        
        time.sleep(60)
    
    data.set_index(["Timestamp"], inplace = True)
    data.dropna(inplace = True)
    
    return data 

def RollSpread(data : "Información de la criptodivisa"):
    """
    RollSpread obtiene un spread teórico con el modelo teórico de Roll.
    
    """
    
    data["Delta"] = data["Close"].diff()
    data["Roll Spread"] = np.nan

    for i in range(len(data) + 1):
        if i > 10:
            X = np.stack((list(data.iloc[i - 10 : i - 5, 4].values), list(data.iloc[i - 5 : i, 4].values)), axis = 0)
            cov = np.cov(X)
            data.iloc[i - 1, 5] = 2 * (abs(cov[1, 0])) ** 0.5
        
    return data.dropna()
