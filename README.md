Impact of COVID-19 on UK BAME population
==============================

COVID-19 has disproportionately affected the BAME population in the UK. Unlike the USA, healthcare is universally accessible through NHS. So there may be deeper socio-economic issues leaving this group more exposed to coronovirus and other negative shocks. This repo aims to bring together and analyse relevant socio-economic data to help explain this imbalance.

## Current Data 
- **Covid Deaths**: - Data used in the [UK COVID BAME report](https://www.gov.uk/government/publications/covid-19-review-of-disparities-in-risks-and-outcomes)
- **Covid Deaths**: Subnational level data is used from the amazing Yin Lin who curates this data daily: [Daily updated facebook page](https://www.facebook.com/groups/224857015370702/)

- **Ethnicity Census data** gives ethnicity breakdown by local authoratitive region [2011 census](https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest#data-sources)

## Data Backlog 
- Amenities from OSM?
- Wealth of LAD


# Running the Repo
- git clone the repo
- `pip install -r requirements.txt`
- to start the data import - run `src/data/datastore.py`
- then can import cleaned data from `data/interim`
- to use notebooks;
```python
import datastore
datastore.lib # gives list of data sets e.g. ['ethnicity_data', 'fbook_covid_data']
datastore.ethnicity_data.data_url # url of original source
datastore.ethnicity_data.df # the data as a dataframe
```


Just want to see what we've come up with? Check out [reports](reports)

# Contributing
Yes please! The repo is structured to separate the data *getting and cleaning* from the *analysis*. So feel free to pick what suits you. If you're just getting into python, I will be producing some example notebooks, so have a look through [those](notebooks). Always appreciate any comments or suggestions for the repo, any suggestions about datasets, analysis or features please raise an issue. 
 
Repo structure based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)

## Backlog 
- use altair for visualisations
- add incidence of amminites (such as super markets?)
- care home and job data
- use causality approaches
- https://geographicdata.science/book/intro 
