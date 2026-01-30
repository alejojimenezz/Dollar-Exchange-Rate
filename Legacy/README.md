# Dollar-Exchange-Rate

Project using conversion from dollar to colombian pesos.

## TO-DO list

- [X] [Integrate latestUpdate and latestValue into one file.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/1)
- [X] Graph dollar exchange rate history.
- [X] Make GUI window mockup.
- [ ] [Fix x ticks in graph to show dates instead of timestamps.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/2)
- [X] Create main file with GUI.
- [X] Convert existing files into functions to call from a main file.
- [ ] Use last points in regression models to predict next dollar value.
- [ ] Test PyQT for GUI.
- [X] [Fix update button to execute only when pushed.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/3)
- [ ] [Update window elements without having to close window.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/4)
- [ ] [Update button not disabling when database is updated.](https://github.com/alejojimenezz/Dollar-Exchange-Rate/issues/5)

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

To update [CSV database file](tasa_cambio.csv), run [dataAPI.py](lib/dataAPI.py)

#### Get update data

- Date from [latestUpdate.date](latestUpdate.py).
- Dollar value from [latestUpdate.value](latestUpdate.py)

### Graph

Running [graph.py](lib/graph.py) will output graphed out data of the dollar exchange rate history, including both linear and polynomial regression lines.

`r` and `r2_score` determine the linear and polynomial relation between the data respectively. The closer the number is to 1 or -1, the more relation ther is between the data.

### Main execution

File [main.py](main.py) calls GUI from [generatedGUI.py](generatedGUI.py), executing functions from previous files to display required data.