import pandas as pd
from pathlib import Path
from api import fetcher

def forming_dataset(*, start_time: str, end_time: str) -> pd.DataFrame:
    pass

def fixed_dataset() -> pd.DataFrame:
    flight = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path("C:/Users/Joshua Xu/Documents/McGill 2021-2022/python_tutorial/dataset").glob("flightlist_*.csv.gz")
    )
    return flight
