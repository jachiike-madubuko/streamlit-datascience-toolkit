import random

import pandas as pd
import streamlit as lit

from bootstrap import *
from content import *
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
                                    page_render[page]['sections']
                                    )
    write(card.format(f'{page} - {section}',page,section))
    if page == pages[0]:
        data = pd.DataFrame([{'id': i, 'name': str(i)+section} for i in range(100)])
        lit.write(data)
    if page == pages[1]:
        write(card.format(f'{page} - {section}',page,section))
    if page == pages[2]:
        write(card.format(f'{page+page} - {section}',page,section))
    if page == pages[3]:
        write(card.format(f'{section} ++ {page}',page,section))
    if page == pages[4]:
        write(card.format(f'{page} ~~ {section}',page,section))
    if page == pages[5]:
        write(card.format(f'{page} __ {section}',page,section))
    # d = DataView("d", lit)
    # t = DataView("t", lit)
    # d.render()
    # t.render()


main()
