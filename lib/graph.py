import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

df = pd.read_csv('updateHistory.csv')

xpoints_pd = df.iloc[:]['vigenciadesde']
xpoints_dt = pd.to_datetime(xpoints_pd)
xpoints = np.flip(xpoints_dt.to_numpy())
modelx = [date.timestamp() for date in xpoints_dt][::-1]

ypoints_pd = df.iloc[:]['valor']
ypoints = np.flip(ypoints_pd.to_numpy())

N = 1500  # Max 2000
modelx = modelx[-N:]
ypoints = ypoints[-N:]

x1 = modelx[0]
x2k = modelx[-1]

slope, intercept, r, p, std_err = stats.linregress(modelx, ypoints)

def linearRegression(modelx):
    return slope * modelx + intercept

lineModel = list(map(linearRegression, modelx))

polyModel = np.poly1d(np.polyfit(modelx, ypoints, 3))
polyLine = np.linspace(x1, x2k, N)

print(r)
print(r2_score(ypoints, polyModel(modelx)))
print(lineModel[-1])
print(polyModel(polyLine[-1]))

plt.plot(modelx, ypoints)
plt.plot(modelx, lineModel)
plt.plot(polyLine, polyModel(polyLine))
plt.show()