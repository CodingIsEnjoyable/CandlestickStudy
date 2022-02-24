# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:18:27 2022

@author: data2wealth
"""

import talib
import quandl

# Download daily data
data = quandl.get("WIKI/NVDA")
print(data)
print(data.columns)

# Make a copy and customize 
df = data.copy()
df.drop(axis=1, columns=['Open', 'High','Low','Close','Volume', 'Ex-Dividend','Split Ratio'], inplace=True)
df.rename(columns={"Adj. Open":"open", "Adj. High":"high", "Adj. Low":"low", "Adj. Close":"close", "Adj. Volume":"volume"},inplace=True)
print(df)

# Calculating candlestick patterns
ms = talib.CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'])
egf = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
hammer = talib.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
hm = talib.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])

# Display result
print("Total trading days: {}".format(df["open"].count()))
print("Morning Star appeared: {} times".format(ms[ms!=0].count()))
print("Engulfing Pattern appeared: {} times".format(egf[egf!=0].count()))
print("Hammer appeared: {} times".format(hammer[hammer!=0].count()))
print("Hanging Man appeared: {} times".format(hm[hm!=0].count()))                      

# Pass the result to copied dataframe
df['morning_star'] = ms
df['engulfing'] = egf
df['hammer'] = hammer
df['hanging_man'] = hm
print(df)                 
print(df.columns)
