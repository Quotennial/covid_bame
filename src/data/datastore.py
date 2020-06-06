from explanatory_data import read_ethnicity_data
from covid_data import read_facebook_data, read_bame_cases, read_bame_deaths, read_bame_exces_deaths
from data_classes import Dataset, GeogData
import config


def gen_obj(data_attr: dict, function):
    data_object = Dataset(data_name=data_attr["name"],
                          data_url=data_attr["url"],
                          lad_col=data_attr["geog_col"])
    data_object.read_data(function)
    return data_object


def gen_geog_obj(data_attr: dict):
    data_object = GeogData(data_name=data_attr["name"],
                           data_url=data_attr["url"],
                           lad_col=data_attr["geog_col"])
    data_object.read_data()
    return data_object



ethnicity_data = gen_obj(config.ethnicity_dict, read_ethnicity_data)
lad_geog = gen_geog_obj(config.lad_dict)

fbook_covid_data = gen_obj(config.fbook_covid_deaths_dict, read_facebook_data)
bame_rpt_cases = gen_obj(config.bame_cases_dict, read_bame_cases)
bame_rpt_deaths = gen_obj(config.bame_deaths_dict, read_bame_deaths)
bame_rpt_excess_deaths = gen_obj(config.bame_excess_deaths_dict, read_bame_exces_deaths)

lib = ["ethnicity_data", "fbook_covid_data", "lad_geog", 
"bame_rpt_cases", "bame_rpt_deaths", "bame_rpt_excess_deaths"]