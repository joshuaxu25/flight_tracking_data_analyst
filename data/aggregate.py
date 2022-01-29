import pandas as pd
from pathlib import Path


def fixed_dataset():
    flight = pd.concat(
        pd.read_csv(file, parsedates=["firstseen", "lastseen", "day"])
        for file in Path("C:/Users/Joshua Xu/Documents/McGill 2021-2022/python_tutorial/dataset").glob("flightlist_*.csv")
    )
