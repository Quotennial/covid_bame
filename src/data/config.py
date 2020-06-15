import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root


ethnicity_dict = {"name": "ethnicity_2011",
                    "url": "https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest/downloads/ethnic-population-by-local-authority.csv",
                    "geog_col":"Geography_name"}

fbook_covid_deaths_dict = {"name": "fbook_covid_deaths",
                    "url": "data/external/COVID-19 UK Cases.xlsx",
                    "geog_col":"LTLA Name"}



lad_dict = {"name": "Local_Authority_Districts__December_2009__Boundaries",
                    "url": "https://opendata.arcgis.com/datasets/5e14c6bedc8740d19683517e5e902057_3.geojson",
                    "geog_col":"geometry"}


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
            "url":"https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2fdeaths%2fdatasets%2fdeathsinvolvingcovid19bylocalareaanddeprivation%2f1march2020to17april2020/referencetablesdraft.xlsx",
            "geog_col":"Area Name"}

furlough_dict = {"name": "furlough_data",
            "url":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/891607/Coronavirus_Job_Retention_Scheme_Statistics_Tables_June_2020.xlsx",
            "geog_col":"Area Name"}

key_workers_dict = {"name": "key_workers",
            "url":"https://www.ons.gov.uk/file?uri=%2femploymentandlabourmarket%2fpeopleinwork%2fearningsandworkinghours%2fdatasets%2fkeyworkersreferencetables%2fcurrent/keyworkersreferencetableupdated.xlsx",
            "geog_col":"Area Name"}