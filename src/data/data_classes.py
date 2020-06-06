from config import ROOT_DIR
from typing import Callable
import pandas as pd
import geopandas as gpd
import os


class Dataset():
    def __init__(self, data_name: str, data_url: str, lad_col: str) -> None:
        """[summary]

        Args:
            data_name (str): Name of the data set 
            data_url (str): Can be url of raw data or path to the external data folder
            lad_col (str): Column name where the Local Authority Districts will be held
        """
        self.data_name = data_name
        self.data_url = data_url
        self.lad_col = lad_col
        # TODO add description and maybe original url?

    def read_data(self, tailored_func: Callable) -> None:
        path = f"{ROOT_DIR}/../../data/interim/clean_{self.data_name}.csv"
        if os.path.exists(path):  # if there is a clean version already
            print(f"Found local clean copy of {self.data_name}")
            self.df = pd.read_csv(path)
        else:
            print(f"Downloading and cleaning External Data {self.data_name}")
            raw_df = tailored_func(self.data_url)
            raw_df.to_csv(path, index=False)
            self.df = raw_df.set_index(self.lad_col)

class GeogData(Dataset):
    def read_data(self) -> None:
        path = f"{ROOT_DIR}/../../data/geog/{self.data_name}.geojson"
        if os.path.exists(path):  # if there is a clean version already
            print(f"Found local clean copy of {self.data_name}")
            self.gdf = gpd.read_file(path)
        else:
            print("Unable to locate geoJSON, please make sure it is in the geog file and name is correct")

        

