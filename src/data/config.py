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
