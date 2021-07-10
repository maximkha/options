# from math import max
import numpy as np
def create_call(option_price, strike_price, current_price, multiplier=100.):
    return lambda x: ((multiplier*(np.maximum((current_price*(1+x))-strike_price,0)-option_price))/(multiplier*option_price))#current_price)

def calchistdata(prices, tdiff):
    numiter = prices.shape[0] - tdiff
    pdiff = np.empty(numiter)
    for i in range(numiter):
        pdiff[i] = (prices[i + tdiff] / prices[i]) - 1
    return pdiff