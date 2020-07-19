import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root


lad_dict = {"name": "Local_Authority_Districts__December_2017__Boundaries_in_the_UK__WGS84_",
                    "url": "http://geoportal1-ons.opendata.arcgis.com/datasets/fab4feab211c4899b602ecfbfbc420a3_2.geojson?outSR={%22latestWkid%22:4326,%22wkid%22:4326}",
                    "page_url": "http://geoportal1-ons.opendata.arcgis.com/datasets/fab4feab211c4899b602ecfbfbc420a3_2.geojson?outSR={%22latestWkid%22:4326,%22wkid%22:4326}",
                    "geog_col":"geometry"}

#### COVID DATA #######
fbook_covid_cases_dict = {"name": "fbook_covid_cases",
                    "url": f"{ROOT_DIR}/../../data/external/COVID-19 UK Cases.xlsx",
                    "geog_col":"LTLA Name"}

bame_cases_dict = {"name": "BAME_report_cases",
                    "url": "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/889167/Disparities_risks_outcomes_of_COVID19_data_pack.ods",
                    "geog_col": "Area Name"}

bame_deaths_dict = {"name": "BAME_report_deaths",
                    "url": "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/889167/Disparities_risks_outcomes_of_COVID19_data_pack.ods",
                    "geog_col": "Area Name"}

bame_excess_deaths_dict = {"name": "bame_excess_deaths",
                    "url": "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/889167/Disparities_risks_outcomes_of_COVID19_data_pack.ods",
                    "geog_col": "Area Name"}

ons_deaths_dict = {"name": "ons_deaths",
            "url":"https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fhealthandsocialcare%2fcausesofdeath%2fdatasets%2fdeathregistrationsandoccurrencesbylocalauthorityandhealthboard%2f2020/lahbtablesweek26.xlsx",
            "page_url": "https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/datasets/deathregistrationsandoccurrencesbylocalauthorityandhealthboard",
            "geog_col":"Area code"}

excess_deaths_grp_dict = {"name": "excess_deaths_data_grp",
            "url":"https://github.com/VictimOfMaths/COVID_LA_Plots/raw/master/LAExcess.csv",
            "page_url": "https://github.com/VictimOfMaths/COVID_LA_Plots",
            "geog_col": "code"}

excess_deaths_loc_dict = {"name": "excess_deaths_data_loc",
            "url":"https://github.com/VictimOfMaths/COVID_LA_Plots/raw/master/LAExcess.csv",
            "page_url": "https://github.com/VictimOfMaths/COVID_LA_Plots",
            "geog_col": "code"}

#### EXPLANATORY DATA ######
ethnicity_dict = {"name": "ethnicity_2011",
                    "url": "https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest/downloads/ethnic-population-by-local-authority.csv",
                    "geog_col":"Geography_code"}

furlough_dict = {"name": "furlough_data",
            "url":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/891607/Coronavirus_Job_Retention_Scheme_Statistics_Tables_June_2020.xlsx",
            "geog_col":"Area Code"}

key_workers_dict = {"name": "key_workers",
            "url":"https://www.ons.gov.uk/file?uri=%2femploymentandlabourmarket%2fpeopleinwork%2fearningsandworkinghours%2fdatasets%2fkeyworkersreferencetables%2fcurrent/keyworkersreferencetableupdated.xlsx",
            "geog_col":"Area Name"}


deprivation_dict = {"name": "deprivation_data",
            "url":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833970/File_1_-_IMD2019_Index_of_Multiple_Deprivation.xlsx",
            "geog_col":"Local Authority District code (2019)"}

pop_est_dict = {"name": "population_est_data",
            "url":"https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fpopulationandmigration%2fpopulationestimates%2fdatasets%2fpopulationestimatesforukenglandandwalesscotlandandnorthernireland%2fmid2019april2020localauthoritydistrictcodes/ukmidyearestimates20192020ladcodes.xls",
            "geog_col":"Code"}
