import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def r(x, y):
    temp_1 = ((x-x.mean())*(y-y.mean())).sum()
    temp_2 = np.sqrt(((x-x.mean())**2).sum()*((y-y.mean())**2).sum())
    return temp_1/temp_2

def t(n, r):
    return np.sqrt(n-2)*r/np.sqrt(1-r**2)

def z_i(r, n, zn, u):
    return 0.5*np.log(((1+r)/(1-r)))+zn*(u/(np.sqrt(n-3)))


data = pd.read_csv("data_u.csv")
data = data[::-1]
data.reset_index(drop=True, inplace=True)
temp = data[900:1000]
y = temp['temp']
R = []
x1 = temp['P']
x2 = temp['Pa']
x3 = temp['hum']
x4 = temp['wind']

R.append(r(y, x1))
R.append(r(y, x2))
R.append(r(y, x3))
R.append(r(y, x4))
print("Выборочные коэф корреляции")
print(R)
z_u=[]
z_d=[]
u = 1.96  # a = 0.95
for i in R:
    z_u.append(z_i(i, len(temp), 1, u))
    z_d.append(z_i(i, len(temp), -1, u))
print("Доверительные интервалы")
print(z_u)
print(z_d)