'''
Add features for visualizations and models
'''

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime as DT

def question_counts(df):
    '''
    Create column that is the count of the number of questions answered by each user
    '''
    q_counts = df.groupby('user_id').size()
    q_counts.name = 'q_counts'
    df = df.set_index('user_id').join(q_counts).reset_index()
    #Set counts = 0 if user has not answered any questions
    df.loc[df.question_id.isnull(), 'q_counts'] = 0
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

def message_and_connect(row, col1='num_connections', col2='message_counts'):
    '''
    Create column for users who have made connections and sent messages
    '''
    return row['connected'] == True and row['messaging'] == True

def message_and_connect_column(df, col1='num_connections', col2='message_counts'):
    '''
    Create message_and_connect column
    '''
    df['num_connections'] = df['num_connections'].fillna(0)
    df['connected'] = df['num_connections'] > 1
    df['messaging'] = df['message_counts'] > 2
    df['message_conn'] = df.apply(lambda row: message_and_connect(row), axis=1)
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
