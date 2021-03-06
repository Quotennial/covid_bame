Impact of COVID-19 on UK BAME population
==============================

This repo aims to bring together and analyse spatial data relevant to the impact of COVID-19 on UK BAME population. COVID-19 has disproportionately affected the BAME population in the UK. Unlike the USA, healthcare is universally accessible through NHS. So there may be deeper socio-economic issues leaving this group more exposed to the impacts of coronovirus. This repo aims to bring together and analyse relevant socio-economic data to help explain this imbalance.

Just want to see what we've come up with? Check out [reports](reports), otherwise clone the repo and get the data!

## Current Data 
- **Excess Deaths**: Angus, Colin (2020): COVID-19 Local Authority Death and Case Plots. The University of Sheffield. Online resource. https://doi.org/10.15131/shef.data.12658088 
- **Covid Deaths**: ONS [Deaths involving COVID](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/datasets/coronavirusandthesocialimpactsongreatbritaindata) released 03 July 2020
- **Covid Deaths**: - Data used in the [UK COVID BAME report](https://www.gov.uk/government/publications/covid-19-review-of-disparities-in-risks-and-outcomes)
- **Covid Cases**: Subnational level data is used from the amazing Yin Lin who curates this data daily: [Daily updated facebook page](https://www.facebook.com/groups/224857015370702/)

- **Ethnicity Census data** gives ethnicity breakdown by local authoratitive region [2011 census](https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest#data-sources)
- **Furlough Data**
- **Key Workers Data** [link](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/keyworkersreferencetables)
- **Deprivation Index** [link]("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833970/File_1_-_IMD2019_Index_of_Multiple_Deprivation.xlsx)
- **Population Estimates** [link](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland)

## Data Backlog 
- Amenities from OSM?
- Wealth of LAD?


# Running the Repo
- clone the repo
- `pip install -r requirements.txt`
- to start the data import - run `src/data/datastore.py`
- then can import processed data ins csv form from `data/interim`
- **or** to use in notebooks;

```python
import sys
sys.path.insert(0, '../src/data')
import bame_datastore
bame_datastore.lib # gives list of datasets
```
```python
{'mortality': ['fbook_covid_data',
  'bame_rpt_deaths',
  'bame_rpt_excess_deaths',
  'ons_deaths'],
 'explanatory': ['ethnicity_data',
  'bame_rpt_cases',
  'furlough_data',
  'key_workers',
  'deprivation'],
 'other': ['lad_geog']}
 ```

```python
datastore.ethnicity_data.data_url # url of original source
datastore.ethnicity_data.df # the data as a dataframe
```

# Contributing
Yes please! The repo is structured to separate the data *getting and cleaning* from the *analysis*. So feel free to pick what suits you. If you're just getting into python, I will be producing some example notebooks, so have a look through [those](notebooks). Always appreciate any comments or suggestions for the repo, any suggestions about datasets, analysis or features please raise an issue. 
 
Repo structure based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)

