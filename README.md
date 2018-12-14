# ETL_Project

## Data Sources
Two primary sources of data were used:
    * Kaggle: https://www.kaggle.com/new-york-city/ny-2015-street-tree-census-tree-data
    * Webscrape: http://leafsnap.com/

## Transformations Needed:
The kaggle tree data was used to create two MySQL tables. The first table is an aggreate of tree species by zipcode. This includes the count of trees by species, and an average diameter of the species. 

The tree species table is a combination of the kaggle data and webscraping. The tree common name from the kaggle data had to be transformed to create a web key field, by stripping all spaces and converting characters to lowercase, to compare tp the data from the web scrape.

## Final Product and Tables
The final product is a relational database containing two tables. NYC Tree data table, and Tree Species table. These could then be used to create a web page showing tree data by zipcode, with a supplemental page with details of the specific tree. 
