import pandas as pd
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



if __name__ == "main": 
    # TODO put these config variables in some config file
    fbook_data_name = "fbook_covid_deaths"
    fbook_filepath = "data/external/COVID-19 UK Cases.xlsx"
    fbook_lad = "LTLA Name"
    fbook_covid_deaths = Dataset(data_name=fbook_data_name, data_url= fbook_filepath, lad_col=fbook_lad)
    fbook_covid_deaths.read_data(read_facebook_data)

    df = pd.read_excel(path, engine="odf", sheet_name="Table_2a", skiprows=6, nrows=160).head()
    print(df)