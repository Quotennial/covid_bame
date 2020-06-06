from typing import Callable
import pandas as pd
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
        path = f"data/interim/clean_{self.data_name}.csv"
        if os.path.exists(path):  # if there is a clean version already
            print("Found local clean copy")
            self.df = pd.read_csv(path)
        else:
            print("Downloading and cleaning External Data")
            raw_df = tailored_func(self.data_url)
            raw_df.to_csv(path, index=False)
            self.df = raw_df.set_index(self.lad_col)

