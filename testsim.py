import numpy as np
import pandas as pd
from simoptions import create_call, calchistdata

TICKER = "SPY"
CALL = create_call(7.64, 418, 417.96)
EXPR = 32 #days

df = pd.read_csv(TICKER.upper() + ".csv")
prices = df["Close"].values

#assume the same diff dist
diffs = calchistdata(prices, EXPR)
profits = CALL(diffs)
print(f"Mean   : {np.mean(profits)}")
print(f"STD    : {np.std(profits)}")
print(f"Median : {np.median(profits)}")
print(f"Min    : {np.min(profits)}")
print(f"Max    : {np.max(profits)}")
print(f"%in $  : {(profits>0).sum()/len(profits)}")
print(f"Sum    : {profits.sum()}")