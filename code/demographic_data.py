import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime as DT

'''
Functions to create and/or modify demographic variables
'''

def gender_categories(row):
    '''
    For larger dataset with updated gender options
    Create gender categories --> helpful for visualizations
    1: woman
    2: man
    3: nonbinary
    4: woman & nonbinary
    5: man & nonbinary
    6: other

    '''
    if row['Genders'] == '["woman"]':
        return 1
    if row['Genders'] == '["man"]':
        return 2
    if row['Genders'] == '["nonbinary"]':
        return 3
    if row['Genders'] == '["woman", "nonbinary"]':
        return 4
    if row['Genders'] == '["man", "nonbinary"]':
        return 5



def gender_category_column(df):
    '''
    Create column of gender categories
    '''
    df['Gender'] = df.apply(lambda row: gender_categories(row), axis=1)
    return df


def age_column(df, col='birthdate'):
    '''
    Create age column based on birthday column
    Fill na values with mean - only 0.3 percent missing values, mean == median, no outliers
    '''
    now = pd.Timestamp(DT.datetime.now())
    #make sure birthday is in 1900s rather than 2000s
    df[col] = df[col].where(df[col] < now, df[col] -  np.timedelta64(100, 'Y'))
    df['age'] = (now - df[col]).astype('<m8[Y]')
    #impute mean
    df['age'] = df['age'].fillna(df['age'].mean())
    return df


def age_grouping(row):
    '''
    Create age groups --> helpful for visualizations
    1: 17-25
    2: 26-35
    3: 36-45
    5: 46-55
    5: 56-66
    '''
    if row['age'] >= 17 and row['age'] < 26:
        return 1
    if row['age'] >= 26 and row['age'] < 36:
        return 2
    if row['age'] >= 36 and row['age'] < 46:
        return 3
    if row['age'] >= 46 and row['age'] < 56:
        return 4
    if row['age'] >= 56 and row['age'] < 67:
        return 5

def age_group_column(df):
    '''
    Create column of age groupings
    '''
    df['age_group'] = df.apply(lambda row: age_grouping(row), axis=1)
    return df

def occupation_grouping(row, col='occupation'):
    '''
    Create occupation groups
    '''
    #create lists of similar occupations
    artist = ['artist', 'Artist']
    student = ['Student', 'Student', 'Graduate Student', 'Designer', 'designer']
    teacher = ['Teacher', 'teacher']
    marketing = ['Marketing', 'marketing','Program Manager', 'Manager', 'Project Manager', 'Product Manager', 'Analyst', 'Sales']
    software = ['Software Engineer', 'Engineer', 'Software Developer']
    health = ['Healthcare']
    law = ['Attorney', 'Lawyer']
    misc = ['Awesome Human', '']

    #assign occupations to categories
    if row[col] in software:
        return 1
    if row[col] in marketing:
        return 2
    if row[col] in student:
        return 3
    if row[col] in teacher:
        return 4
    if row[col] in law:
        return 5
    else:
        return 6

def occupation_group_column(df, col='occupation'):
    '''
    Create column of occupation groupings
    '''
    df['occ_group'] = df.apply(lambda row: occupation_grouping(row, col), axis=1)
    return df
