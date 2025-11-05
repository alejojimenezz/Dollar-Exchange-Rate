from matplotlib.figure import Figure as fg
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

df = pd.read_csv('tasa_cambio.csv')

xpoints_pd = df.iloc[:]['vigenciadesde']
xpoints_dt = pd.to_datetime(xpoints_pd)
xpoints = np.flip(xpoints_dt.to_numpy())
modelx = [date.timestamp() for date in xpoints_dt][::-1]

x1 = modelx[0]
x2k = modelx[-1]

ypoints_pd = df.iloc[:]['valor']
ypoints = np.flip(ypoints_pd.to_numpy())

slope, intercept, r, p, std_err = stats.linregress(modelx, ypoints)

def linearRegression(modelx):
    return slope * modelx + intercept

lineModel = list(map(linearRegression, modelx))

polyModel = np.poly1d(np.polyfit(modelx, ypoints, 3))
polyLine = np.linspace(x1, x2k, 2000)

print(r)
print(r2_score(ypoints, polyModel(modelx)))

def get_figure():
    fig = fg(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(modelx, ypoints, label="Datos originales")
    ax.plot(modelx, lineModel, label="Regresión lineal")
    ax.plot(polyLine, polyModel(polyLine), label="Polinómica grado 3")
    ax.set_title("Tasa de cambio")
    ax.set_xlabel("Tiempo (timestamp)")
    ax.set_label("Valor")
    ax.legend()
    return fig