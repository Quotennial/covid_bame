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
    area_cd_col = deaths_df_raw.columns[0] # becasue of trailing space in column name 
    deaths_df = deaths_df_raw.groupby([area_cd_col, area_nme_col,'Cause of death', 'Week number']).sum() #get counts by week no.
    deaths_df = deaths_df.groupby([area_cd_col, area_nme_col,'Cause of death']).sum().reset_index() # get total counts
    deaths_df = deaths_df.pivot(index = area_cd_col, columns = "Cause of death") #format columns
    deaths_df.columns = deaths_df.columns.map(''.join)
    deaths_df = deaths_df.reset_index().drop(columns = [deaths_df.columns[1]])
    deaths_df.columns = ["Area code", "Area Name", "deaths_all", "deaths_covid"]
    deaths_df

    return deaths_df

def read_excess_deaths_grp(url:str)->pd.DataFrame:
    raw_df = pd.read_csv(url, index_col=0)

    df_max = raw_df.dropna().groupby(["code"]).max()
    df_max = df_max[['name', 'week', 'pop']]

    df_mean = raw_df.dropna().groupby(["code"]).mean()
    df_mean = df_mean[['excessrate','othexcess','COVIDrate']]

    df_sum = raw_df.groupby(["code"]).sum()
    df_sum = df_sum[["deaths.1519", "AllCause.20", "COVID.20", "Other.20", "allexcess", "excessrate", "othexcess"]]
    df = df_max.join(df_sum).join(df_mean, lsuffix="_sum", rsuffix="_mean")
    df.to_csv("test.csv")
    return df.reset_index()

def read_excess_deaths_loc(url:str)->pd.DataFrame:
    raw_df = pd.read_csv(url, index_col=0)

    df_max = raw_df.dropna().groupby(["code", "location"]).max()
    df_max = df_max[['name', 'week', 'pop']]

    df_mean = raw_df.dropna().groupby(["code", "location"]).mean()
    df_mean = df_mean[['excessrate','othexcess','COVIDrate']]

    df_sum = raw_df.groupby(["code", "location"]).sum()
    df_sum = df_sum[["deaths.1519", "AllCause.20", "COVID.20", "Other.20", "allexcess", "excessrate", "othexcess"]]

    df = df_max.join(df_sum).join(df_mean, lsuffix="_sum", rsuffix="_mean")
    return df.reset_index()


if __name__ == "main":
    pass