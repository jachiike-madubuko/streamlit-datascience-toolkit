import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
# https: // docs.streamlit.io/en/stable/api.html
# Pandas for DataFrames
import pandas as pd
import altair as alt
from bootstrap import *


# Matplotlib for visualization
# display plots in the notebook

# Seaborn for easier visualization
# sns.set_style('darkgrid')

def import_csv(url):
    df = pd.read_csv(url)
    # lit.write(df.head(100))
    return df


def col_types(df):
    categorical = list(df.columns[df.dtypes == 'object'])
    numerical = list(df.columns[df.dtypes != 'object'])
    return categorical, numerical

def exploratory_analysis(lit, df, color):
    categorical, numerical = col_types(df)
    percent_missing = 100 - (df.isna().mean().round(4) * 100)
    lit.write(card.format('bg-'+color, 'Data Summary', f'{str(df.shape[0])} samples and {str(df.shape[1])} features',
    two_col_temp.format(
            'Categorical',
            list_render(categorical, color, percent_missing),
            'Numerical',
            list_render(numerical, color,percent_missing)
            )),
        unsafe_allow_html=True)
    corrs = df.corr()
    mask = np.zeros_like(corrs)
    mask[np.triu_indices_from(mask)] = 1
    plt.figure(figsize=(9,8))
    sns.heatmap(
       corrs*100,
        cmap='RdBu_r',
        annot=True,
        fmt='.0f',
        mask=mask,
        cbar=False
        )
    lit.pyplot()
    lit.write(df.describe())
    # lit.write(list(dict(df.count()).values()))

    lit.subheader('Numerical Features')
    df.hist(figsize=(14, 14), xrot=-45)
    lit.pyplot()

    # TODO: figure out how to add pandas stlying  of data smells like missing values and std of 0
    lit.subheader('Categorical Features')
    lit.write(df.describe(include=['object']))


    cate = lit.selectbox('Categorical Cols', categorical)
    num = lit.selectbox('Numerical Cols', numerical)
    sns.countplot(y=cate, data=df)
    lit.pyplot()

    sns.boxplot(y=cate, x=num, data=df)
    lit.pyplot()

    cates = lit.multiselect('Cate Group', categorical, default=categorical[0],)
    aggs = lit.multiselect('Agg types', ['mean', 'std', 'sum', 'min', 'max'], default='mean')
    lit.write(df.groupby(cates).agg(aggs))

