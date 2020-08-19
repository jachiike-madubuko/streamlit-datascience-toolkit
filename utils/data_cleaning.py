import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns



def data_cleaning_routine(lit, df,color):
    lit.header('Drop Unwanted Observations')
    lit.write(df.head(5))
    lit.write(df.shape)
    df= df.drop_duplicates()
    lit.header('Fix Structural Errors')
    lit.write(df.basement.unique())
    df.basement.fillna(0, inplace=True)
    lit.write(df.basement.unique())
    sns.countplot(y='roof', data=df)
    df.roof.replace(['shake-shingle', 'asphalt,shake-shingle'], 'Shake Shingle',
                    inplace=True)
    df.roof.replace('composition', 'Composition', inplace=True)
    df.roof.replace('asphalt', 'Asphalt', inplace=True)
    lit.pyplot()
    # lit.subheader('TODO: create a widget for cleaning data')
    # col = lit.selectbox('Columns', df.columns[df.dtypes == 'object'])
    # values = lit.multiselect('Values', df[col].unique())
    # replacement = lit.text_input('replacement')
    # lit.subheader(f'{values} => {replacement}')
    # replace = lit.button('REPLACE')

    # if replace:
    #     df[col].replace(values, replacement,inplace=True)
    # sns.countplot(y=col, data=df)
    df.exterior_walls.replace(['Block', 'Concrete'],
                              'Concrete Block', inplace=True)
    df.exterior_walls.replace(['Rock, Stone'],
                              'Masonry', inplace=True)
    sns.countplot(y='exterior_walls', data=df)
    lit.pyplot()
    lit.header('Remove "Guilty" Outliers')
    num_col = lit.selectbox('Numerical Columns', df.columns[df.dtypes != 'object'])
    sns.boxplot(df[num_col])
    top = 1.1*(df[num_col].max() +df[num_col].min())
    plt.xlim(0,top)
    lit.pyplot()
    sns.violinplot(num_col, data=df)
    plt.xlim(0,top)
    lit.pyplot()
    lit.header('Handle Missing Data')
    lit.subheader('Handle Categorical Missing Data')
    lit.write(df.select_dtypes(include=['object']).isnull().sum())
    for col, num_missing in df.select_dtypes(include=['object']).isnull().sum().items():
        if num_missing != 0:
            # lit.write(col)
            df[col].fillna('Missing', inplace=True)
    lit.write(df.select_dtypes(include=['object']).isnull().sum())
    # for i in df.select_dtypes(include=['object'])
    lit.subheader('Handle Numerical Missing Data')
    lit.write(df.select_dtypes(exclude=['object']).isnull().sum())


