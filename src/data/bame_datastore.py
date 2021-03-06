from explanatory_data import read_ethnicity_data, read_furlough_data, read_key_workers, read_deprivation, read_pop_est
from covid_data import read_facebook_data, read_bame_cases, read_bame_deaths, read_bame_exces_deaths, read_ons_deaths, read_excess_deaths_grp, read_excess_deaths_loc
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

lad_geog = gen_geog_obj(config.lad_dict)

fbook_covid_data = gen_obj(config.fbook_covid_cases_dict, read_facebook_data)
bame_rpt_cases = gen_obj(config.bame_cases_dict, read_bame_cases)
bame_rpt_deaths = gen_obj(config.bame_deaths_dict, read_bame_deaths)
bame_rpt_excess_deaths = gen_obj(config.bame_excess_deaths_dict, read_bame_exces_deaths)
ons_deaths = gen_obj(config.ons_deaths_dict, read_ons_deaths)
excess_deaths_grp = gen_obj(config.excess_deaths_grp_dict, read_excess_deaths_grp)
excess_deaths_loc = gen_obj(config.excess_deaths_loc_dict, read_excess_deaths_loc)


ethnicity_data = gen_obj(config.ethnicity_dict, read_ethnicity_data)
furlough_data = gen_obj(config.furlough_dict, read_furlough_data)
key_workers = gen_obj(config.key_workers_dict, read_key_workers)
deprivation = gen_obj(config.deprivation_dict, read_deprivation)
pop_est = gen_obj(config.pop_est_dict, read_pop_est)

lib = {"mortality": ["excess_deaths_grp", "excess_deaths_loc","fbook_covid_data", "bame_rpt_deaths", "bame_rpt_excess_deaths", "ons_deaths"],
    "explanatory": ["ethnicity_data", "bame_rpt_cases", "furlough_data", "key_workers", "deprivation",
                    "pop_est"],
    "other":["lad_geog"]}

if __name__ == "main":
    ethnicity_data = gen_obj(config.ethnicity_dict, read_ethnicity_data)
    