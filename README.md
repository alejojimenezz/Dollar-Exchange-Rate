# Dollar-Exchange-Rate

Project using conversion from dollar to colombian pesos.

- [Dollar-Exchange-Rate](#dollar-exchange-rate)
  - [TO-DO list](#to-do-list)
  - [Libraries](#libraries)
  - [Files](#files)
  - [Use](#use)
    - [Update](#update)
      - [Get update data](#get-update-data)
    - [Graph](#graph)


## TO-DO list

- [X] [Integrate latestUpdate and latestValue into one file.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/1)
- [X] Graph dollar exchange rate history.
- [X] Update database with ALL historic values.
- [ ] [Fix x ticks in graph to show dates instead of timestamps.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/2)
- [ ] Create main file with GUI.
- [ ] Convert existing files into functions to call from a main file.
- [X] Use last points in regression models to predict next dollar value.
- [ ] Test PyQT for GUI.
- [X] [Fix update button to execute only when pushed.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/3)
- [ ] Implement Main file.

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

## Files

- [formatCSV.py](formatCSV.py): Used once. Formats [downloaded historic database](historic.csv) to match previous database from API. Not necessary to run again.
- [updateFunction.py](updateFunction.py): Updates [API database](DB_fromAPI.csv) (latest 2000 values).
- [updateExchangeHistory.py](updateExchangeHistory.py): Updates full [historic database](updateHistory.csv).
- [latestUpdate.py](latestUpdate.py): Returns relevant data from database.

## Use

### Update

To update [CSV database file](DB_fromAPI.csv), run [dataAPI.py](lib/dataAPI.py) or [updateFunction.py](updateFunction.py).

#### Get update data

- Date from [latestUpdate.date](latestUpdate.py).
- Dollar value from [latestUpdate.value](latestUpdate.py)

### Graph

Running [graph.py](lib/graph.py) will output graphed out data of the dollar exchange rate history, including both linear and polynomial regression lines.

`r` and `r2_score` determine the linear and polynomial relation between the data respectively. The closer the number is to 1 or -1, the more relation ther is between the data.
