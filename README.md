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

- [x] Format CSV files to merge into single usable database.
- [ ] Introduce feature to update [FullExchangeRate.csv](/FullExchangeRate.csv) with [updateFunction.py](/updateFunction.py) output
- [ ] Migrate [TO-DO list](#to-do-list) to GitHub issues
- [ ] Update [README.md Use section](#use)
- [ ] Reintroduce data graphs
- [ ] [Fix x ticks in graph to show dates instead of timestamps.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/2)
- [ ] Use last points in regression models to predict next dollar value.

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
