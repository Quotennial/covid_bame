import pandas as pd
#TODO fix this relative import and linting
from base_data import Dataset

def read_facebook_data(url:str)->pd.DataFrame:
    covid_df = pd.read_excel(url, sheet_name="L4-LTLA",
                        usecols="B:AJ").dropna(subset=['Population (ONS estimates mid-2018)'])
    covid_df.columns = covid_df.columns.astype(str)
    return covid_df


# TODO put these config variables in some config file
fbook_data_name = "fbook_covid_deaths"
fbook_filepath = "data/external/COVID-19 UK Cases.xlsx"
fbook_lad = "LTLA Name"
fbook_covid_deaths = Dataset(data_name=fbook_data_name, data_url= fbook_filepath, lad_col=fbook_lad)
fbook_covid_deaths.read_data(read_facebook_data)