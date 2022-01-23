import pandas as pd
from pathlib import Path


def fix_dataset() -> pd.DataFrame:
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in
        Path("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list
