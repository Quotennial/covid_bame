import pandas as pd
import requests
from config import ROOT_DIR
from data_classes import Dataset

def read_facebook_data(url:str)->pd.DataFrame:
    covid_df = pd.read_excel(url, sheet_name="L4-LTLA",
                        usecols="B:AJ").dropna(subset=['Population (ONS estimates mid-2018)'])
    covid_df.columns = covid_df.columns.astype(str)
    return covid_df

def read_bame_cases(url:str)->pd.DataFrame:
    cases_df = pd.read_excel(url, engine="odf", sheet_name="Table_2a", skiprows=6, nrows=160)
    return cases_df

def read_bame_deaths(url:str)->pd.DataFrame:
    cases_df = pd.read_excel(url, engine="odf", sheet_name="Table_2b", skiprows=6, nrows=158)
    return cases_df

def read_bame_exces_deaths(url:str)->pd.DataFrame:
    cases_df = pd.read_excel(url, engine="odf", sheet_name="Table_2c", skiprows=7, nrows=161)
    return cases_df

def read_ons_deaths(url:str)->pd.DataFrame:
    r = requests.get(url)
    fpath = f"{ROOT_DIR}/../../data/external/ons_covid.xlsx"
    with open(fpath, 'wb') as outfile:
        outfile.write(r.content)
    cases_df = pd.read_excel(fpath, sheet_name="Table 2", skiprows=4, nrows=390)
    cases_df.drop(['Unnamed: 6', 'Unnamed: 9', 'Unnamed: 12'], axis=1, inplace =True)
    cases_df.columns = ["Sex","Geography","Area code","Area name", 
                    "all_Deaths", "all_Rate", "all Lower CI", "all Upper CI", 
                    "covid_Deaths", "covid_Rate", "covid Lower CI", "covid Upper CI"]

    return cases_df


if __name__ == "main":
    pass