import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def import_csv(url):
    df = pd.read_csv(url)
    # lit.write(df.head(100))
    return df


def data_cleaning_routine(lit):
    lit.header('Drop Unwanted Observations')
    lit.header('Fix Structural Errors')
    lit.header('Remove "Guilty" Outliers')
    lit.header('Handle Missing Data')

