import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime as DT

def question_counts(df):
    '''
    Create column that is the count of the number of questions answered by each user
    '''
    counts = df.groupby('user_id').size()
    counts.name = 'counts'
    df = df.set_index('user_id').join(counts).reset_index()
    #Set counts = 0 if user has not answered any questions
    df.loc[df.question_id.isnull(), 'counts'] = 0
    return df


def dummify(new_df, col):
    '''
    - Create dummy variable columns for selected categorical variables
    - Add dummy variable df to new_df
    - Drop original categorical columns from dataframe
    '''
    dummies_df = pd.get_dummies(new_df[col])
    #dummies_df = dummies_df.astype(int)
    new_df = pd.concat([new_df, dummies_df], axis=1)
    new_df = new_df.drop(col, axis=1)

    return new_df

def create_dummies(df):
    '''
    Create dummy variable columns for categorical variables with a limited number
    of categories:

    gender
    education
    visibility to other users (connections only or all users)
    '''
    #Gender
    dummify(df, 'gender')
    # #Education
    dummify(df, 'education')
    # #Visibility
    dummify(df, 'visible_to')

    return df

def to_day_of_week(df, col):
    df['day_answered'] = df[col].dt.dayofweek
    return df

def answering_questions(row):
    '''
    Many users are logging in but not answering questions. Creating variables for
    these cases.
    1: user still logging in but not answering questions
    2: user still logging in and answering questions
    3: user not logging in or answering questions
    '''
    if row['churn_month']==False and row['q_churn_month']==True:
        return 1
    if row['churn_month']==False and row['q_churn_month']==False:
        return 2
    if row['churn_month']==True and row['q_churn_month']==True:
        return 3

def message_counts(df):
    '''
    Create column that is the count of the number of questions answered by each user
    '''
    message_counts = df.groupby('user_id').size()
    message_counts.name = 'message_counts'
    df = df.set_index('user_id').join(message_counts).reset_index()
    #Set counts = 0 if user has not sent any messages
    df.loc[df.message_id.isnull(), 'counts'] = 0
    return df



# def churn_columns(df):
#     '''
#     Add 4 columns for churn:
#         - churn_2weeks: based on activity within 2 weeks of most recent date
#         - churn_month: based on activity within 1 month of most recent date
#         - q_churn_2Weeks: based on question answered within 2 weeks of most recent date
#         - q_churn_month: based on question answered within 1 month of most recent date
#     '''
#     #hard-coded dates because dataframe is a snapshot - if working with current
#     #data, would instead use 2 weeks/1 month prior to 'now'
#     df['churn_2Weeks'] = df['last_seen_at'] < '2015-10-19'
#     df['churn_month'] = df['last_seen_at'] < '2015-10-02'
#     df['q_churn_2Weeks'] = df['ans_created'] < '2015-10-19'
#     df['q_churn_month'] = df['ans_created'] < '2015-10-02'
#
#     return df
