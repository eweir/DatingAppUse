import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime as DT

'''
These functions create variables based on geographic user data
'''

def categorize_region(row):
    '''
    Categorized region of user:
        - 1 = Washington
        - 2 = California
        - 3 = Oregon
        - 4 = New York
        - 5 = Other
    '''
    if row['region'] == 'WA':
        return 1
    if row['region'] == 'CA':
        return 2
    if row['region'] == 'OR':
        return 3
    if row['region'] == 'NY':
        return 4
    else:
        return 5

def region_category(df):
    '''
    Create column with categorized regions:
        - 1 = Washington
        - 2 = California
        - 3 = Oregon
        - 4 = New York
        - 5 = Other
    '''
    df['region_category'] = df.apply(lambda row: categorize_region(row), axis=1)
    return df

def categorize_cities(row, col='city'):
    '''
    Categorize cities based on popularity/number of users in each city
    1: Seattle
    2: Portland
    3: New York
    4: Los Angeles
    5: San Francisco

    col set to 'city' based on primary data source, can be changed if column
    comes from a different data source
    '''
    if row[col] == 'Seattle':
        return 1
    if row[col] == 'Portland':
        return 2
    if row[col] == 'New York':
        return 3
    if row[col] == 'Los Angeles':
        return 4
    if row[col] == 'San Francisco':
        return 5
    else:
        return 6

def city_filter_column(df):
    '''
    Create column of city categories
    '''
    df['City_filter'] = df.apply(lambda row: categorize_cities(row), axis=1)
    return df
