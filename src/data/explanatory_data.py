import pandas as pd
import requests
from data_classes import Dataset
from config import ROOT_DIR


def read_ethnicity_data(data_url: str) -> pd.DataFrame:
    """Reads and cleans the 2011 census data on ethnicity break down by local authority.

    Args:
        data_url (str): web url or path to raw data 

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    race_df_raw = pd.read_csv(data_url)
    drop = "% of national ethnic population in this LA area"
    # drop rows with national comparisons
    race_df_raw = race_df_raw[race_df_raw.Measure != drop]
    race_df_raw = race_df_raw[race_df_raw.Measure == "% of local population in this ethnic group"]
    race_df_raw = race_df_raw[race_df_raw.Ethnicity_type == "ONS 2011 5+1"]

    race_df = pd.pivot_table(race_df_raw,
                             index=["Geography_code",
                                    "Geography_name", "Denominator"],
                             columns="Ethnicity",
                             values="Value").reset_index()
    race_df.columns.name = None  # remove column name

    return race_df

def read_furlough_data(url:str) -> pd.DataFrame:
    df = pd.read_excel(url, sheet_name="5. Local Authority", skiprows=5, nrows=480)
    df.dropna(thresh=3, inplace=True)
    df.drop(df.columns[0], axis=1, inplace=True)
    df.columns = ["Area Code", "Area Name", "total_furloughed"]
    return df

def read_key_workers(url:str)->pd.DataFrame:
    r = requests.get(url)
    fpath = f"{ROOT_DIR}/../../data/external/keyworkers.xlsx"
    with open(fpath, 'wb') as outfile:
        outfile.write(r.content)
    df = pd.read_excel(fpath, sheet_name="Table 19", skiprows=4, nrows=378)
    df.drop(df.columns[3:], axis=1, inplace =True)
    df.columns = ["Area Name", "total_key_workers", "pct_of_pop"]
    return df

def read_deprivation(url:str)->pd.DataFrame:
    r = requests.get(url)
    fpath = f"../data/external/deprv_index.xlsx"
    with open(fpath, 'wb') as outfile:
        outfile.write(r.content)
    df_read = pd.read_excel(fpath, sheet_name="IMD2019")
    df_read.rename(columns={"Index of Multiple Deprivation (IMD) Rank": "IMD_rank", 
        "Index of Multiple Deprivation (IMD) Decile": "IMD_decile"}, inplace=True)
    depriv_df_mean = df_read.groupby(["Local Authority District code (2019)" ,"Local Authority District name (2019)"]).mean()
    depriv_df_std = df_read.groupby(["Local Authority District code (2019)" ,"Local Authority District name (2019)"]).std()
    df = depriv_df_mean.join(depriv_df_std, lsuffix="_avg", rsuffix="_std").reset_index()
    return df

def read_pop_est(url:str)->pd.DataFrame:
    r = requests.get(url)
    fpath = f"{ROOT_DIR}/../../data/external/pop_est.xlsx"
    with open(fpath, 'wb') as outfile:
        outfile.write(r.content)
    df_read = pd.read_excel(fpath, sheet_name="MYE2 - Persons", skiprows=4).dropna()
    return df_read
if __name__ == "__main__":
    pass


