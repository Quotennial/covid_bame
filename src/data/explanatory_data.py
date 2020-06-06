import pandas as pd
from data_classes import Dataset


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
    race_df = pd.pivot_table(race_df_raw,
                             index=["Geography_code",
                                    "Geography_name", "Denominator"],
                             columns="Ethnicity",
                             values="Value").reset_index()
    race_df.columns.name = None  # remove column name

    return race_df


# TODO put these config variables in some config file
ethnic_data_name = "ethnicity_2011"
ethnic_url = "https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest/downloads/ethnic-population-by-local-authority.csv"
ethnic_lad = "Geography_name"
ethnicity_data = Dataset(data_name=ethnic_data_name,
                         data_url=ethnic_url, lad_col=ethnic_lad)
ethnicity_data.read_data(read_ethnicity_data)
