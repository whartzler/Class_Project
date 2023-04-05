# Electric Vehicle Analysis

## Overview of Project
As the world shifts its focus from the traditional fossil fuel-powered vehicle towards an eco-friendlier stance, electric vehicles (EVs) have begun to take center stage.  Because of this rapidly changing global demeanor relative to the automobile industry, it was only natural that we were interested in doing a project involving EVs.  Given that EVs are becoming more and more prevalent in today’s society, there are many different types of EVs to consider.  For example, Battery Electric Vehicles (BEVs) are vehicles that are powered by an electric motor, Plug-in Hybrid Electric Vehicles (PHEVs) are vehicles that have two motors that run on both gasoline and electricity, and Fuel-Cell Vehicles (FCVs) utilize energy stored as hydrogen that gets converted to electricity by a fuel cell.  

## Goal
The goal of this project is to create a machine learning model that can predict if the vehicle purchased is either FCV or a BEV based on a range of sociodemographic data and determine if there are any similar demographics between FCV and BEV owners.


## Data
The dataset used for this project presents results from a survey conducted from 2015 - 2017 of 906 FCV and 12,910 BEV owners in California. The study investigated the sociodemographic profiles of FCV and BEV buyers.  The [dataset](https://doi.org/10.25338/B8P313) has an accompanying [article](https://escholarship.org/uc/item/866706mr) that thoroughly explains how the producers of the data acquired the information, as well as a comprehensive analysis of the data itself. 

## Cleaning the Data
In order to produce a working machine learning model that can predict whether a consumer was a purchaser of an FCV or a BEV, we first had to clean the data.  This process consisted of familiarizing ourselves with the data by examining the number of rows and the number of columns, as well as determining what types of data were available to work with.  The columns of the data consist of sociodemographic information such as a consumer’s household income, education level, age, gender, how important the consumer felt reducing greenhouse gas emissions were, etc.  After reviewing the data, we began preparing the data for a machine learning model by correcting misspelled values, dropping null values, and eliminating significant outliers.

First, we loaded in the dataset and viewed its dimensions, and we found that our original data had 27,021 rows and 25 columns.  Then, after correcting the spelling of several column names and removing several columns that were not needed, we dropped all rows containing null values.  This resulted in a significantly smaller dataset, one with 4,709 rows and 24 columns.  After dropping the null values, we found that our data had an extremely large variance (discussed more in the Data Exploration & Analysis section).  Due to this, we further reduced our dataset to 3,503 rows by removing all the data points that were beyond two standard deviations from their respective means.  Once the data was adequately cleaned, we shifted our attention towards further components of the project, as described below.


## Creating the Database
As part of this project, we created an AWS database to house our data in order to make it publicly accessible. Through PostgreSQL, we imported the csv files, mapped the data types, created tables, and ran some preliminary queries to check the data and ensure its usability.  


## **ML Model Overview**
After the data was successfully cleaned, we turned our attention to creating machine learning models.  Given that all of the data is labelled and available, we knew that we would be using supervised machine learning models. The models chosen were: logistical regression, decision tree, random forest, extreme gradient boosting, single vector machine, and the ridge classifier. The single dataset was cleaned/processed four different ways. The first data set contained outliers. The second dataset had the outliers removed. The third dataset had no outliers and the classes were balanced using oversampling. The final dataset the vehicle attributes: `manufacturer`, `model`, and `model year` columns were dropped. 

### FCV/BEV Dataset - Preprocessed with Outliers
<br>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Train_Accuracy</th>
      <th>Test_Accuracy</th>
      <th>Train_Recall</th>
      <th>Test_Recall</th>
      <th>Train_Precision</th>
      <th>Test_Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Logistical Regression</td>
      <td>0.954187</td>
      <td>0.953999</td>
      <td>0.998721</td>
      <td>0.998509</td>
      <td>0.955060</td>
      <td>0.955064</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Decision Tree</td>
      <td>1.000000</td>
      <td>0.998585</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.999254</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuned Decision Tree</td>
      <td>0.992415</td>
      <td>0.990800</td>
      <td>0.999041</td>
      <td>0.999254</td>
      <td>0.993009</td>
      <td>0.991124</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Random Forest</td>
      <td>1.000000</td>
      <td>0.990800</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.991124</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Random Forest w/weights</td>
      <td>1.000000</td>
      <td>0.992215</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.992593</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tuned Random Forest</td>
      <td>0.949029</td>
      <td>0.949045</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.949029</td>
      <td>0.949045</td>
    </tr>
    <tr>
      <th>6</th>
      <td>XGBoost</td>
      <td>1.000000</td>
      <td>0.998585</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.999254</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tuned XGBoost</td>
      <td>0.999393</td>
      <td>0.998585</td>
      <td>0.999680</td>
      <td>0.999254</td>
      <td>0.999680</td>
      <td>0.999254</td>
    </tr>
  </tbody>
</table>
</div>
<br>  

***Observations:***
All models quickly learned how to predict an FCV or BEV based on the attributes of the vehicle (ie. All Toyota, Mirai models were battery electric vehicles and Teslas were fuel cell vehicles). Even with outliers all models had an very close to perfect 100% prediction accuracy. There did not appear to be any over or underfitting. This dataset was missing the `model year` column.


### FCV/BEV Dataset - Preprocessed without Outliers

<br>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Train_Accuracy</th>
      <th>Test_Accuracy</th>
      <th>Train_Recall</th>
      <th>Test_Recall</th>
      <th>Train_Precision</th>
      <th>Test_Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Logistical Regression</td>
      <td>0.999592</td>
      <td>1.0</td>
      <td>0.999569</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Decision Tree</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuned Decision Tree</td>
      <td>0.999592</td>
      <td>1.0</td>
      <td>0.999569</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Random Forest</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Random Forest w/weights</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tuned Random Forest</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>XGBoost</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tuned XGBoost</td>
      <td>0.999592</td>
      <td>1.0</td>
      <td>0.999569</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
<br>  

***Observations:***
With out outliers all models had a near perfect 100% prediction accuracy. There did not appear to be any over or underfitting. This dataset was missing the `model year` column and included a unnecessary column, `last page`.

### FCV/BEV Dataset - Preprocessed Oversampling

<br>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Train_Accuracy</th>
      <th>Test_Accuracy</th>
      <th>Train_Recall</th>
      <th>Test_Recall</th>
      <th>Train_Precision</th>
      <th>Test_Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Logistical Regression</td>
      <td>0.975728</td>
      <td>0.971691</td>
      <td>0.997442</td>
      <td>0.998509</td>
      <td>0.977444</td>
      <td>0.972404</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Decision Tree</td>
      <td>1.000000</td>
      <td>0.998585</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.999254</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuned Decision Tree</td>
      <td>0.993022</td>
      <td>0.990800</td>
      <td>0.999680</td>
      <td>0.999254</td>
      <td>0.993014</td>
      <td>0.991124</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Random Forest</td>
      <td>1.000000</td>
      <td>0.992215</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.992593</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Random Forest w/weights</td>
      <td>1.000000</td>
      <td>0.992215</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.992593</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tuned Random Forest</td>
      <td>0.980886</td>
      <td>0.973815</td>
      <td>0.999680</td>
      <td>0.999254</td>
      <td>0.980558</td>
      <td>0.973837</td>
    </tr>
    <tr>
      <th>6</th>
      <td>XGBoost</td>
      <td>1.000000</td>
      <td>0.998585</td>
      <td>1.000000</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>0.999254</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tuned XGBoost</td>
      <td>0.999393</td>
      <td>0.999292</td>
      <td>0.999361</td>
      <td>0.999254</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>
<br>

***Observations:***
Given that the BEV and FCV classes were unweighted, it was useful to look at models with the classes balanced. Oversampling was used to balance the classes. Again all models quickly learned how to predict an FCV or BEV based on the attributes of the vehicle (ie. All Toyota, Mirai models were battery electric vehicles and Teslas were fuel cell vehicles). All models had an about an 100% accuracy prediction. There did not appear to be any over or underfitting. This dataset had the `model year` column and the outliers were removed.



### FCV/BEV Dataset - without Manufacturer, Model, & Model Year

<br>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Train_Accuracy</th>
      <th>Test_Accuracy</th>
      <th>Train_Recall</th>
      <th>Test_Recall</th>
      <th>Train_Precision</th>
      <th>Test_Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SVM</td>
      <td>0.843204</td>
      <td>0.842792</td>
      <td>0.828844</td>
      <td>0.832512</td>
      <td>0.851025</td>
      <td>0.855263</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tuned SVM</td>
      <td>0.987938</td>
      <td>0.971873</td>
      <td>0.999565</td>
      <td>1.0</td>
      <td>0.976655</td>
      <td>0.947712</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ridge Classifier</td>
      <td>0.833297</td>
      <td>0.830738</td>
      <td>0.770199</td>
      <td>0.766502</td>
      <td>0.878592</td>
      <td>0.886104</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuned Ridge Classifier</td>
      <td>0.833297</td>
      <td>0.830738</td>
      <td>0.770199</td>
      <td>0.766502</td>
      <td>0.878592</td>
      <td>0.886104</td>
    </tr>
  </tbody>
</table>
</div>
<br>

***Observations:***
Realizing that it was too easy for the models to predict the vehicle type based vehicle attributes. The vehicle attributes were removed to get a better idea of how buyer demographics effected vehicle type. After dropping `manufacturer`, `model`, and `model year` it was interesting to see the all models performances dropped by about 10%. In addition, support vector machine (SVM) and ridge classifier were the models used to train and test the dataset. The tuned SVM model had the highest accuracy at roughly 97%. Since there was little to no difference between the test and train models there was no indication of over or under fitting.

### Understanding the Confusion Matrix

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Predicted/Actual</th>
      <th>FCV (1)</th>
      <th>BEV (0)</th>
    </tr>
    <tr style="text-align: right;">
      <th> FCV (1)</th>
         <td> TP </td>
         <td> FP </td>
     </tr>
     <tr style="text-align: right;">
       <th> BEV (0)</th>
         <td> FN </td>
         <td> TN </td>
     </tr>
  </thead>
  <tbody>
   </tbody>
</table>

**The Tuned XGBoost Model with the Oversampled Data was chosen as the best model.**

The model is predicting whether a car is a battery electric vehicle (BEV - 0) or a fuel cell vehicle (FCV - 1) based on buyer demographics.

**Model evaluation criteria:**
The model can make two types of wrong predictions:
1. Predicting the car is a FEV when it’s really a BEV (FP - Type I Error)
2. Predicting the car is a BEV when it’s really a FEV  (FN - Type II Error)

**Which case is more important?**
	In this case they are the same. We want to maximize the accuracy of both classes (positive and negative), how many of both positive and negative has the model predicted correctly. Accuracy should be high as possible.

The performance of the test set confusion matrix gets 72 (TP), 0 (FP), and 1 (FN), 1340 (FN). 

Accuracy = (72 + 1340)/ (72 + 0 + 1 + 1340) =  .9992 

The Tuned XGBoost Model can correctly predict with a 99% accuracy whether the car is a FEV or BEV based on buyer demographics.

 
### FCV/BEV Dataset - Preprocessed Oversampling, Tuned XGBoost Confusion Matrix

<br>

#### Checking the performance on the train set

<br>
<img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/CM_3_Tuned_XGB_train.png" width="550" height="155" > 
<img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/CM_3_Tuned_XGB_train2.png" > 
 <br>
 
 ### Checking the performance on the test set
 
 <br>
 <img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/CM3_Tuned_XGB_Test2.png" width="550" height="155" > 
 <img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/CM3_Tuned_XGB_Test.png" > 
 
 <br>

### Plotting the Tuned Decision Tree

<br>
<img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/DT1.png" width ="804" height="780">
<br>

***Observations:***
The plot of the decision tree shows the conditions that the model is using to evaluate whether the vehicle is a BEV or FCV. The first three were the `manufacturer`, `model`, and  `model year`. Then the `longest trip`, `number of trips over 200 miles`, and `importance of reducing greenhouse gases` were evaluated to determine the type of vehicle.

### Feature Importance of the Random Forest Model
<br>
<img src="https://github.com/whartzler/Class_Project/blob/main/ML_Models/Images/F_Importance3.png" width="803" height="532">
<br>

***Observations:***
The feature importance was calcuated and sorted from the random forest model. The `manufacturer` had a 33%, `model` had a 37%, and  `model year` a 15% over all the total 19 attributes in determining the prediction. Then the `longest trip` had a 3%, `number of trips over 200 miles` had a 2%, and `importance of reducing greenhouse gases` had a 2% impact compared to all the 19 attributes in determining vehicle type. The feature importance supported the plotted tuned decision tree.


## Tableau Visualizations & Results
We reviewed the biggest gender group of FCV and BEV owners along with different metric's to see if we can find which gender was the primary customer base and if there are any similiarities/differences between the demographics of each group.  We looked at a couple of demographics with examples below.  More can be reviewed on the tableau page.  

#### Gender Breakout
![image](https://user-images.githubusercontent.com/109490755/229959025-c233614e-42d8-4ae1-83c3-e7ae3d3ec307.png)


#### Household Income
When reveiwing the two groups each type of vehicle owner had very similar demograpics through all income groups.  The major differences we Females that had an income less than $150k made up the majority of FCV owners while Female's who had an income between 150k - 250k made up the majority of BEV owners.
![image](https://user-images.githubusercontent.com/109490755/229382069-fb34fcd2-a900-444a-aae2-1a5ba91f8411.png)

#### Education & Home Ownership Comparison
Education and home Ownership also was very similar between the two groups.  As education level increased both FCV and BEV owners the total population % who owned either type of vehicle grew in both male and female's.  Both vehicle groups also had a majority of home owners for male and female owners.
![image](https://user-images.githubusercontent.com/109490755/229958833-581b3261-199b-47a8-8184-83aa0a5d48e2.png)


#### Previously Owned Cars
Looking at 4 types previosuly owned cars FCV and BEV owners owned the data is also very similar.  Both FCV and BEV highest prior car owned was the HEV (Hybrid Electric Vehicle).
![image](https://user-images.githubusercontent.com/109490755/229382425-33ff53d9-b176-4e98-9b3f-b84da7fd80a8.png)


## Technologies
- Importing & Cleaning the Data
  - Python via Jupyter Notebook (Pandas, Numpy, Scipy)
- Database
  - PostgreSQL
- EDA
  - Matplotlib, Seaborn, Numpy
- Machine Learning
  - Sklearn (Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM, Ridge Classifier)
- Visualizations
  - Tableau Public



## File Guide 
- [EDA and ETL Notebook](https://github.com/whartzler/Class_Project/blob/main/Project_Template.ipynb)
- [Tableau Story](https://public.tableau.com/app/profile/warren.hartzler5043/viz/ClassProject_16797804258450/FCVvsBEVCustomerReview)
- [ML Model](https://github.com/whartzler/Class_Project/blob/main/ML_Models/ML_Project.ipynb)
- [Export of Cleaned Dataset](https://github.com/whartzler/Class_Project/tree/main/Exports)
- [Presentation](https://docs.google.com/presentation/d/1UMoQD5Q_BG4J8CWz9ukYXhL95_icRL-jdCqHiMPY6Mc/edit#slide=id.p)

## References
Citation of the dataset: 
Hardman, Scott (2019), Sociodemographic data for battery electric vehicle owning households in California (From NCST Project "Understanding the Early Adopters of Fuel Cell Vehicles"), Dryad, Dataset, https://doi.org/10.25338/B8P313


<hr>



