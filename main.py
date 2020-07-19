import random

import pandas as pd
import streamlit as lit

from bootstrap import *
from content import *
from sections import *
from models import DataView



def main():
    page = lit.sidebar.radio("Page",
                             pages
                             )
    page_layout = {
        "title": page,
        "subtitle": page_render[page]['subtitle'],
        "description": page_render[page]['description'],
    }
    jumbo_layout = {
        "bg": f"bg-{page_render[page]['bg']}",
        "inner_jumbo": inner.format_map(page_layout)
    }
    write(jumbo.format_map(jumbo_layout))
    section = lit.sidebar.radio("Section",
                                list(page_render[page]['sections'].keys())
                                )
    write(card.format(f'{page} - {section}', section, page_render[page]['sections'][section]))
    section_render(section, lit)
    # d = DataView("d", lit)
    # t = DataView("t", lit)
    # d.render()
    # t.render()


main()
