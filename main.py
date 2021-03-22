import seaborn as sns
from matplotlib import pyplot as plt
import random

import pandas as pd
import streamlit as lit

from bootstrap import *
from content import *
from helper import *
from sections import *
from models import DataView
import numpy as np

# Pandas for DataFrames
pd.set_option('display.max_columns', 100)

# Matplotlib for visualization

# Seaborn for easier visualization
sns.set_style('darkgrid')

def main():
    #could create jumbo after section is decided to put section info into jumbo
    page = lit.sidebar.radio("Page", pages)
    page_layout = {
        "title": page,
        "subtitle": page_render[page]['subtitle'],
        "description": list_group_render(page_render[page]),
    }
    jumbo_layout = {
        "bg": f"bg-{page_render[page]['bg']}",
        "inner_jumbo": inner.format_map(page_layout)
    }
    write(lit,jumbo.format_map(jumbo_layout))
    section = lit.sidebar.radio("Section",
                                list(page_render[page]['sections'].keys())
                                )
    write(lit,card.format(f"bg-{page_render[page]['bg']}", f'{page} - {section}', section,
                      page_render[page]['sections'][section]))
    section_render(section, lit, page_render[page]['bg'])
    # write(lit,'<iframe class="card shadow-lg rounded-10" height=1500 width=500 src="http://faux-me-up.surge.sh/"> </iframe >')
    # d = DataView("d", lit)
    # t = DataView("t", lit)
    # d.render()
    # t.render()


main()



