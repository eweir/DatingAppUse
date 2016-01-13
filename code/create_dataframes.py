'''
Load tables into dataframes, clean data, dummify gender, age, and visible_to, add outcome columns
'''

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime as DT

def engine(user, password):
    '''
    Create engine to load sql tables into dataframes
    '''
    engine = create_engine('postgresql://user:password@localhost/capstone', echo=False)

    return engine


def load_sql_tables(table):
    '''
    Create dataframes from sql tables
    '''

    df = pd.read_sql_table(table, engine)

    return df

def to_utf8(df, col):
    '''
    Encode columns as utf-8
    '''
    df[col] = df[col].apply(lambda x: x.encode('utf-8') if x is not None else np.nan)
    return df

def data_cleaning(df):
    '''
    Clean data
    - remove rows where user is a test user or admin/tech support
    - convert text columns to str format

    '''

    df = df[df['user_id'] != 1]
    df = df[df['user_id'] != 4]
    df = df[df['user_id'] != 5]

    to_utf8(df, 'question_body')
    to_utf8(df, 'ans_body')

    return df


def outcome_columns(df):
    '''
    Create outcome columns:
        - q_ans: user has answered at least two questions (required to answer 1 question at signup)
        - connected: user has at least one connection
        - only_signup: user has signed up but hasn't answered any questions or made
                       any connections

    '''
    df['q_ans'] = df['counts'] >= 2
    df['connected'] = df['num_connections'] >= 1
    df['only_signup'] = (df['connected'] == False) & (df['q_ans'] == False)

    return df


def usage(row):
    '''
    Categorize level of engagement based on content of only_signup, q_ans,
    and connected columns
    '''
    if row['only_signup']:
        return 1
    if row['q_ans'] and not row['connected']:
        return 2
    if row['connected']:
        return 3
    return 'other'

def engagement_level_col(df):
    '''
    Create column for engagement_level outcome variable

    only_signup = level 1
    q_ans = level 2
    connected = level 3
    '''
    df['engagement_level'] = df.apply(lambda row: usage(row), axis=1)
    return df


def active(df):
    '''
    Create binary variable for whether user is active in the app
    False = only signup
    True = some activity (question answered or connections)

    Cast variable as integer
    '''
    df['active'] = df['engagement_level'] != 1
    df['active'] = df['active'].astype(int)
    return df

def connect(df):
    '''
    Create binary variable for whether user is connected to other users
    0 = answered questions but no connections
    1 = made connections
    '''

    df['connect'] = df['engagement_level'].map({2:0, 3:1})
    return df


def to_day_of_week(df, col):
    '''
    Create column containing the day of the week on which a question was answered
    '''
    df['day_answered'] = df[col].dt.dayofweek
    return df
