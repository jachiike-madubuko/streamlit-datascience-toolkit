import seaborn as sns
from matplotlib import pyplot as plt
from collections import defaultdict

import numpy as np

import pandas as pd
pd.set_option('display.max_columns', 100)

# Seaborn for easier visualization
sns.set_style('darkgrid')

from utils.exploratory_analysis import *
from utils.data_cleaning import *

df = None

def data_structures_render(lit,color):
    data_struct = lit.selectbox('Pick a data structure', [
                                'Lists', 'Tuples', 'Sets', 'Dictionaries'])
    lit.header(data_struct)
    if data_struct == 'Lists':
        with lit.echo():
            5+5*5
            v = 44
            v
    if data_struct == 'Tuples':
        lit.subheader('tuples content here')
    if data_struct == 'Sets':
        lit.subheader('set content here')
    if data_struct == 'Dictionaries':
        lit.subheader('dict content here')


def numpy_render(lit,color):
    lit.header('num my pie')


def pandas_render(lit,color):
    lit.header('black and white')


def flow_render(lit,color):
    lit.header('hustle and flow')


def fake_render(lit,color):
    lit.header('fake mean')


def mean_render(lit,color):
    lit.header('lean mean')


def poly_render(lit,color):
    lit.header('polyglot')


def tree_render(lit,color):
    lit.header('trees and leaves')


def truth_render(lit,color):
    lit.header('🎨')


def explore_render(lit, color):
    url = 'data/real_estate_data.csv'
    df = import_csv(url)
    exploratory_analysis(lit=lit, df=df, color=color)
    # categorical = list(df.columns[df.dtypes == 'object'])
    # numerical = list(df.columns[df.dtypes != 'object'])

    # cate = lit.selectbox('Categorical Cols', categorical)
    # sns.countplot(y=cate, data=df)
    # lit.pyplot()

    # num = lit.selectbox('Numerical Cols', numerical)
    # sns.boxplot(y=cate, x=num, data=df)
    # lit.pyplot()


def cleaning_render(lit, color):
    url = 'data/real_estate_data.csv'
    df = import_csv(url)
    abt = data_cleaning_routine(lit=lit, df=df, color=color)



def feat_render(lit,color):
    lit.header('feat fire')


def regress_render(lit,color):
    lit.header('🧨🧨🧨🧨🧨')


def training_render(lit,color):
    lit.header('trainigign ada🎨')


def truth_render(lit,color):
    lit.header('you can\'t handle the trth🎨')


def more_explore_render(lit,color):
    lit.header('space dadadadaaaa')


def abt_render(lit,color):
    lit.header('abt vs ebt')


def classification_render(lit,color):
    lit.header('classy aintcha')


def eval_render(lit,color):
    lit.header('you 👩🏿‍🚀')


def predict_render(lit,color):
    lit.header('🕵🏿‍♀️🕵🏿‍♀️🕵🏿‍♂️🕵🏿‍♂️')


def wrangling_render(lit,color):
    lit.header('🐴')


def reduction_render(lit,color):
    lit.header('🌌☄')


def pca_render(lit,color):
    lit.header('PCA')


def cluster_render(lit,color):
    lit.header('🌠☄')


def analysis_render(lit,color):
    lit.header('🎈🎄🎀')


def stars_render(lit,color):
    lit.header('🌟🌟')


def mission_render(lit,color):
    lit.header('⚔⚒')


def launch_render(lit,color):
    lit.header('🚀🚀🚀')


def voyage_render(lit,color):
    lit.header('🎢')


def arrival_render(lit,color):
    lit.header('📍')


def planet_render(lit,color):
    lit.header('👽')


def section_render(section, lit, color):
    def nothing():
        lit.write('nothing yet, get to it fool')
        lit.balloons()
    section_dict = defaultdict(nothing)

    # python DataScience Class
    section_dict["Data Structures"] = data_structures_render
    section_dict["Flow and Functions"] = flow_render
    section_dict["NumPy"] = numpy_render
    section_dict["Pandas"] = pandas_render

    # Model Complexity
    section_dict['Fake It Til You Make It'] = fake_render
    section_dict['Mean Models & Linear Regression'] = mean_render
    section_dict['Polynomial Regression & Model Parameters'] = poly_render
    section_dict['Decision Trees & Model Tuning'] = tree_render
    section_dict['Unseen Data & The Search for Empirical Truth'] = truth_render

    # real estate
    section_dict['Exploratory Analysis'] = explore_render
    section_dict['Data Cleaning'] = cleaning_render
    section_dict['Feature Engineering'] = feat_render
    section_dict['Regression Model Selection'] = regress_render
    section_dict['Model Training'] = training_render

    # CPO
    section_dict['Exploratory Analysis 2'] = more_explore_render
    section_dict['ABT'] = abt_render
    section_dict['Classification Model Selection'] = classification_render
    section_dict['Model Evaluation'] = eval_render
    section_dict['Production Prediction'] = predict_render

    # unsupervised
    section_dict['Data Wrangling'] = wrangling_render
    section_dict['Dimensionality Reduction'] = reduction_render
    section_dict['PCA'] = pca_render
    section_dict['Clustering Model Selection'] = cluster_render
    section_dict['Cluster Analysis'] = analysis_render

    section_dict['To The Stars'] = stars_render
    section_dict['The Mission'] = mission_render
    section_dict['The Launch'] = launch_render
    section_dict['The Voyage'] = voyage_render
    section_dict['The Arrival'] = arrival_render
    section_dict['The New Planet'] = planet_render

    if section_dict[section]:
        section_dict[section](lit, color)
