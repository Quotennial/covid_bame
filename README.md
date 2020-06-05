Impact of COVID-19 on UK BAME population
==============================

COVID-19 has disproportionately affected the BAME population in the UK. Unlike the USA, healthcare is universally accessible through NHS, so imbalances may be the result of deeper socio-economic issues. This repo aims to bring together and analyse relevant socio-economic data to help explain this imbalance.

## Current Data 

- **Covid Deaths**: Subnational level data is used from the amazing Yin Lin who curates this data daily: [Daily updated facebook page](https://www.facebook.com/groups/224857015370702/)

- **Ethnicity Census data** gives ethnicity breakdown by locak authoratitive region [2011 census](https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/regional-ethnic-diversity/latest#data-sources)

## Data Pipeline 
- Data uses in the [UK COVID BAME report](https://www.gov.uk/government/publications/covid-19-review-of-disparities-in-risks-and-outcomes)
- Amenities from OSM?


# Running the Repo
TODO

# Contributing
Yes please! The repo is structured as to separate the data getting and cleaning from the analysis. So whichever area you would like to contribute to please do. If you're just getting into python, I will be producing some example notebooks so have a look through [those](notebooks). I would really appreciate any comments or suggestions for the repo :)
 
Repo structure based on the [cookiecutter data science project template]("https://drivendata.github.io/cookiecutter-data-science/)

## Backlog 
Repo
- pick a local authority boundary http://geoportal.statistics.gov.uk/datasets/ae90afc385c04d869bc8cf8890bd1bcd_1 
- make data import routines - all based around LAD. Then can select which data to import
- select which coronavirus data is used?

Features
- use altair for visualisations
- add incidence of amminites (such as super markets?)
- care home and job data
- use causality approaches
- https://geographicdata.science/book/intro 
