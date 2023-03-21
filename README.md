# Class_Project

## Why this Project
We wanted to look at the future of electronic and fuel cell vehicles and research the demographic for each and determine if there are any differences in the customer base that purchased these vehicles.  

## Objective
Based on the data we want to identify Current FCV & BEV Owners Demographics and see if there are any major differences between the two car owners.
For our ML model we will attemp to predict based on the information if we can identify the customer as a FCV or BEV owner.

## Description of the Data
This dataset presents results from a survey of FCV and BEV owners over the course of 2015 - 2017 to compare the sociodeographic profile of FCV and BEV owners.

## Questions to answer
1. ML Model to predict based on the demographics determine if the owner is a FCV or BEV owner
2. Review BEV or FCV owners and determine if their Demographics have and major differences or similarities
    -  Male or Female the Primiary Customers of each type of Vehicle Type
    - Any similarities/differences between the customer home and education demoggraphics
    - Any similarities/differences between the customer car useage
    

## Segment 1
- [x] Create a repository for the project, and then invite the other team members to join it.
- [x] Decide on a topic for the project—that is, think of a question that using data can answer
- [x] Source a dataset or, if applicable, multiple datasets that will suit your needs.
- [ ] Begin to clean, organize, and perform an exploratory data analysis on your datasets so that they're ready for analysis.
  - ETL on FCV Dataset.ipynb is a cleaned copy of the dataset and provides export to export folder
  - perform some EDA.
- [ ] Include mock-ups of a machine learning model and a database

### Next Steps
1. ETL Group
    - Determine Null values and see how we should treat them
    - Update the Manufacturer Names
    - Review the datatypes...
2. ML Group
    - Mock up models
        - Decision Trees
        - Random Forest
        - Boosting
3. Databases
    - Finalize the Excel export for Daniel 
    
## Things people wanna do
 - Ryan - ETL
 - Nick - ML & Viz (Tableau)
 - Christy - ML & Viz (Tableau)
 - Daniel - SQL
 - Warren - ETL and assist where needed

### Due Dates: 
 - Segment 1: March 22nd 
 - Segment 2: March 29
 - Segment 3: April 5th! & Final day of class


**Things to Think About**
- What to do about all the missing data?
- There are a few columns we need to figure out what values mean (Education, 1-4).
- Which columns are we dropping...although I think Ryan has this figured out for us. 
- So the target column is the VEH, BEV dummy?? There are 2 values 1 or 0. Which matchs to VEH and which to BEV?
- Should we convert the date column to a datetime data type?
