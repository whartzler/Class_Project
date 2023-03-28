# Class_Project

## Overview of Project
As the world shifts its focus from the traditional fossil fuel-powered vehicle towards an eco-friendlier stance, electric vehicles (EVs) have begun to take center stage.  Because of this rapidly changing global demeanor relative to the automobile industry, it was only natural that we were interested in doing a project involving EVs.  Given that EVs are becoming so prevalent in today’s society, there are many different types of EVs to consider.  For example, battery electric vehicles (BEVs) are vehicles that produce power via an electric motor that runs on large rechargeable battery packs, plug-in hybrid electric vehicles (PHEVs) are vehicles that run on both gasoline and battery packs that are recharged via an external source, fuel-cell vehicles (FCVs) are vehicles that generate electricity via electrical and chemical processes that involve converting hydrogen and oxygen into usable electricity for the vehicle to operate, etc.  As we can see, the scope of discussion can be very broad. 

## Goal 
Our goal is to could create a machine learning model that can predict if a customer has purchased an FCV or a BEV based on a range of sociodemographic data and compare the demographics of each customer base to see if their is common similarities between the groups.  	

## Description of Dataset
The dataset used for this project contains results from a survey of FCV and BEV owners from California households from 2015 – 2017.  The [dataset](https://doi.org/10.25338/B8P313) has an accompanying [article](https://escholarship.org/uc/item/866706mr) that thoroughly explains how the producers of the data acquired the information, as well as a comprehensive analysis of the data itself. Our citation of the dataset that accompanies this article is given at the bottom of this page.

In order to produce a working machine learning model that can predict whether a consumer was a purchaser of an FCV or a BEV, we first had to clean the data.  To do this, we first loaded the dataset into a Jupyter Notebook file and began implementing a typical data cleansing routine.  This routine consisted of familiarizing ourselves with the data by examining the number of rows (27,021) and the number of columns (25), as well as determining what types of data were available to work with.  The columns of the data consisted of sociodemographic information such as a consumer’s household income, education level, age, gender, how important the consumer felt reducing greenhouse gas emissions were, etc.  After reviewing the data that was available, we began preparing the data for a machine learning model by correcting misspelled values, dropping null values, eliminating significant outliers, and encoding values that were to be ultimately placed into the machine learning model. 
[place this paragraph in results section with images of each major data cleaning step?]

[paragraph discussing the SQL database]

[paragraph discussing the data visualizations with Tableau]

After our data was successfully cleaned, we turned our attention to creating machine learning models.  Given that all of the data is labelled and available, we knew that we would be using a supervised machine learning model.  In particular, we decided to use a [finish this paragraph by discussing the types of machine learning models used].  

## References
Citation of the dataset: 
Hardman, Scott (2019), Sociodemographic data for battery electric vehicle owning households in California (From NCST Project "Understanding the Early Adopters of Fuel Cell Vehicles"), Dryad, Dataset, https://doi.org/10.25338/B8P313

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
    

## Segment 2
- [ ] A detailed README.md file that includes the project status, images, descriptions, and results
- [ ] A machine learning model, including a confusion matrix and accuracy score 
- [ ] Database that stores data for the project with at least two tables or collections
- [ ] Selected topic and the reasoning for that selection (2 points)
- [ ] Description of the data (3 points)
- [ ] Questions that the team originally planned to answer with the project (2 points)
- [ ] Description of the data exploration phase of the project (5 points)
- [ ] Description of the analysis phase of the project (5 points)
- [ ] Technologies, languages, tools, and algorithms that the team used throughout the project (3 points)

### Next Steps

    
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


**Things to Think About For Wednesday**

Our Model evaluation criterion

The model can make two types of wrong predictions:

1 = Client purchasing a FCV, 0 = Client purchases a BEV

- Predicting an client will buy an FCV when the client buys an BEV
- Predicting an client will not FCV when the client actually does buy a VEH 

Consider which of the following metrics should be used:

- Accuracy, Recall, Precision
- F1 Score
- Receiving Operating Characteristics(ROC),Area under the Curve(AUC)
- Log Loss
