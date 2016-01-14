##User Engagement with a Social Discovery App

This project is based on confidential data. Consequently, only the content of my code folder are shared here.

###Motivation

This project was motivated by a business question: How many users are churning and who are they? Which users are messaging other users?

###Data

Data for the project was provided in the form of a database snapshot containing 28 tables. I used PostgreSQL to join and modify tables and create a single table with all relevant data on which I performed all analyses. I then used Pandas python data analysis library to load my final table into a dataframe on which I performed data cleaning and  feature engineering, and then used to create outcome variables.


###EDA

Following data cleaning, the project started with exploratory data analysis of various features of the user dataset. In looking at overall user churn, it was clear that there are more users who have not churned than there are users who have churned.

#####Region

Regions are anonymized at the request of app owners. All regions followed the same pattern as overall churn, except for region 1. Region 1 also had more males than females, which diverges from other regions and overall ratios. This, along with common professions in the area and region population may contribute to a higher churn rate.

<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/Region_churn.png" width=500>

#####Age

Churn was relatively consistent among different age groups, and was aligned with overall churn rates for most groups. One notable difference was that users between the ages of 17 and 25 had an almost even ratio of churn/not churn. It is possible that users in this age group are making social connections in daily life and/or are at an age where they are less interested in reaching out to online tools to find social connections.


<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/Churn_age.png" alt="Image Not Found" width=500>

###User Engagement Funnel

Another important question, aside from churn, is related to the user engagement funnel below. The end goal is for users who sign up to eventually send messages to other users, and it will be useful to identify variables that contribute to user messaging behavior.

<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/funnel.png" alt="Image Not Found" width=700>


###Modeling

#####Feature Engineering

The project required quite a bit of feature engineering for both predictor and outcome variables. Code for the engineering of features can be found in new_features.py. Code for geographic features is in geographic_data.py, and code for demographic features is in demographic_data.py


#####Random Forest - Churn

I used a Random Forest Classifier to model churn data. Input variables were: number of questions answered, number of connections, number of messages sent, user age, user preferred age, and geographic proximity. The outcome variable was churn, which was measured as activity with the past month. The random forest model had an AUC of 0.77, with the following ROC plot:

<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/roc_churn.png" alt="Image Not Found" width=500>

#####Feature Importances - Churn

I calculated feature importances from the random forest classifier model. The results can be seen below:

<img src="https://raw.githubusercontent.com/eweir/SocialDiscoveryAppUse/master/images/feat_imports.png" alt="Image Not Found" width=500>


#####Random Forest - Messaging

I also fit a Random Forest model to predict user messaging behavior. Input variables were: number of questions answered, number of connections, user age, user preferred age, and geographic proximity. The outcome variable was weather or not users had sent any messages. The model had an AUC of 0.86, with the following ROC plot:

<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/roc_messaging.png" alt="Image Not Found" width=500>


#####Feature Importances - Messaging

Important features from the random forest classifier can be seen below:

<img src="https://github.com/eweir/SocialDiscoveryAppUse/blob/master/images/feat_import_mess.png" alt="Image Not Found" width=500>

###Next Steps

Next, I would be interested in:
 - Natural language processing of text components of the app
 - Explore user engagement funnel further
    - Look specifically at the behavior of users who find the app from different sources
    - Look at the number of messages exchanged (conversations)
