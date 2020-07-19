import pandas as pd
import random
from bootstrap import *
class DataView(object):
    def __init__(self, name, lit):
        super().__init__()
        self.data = pd.DataFrame([
            {"name": f"{name}_obj{i}", "id": i, "price": random.randint(0,25)} for i in range(1000)
        ])
        self.view=None
        self.name=name
        self.lit=lit
        btn = self.lit.button(f'hi {name} hi')
        self.title = self.lit.write(card.format(name+name, btn, 'subtitle'), unsafe_allow_html=True)
        self.view_state="options"
        self.view_states=["options", "data", "stats"]
        self.dataview=lit.empty()
        self.statsview=lit.empty()
        self.optionsview=lit.empty()
        # self.layout()

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


class DataMVC(object):
    def __init__(self):
        super().__init__()
        self.data_model = DataModel()
        self.data_view = DataView()
        self.data_controller = DataController()