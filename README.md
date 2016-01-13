##User Engagement with a Social Discovery App

This project is based on confidential data. Consequently, only the content of my code folder are shared here.

###Motivation

This project was motivated by a business question. The owners of the app wanted to know how many users were churning and who those users are.

###Data

Data for the project was provided in the form of a database snapshot containing 28 tables. I used PostgreSQL to join and modify tables and create a single table with all relevant data on which I performed all analyses. I then used Pandas python data analysis library to load my final table into a dataframe on which I performed data cleaning and  feature engineering, and then used to create outcome variables.


###EDA

Following data cleaning, the project started with exploratory data analysis of various features of the user dataset. In looking at overall user churn, it was clear that there are more users who have not churned than there are users who have churned.

####Region

Regions are anonymized at the request of app owners. All regions followed the same pattern as overall churn, except for region 1. Region 1 also had more males than females, which diverges from other regions and overall ratios. This, along with common professions in the area and region population may contribute to a higher churn rate.

####Age

Churn was relatively consistent among different age groups, and was aligned with overall churn rates for most groups. One notable difference was that users between the ages of 17 and 25 had an almost even ratio of churn/not churn. It is possible that users in this age group are making social connections in daily life and/or are at an age where they are less interested in reaching out to online tools to find social connections.

###Modeling

####Feature Engineering

The project required quite a bit of feature engineering for both predictor and outcome variables. Code for the engineering of features can be found in new_features.py.


####Random Forest

I used a Random Forest Classifier to model churn data. Input variables were: number of questions answered, number of connections, number of messages sent, user age, user preferred age, and geographic proximity. The outcome variable was churn, which was measured as activity with the past month.
