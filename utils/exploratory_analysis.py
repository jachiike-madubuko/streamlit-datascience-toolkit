import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
# https: // docs.streamlit.io/en/stable/api.html
# Pandas for DataFrames
import pandas as pd
import altair as alt

# Matplotlib for visualization
# display plots in the notebook

# Seaborn for easier visualization
sns.set_style('darkgrid')

def import_csv(lit, url):
    df = pd.read_csv(url)
    lit.write(df.head(100))
    return df


def exploratory_analysis(lit, df):
    lit.subheader(
        'TODO:Template to display shape and number of categorical vs numerical cols')
    lit.write(df.shape)
    lit.write(df.dtypes)

    lit.subheader('Data Distribution')
    df.hist()
    lit.pyplot()

    lit.subheader('Numerical Features')
    lit.write(df.describe())

    lit.subheader('Categorical Features')
    lit.write(df.describe(include=['object']))

class DataView(object):
    def __init__(self, name, lit):
        super().__init__()
        self.data = pd.DataFrame([
            {"name": f"{name}_obj{i}", "id": i, "price": random.randint(0,25)} for i in range(1000)
        ])
        self.view=None
        self.name=name
        self.lit=lit
        self.title=lit.write(name)
        self.view_state="options"
        self.view_states=["options", "data", "stats"]
        self.dataview=lit.empty()
        self.statsview=lit.empty()
        self.optionsview=lit.empty()
        self.layout()

    def layout(self):
        self.dataview
        self.statsview
        self.optionsview

    def display(self, view):
        self.update_button()
        self.stats_button()
        self.data_button()

    def update(self):
        self.data = pd.DataFrame([
            {"name": f"{self.name}_obj{i}", "id": i, "price": random.randint(100,2005)} for i in range(100)
        ])

    def update_button(self):
        if self.lit.button(f'update {self.name}',"press for stats"):
            self.update()

    def data_button(self):
        if self.lit.button(f'{self.name} data',"press for stats"):
            self.dataview.dataframe(self.data)
    def stats_button(self):
        if self.lit.button(f'{self.name} stats',"press for stats"):
            # self.display('stats')
            # self.dataview.dataframe(self.data)
            self.statsview.dataframe(self.data.describe())

    def buttons(self):
        self.update_button()
        self.stats_button()
        self.data_button()

    def render(self):
        # view = self.lit.radio(f'Select {self.name} View',('data','stats','options'))
        # self.update_button()
        self.buttons()

        self.lit.dataframe(self.data.describe())
        self.lit.dataframe(self.data)
        # if view =='options':


class DataModel(object):
    #handles data manipulation and maintaining state using external data sources
    def __init__(self):
        super().__init__()

class DataController(object):
    #handles business logic to for updating the view and model based on changes to either
    def __init__(self):
        super().__init__()



#try setting global litty varible to enable data caching
#figure out how to advance cache
class DataMVC(object):
    def __init__(self, lit, url):
        super().__init__()
        # self.data_model = DataModel()
        # self.data_view = DataView()
        # self.data_controller = DataController()
        self.url = url
        self.lit = lit
        self.df = None
        self.import_csv()

    def get_df(self):
        return self.df

    def import_csv(self):
        self.df = pd.read_csv(self.url)
        self.lit.header(self.url.split('/')[-1][:-4].replace('_', ' ').title())
        self.lit.write(self.df.head(100))
        return self.df

    def exploratory_analysis(self):
        self.lit.subheader(
            'TODO:Template to display shape and number of categorical vs numerical cols')
        self.lit.write(self.df.shape)
        self.lit.write(self.df.dtypes)

        self.lit.subheader('Data Distribution')
        plt.figure(figsize=(8,8))
        self.df.hist()
        self.lit.pyplot()

        self.lit.subheader('Numerical Features')
        # TODO: figure out how to add pandas stlying  of data smells like missing values and std of 0
        self.lit.write(self.df.describe())

        self.lit.subheader('Categorical Features')
        self.lit.write(self.df.describe(include=['object']))

        categorical = list(self.df.columns[self.df.dtypes == 'object'])
        numerical = list(self.df.columns[self.df.dtypes != 'object'])

        cate = self.lit.selectbox('Categorical Cols', categorical)
        sns.countplot(y=cate, data=self.df)
        self.lit.pyplot()

        num = self.lit.selectbox('Numerical Cols', numerical)
        sns.boxplot(y=cate, x=num, data=self.df)
        sns.heatmap(self.df.corr(), cmap='RdBu_r')
        self.lit.pyplot()

        self.lit.write(self.df.groupby(cate).mean())
        self.lit.header('Do workbook exercises before moving to data cleaning')
