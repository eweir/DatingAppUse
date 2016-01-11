import pandas as pd
import numpy as np

#To be run after create_dataframes.py

def users_table(df):
    '''
    Create dataframe with only one row per user - engagement level is assigned to
    each user

    In this dataframe, multiple questions and answers per user are not retained and
    predictors consist of data unique to the user (e.g., age, search_proximity, education)
    '''
    df = df.sort_values('engagement_level').groupby('user_id', as_index=False).first()
    return df

def questions_table(df):
    '''
    Create dataframe with only questions that were answered

    In this dataframe, there are multiple rows for some users - one row for every
    answer to a question
        - This way question ID and content are retained
        - May be able to use question content, ID, sponsor_id, etc to predict
          'connect' variable
    Can be used to predict 'connect' variable: Whether a user made connections
    after answering questions, or just answered questions
        0 = answered question(s) and did not make any connections
        1 = answered question(s) and made at least one connection
    '''

    df = df[df['question_body'].notnull()]
    return df

def churn_table_use(df, date1, date2, col='last_seen_at'):
    '''
    Create churn table and add 2 columns for churn:
        - churn_2weeks: based on activity within 2 weeks of most recent date
        - churn_month: based on activity within 1 month of most recent date
    '''
    #hard-coded dates because dataframe is a snapshot - if working with current
    #data, would instead use 2 weeks/1 month prior to 'now'
    df = df[df[col].notnull()]
    df['churn_2weeks'] = df[col] < date1
    df['churn_month'] = df[col] < date2

    return df

def churn_table_questions(df, col='ans_created'):
    '''
    Create question churn table and add 2 columns for churn:
        - q_churn_2Weeks: based on question answered within 2 weeks of most recent date
        - q_churn_month: based on question answered within 1 month of most recent date
    '''
    df = df[df[col].notnull()]
    df['q_churn_2weeks'] = df[col] < '2015-10-19'
    df['q_churn_month'] = df[col] < '2015-10-02'
    return df

# def churn_columns(df):
#     '''
#     Add two columns for churn:
#         - churn_2weeks: based on activity within 2 weeks of most recent date
#         - churn_month: based on activity within 1 month of most recent date
#     '''
#     #hard-coded dates because dataframe is a snapshot - if working with current
#     #data, would instead use 2 weeks/1 month prior to 'now'
#     df['churn_2Weeks'] = df['last_seen_at'] < '2015-10-19'
#     df['churn_month'] = df['last_seen_at'] < '2015-10-02'
#
#     return df
