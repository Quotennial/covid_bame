from explanatory_data import read_ethnicity_data
from covid_data import read_facebook_data
from data_classes import Dataset
import config

def gen_obj(data_attr:dict, function):
    data_object = Dataset(data_name = data_attr["name"],
    data_url=data_attr["url"],
    lad_col=data_attr["geog_col"])
    data_object.read_data(function)
    return data_object



ethnicity_attr = {"name": "ethnicity_2011",
                    "url": "https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest/downloads/ethnic-population-by-local-authority.csv",
                    "geog_col":"Geography_name"}

ethnicity_data = gen_obj(ethnicity_attr, read_ethnicity_data)



fbook_covid_attr = {"name": "fbook_covid_deaths",
                    "url": "data/external/COVID-19 UK Cases.xlsx",
                    "geog_col":"LTLA Name"}

fbook_covid_data = gen_obj(fbook_covid_attr, read_facebook_data)
