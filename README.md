# Dollar-Exchange-Rate

Project using conversion from dollar to colombian pesos.

## TO-DO list

- [X] [Integrate latestUpdate and latestValue into one file.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/1)
- [X] Graph dollar exchange rate history.
- [ ] Make GUI window mockup
- [ ] Fix x ticks in graph to show dates instead of timestamps.
- [ ] Create main file with GUI.
- [ ] Convert existing files into functions to call from a main file.

## Libraries

- DateTime
- Pandas
- SodaPy
- MatPlotLib
- NumPy

```
pip install pandas
pip install sodapy
```

## Use

### Update

To update [CSV database file](tasa_cambio.csv), run [dataAPI.py](dataAPI.py)

#### Get update data

- Date from [latestUpdate.date](latestUpdate.py).
- Dollar value from [latestUpdate.value](latestUpdate.py)

### Graph

Running [graph.py](graph.py) will output graphed out data of the dollar exchange rate history, including both linear and polynomial regression lines.

`r` and `r2_score` determine the linear and polynomial relation between the data respectively. The closer the number is to 1 or -1, the more relation ther is between the data.