import pandas as pd
import requests
from config import ROOT_DIR
from data_classes import Dataset

def read_facebook_data(url:str)->pd.DataFrame:
    covid_df = pd.read_excel(url, sheet_name="L4-LTLA",
                        usecols="B:BB").dropna(subset=['Population (ONS estimates mid-2018)'])
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
    deaths_df_raw = pd.read_excel(fpath, sheet_name="Registrations - All data", skiprows=3)

    area_nme_col = deaths_df_raw.columns[2] # becasue of trailing space in column name 
    deaths_df = deaths_df_raw.groupby([area_nme_col,'Cause of death', 'Week number']).sum() #get counts by week no.
    deaths_df = deaths_df.groupby([area_nme_col,'Cause of death']).sum().reset_index() # get total counts
    
    deaths_df = deaths_df.pivot(index = "Area name ", columns = "Cause of death") #format columns
    deaths_df.columns = deaths_df.columns.map(''.join)
    deaths_df = deaths_df.reset_index()
    deaths_df.columns = ["Area Name", "deaths_all", "deaths_covid"]

    return deaths_df


if __name__ == "main":
    pass