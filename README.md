# Dollar-Exchange-Rate
Project using conversion from dollar to colombian pesos

## TO-DO list

- [ ] Integrate latestUpdate and latestValue into one file.
- [ ] Convert existing files into functions to call from a main file.
- [ ] Create main file with UI.
- [ ] Graph dollar exchange rate history.

## Libraries

- Datetime
- Pandas
- Sodapy

```
pip install pandas
pip install sodapy
```

## Use

### Update

To update [CSV database file](tasa_cambio.csv), run [dataAPI.py](dataAPI.py)

#### Get update data

- Date from [latestUpdate.py](latestUpdate.py).
- Dollar value from [latestValue.py](latestValue.py)