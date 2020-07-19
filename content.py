import streamlit as lit
pages = ("🐍 for 👩🏿‍💻🧙🏿‍♂️",
         "How the 🌎 Works",
         "🏡 Tycoon",
         "Chief People Officer",
         "Unsupervised Customers",
         "🚀 🌌",
         )
page_data = [
    {
    'bg':'primary',
    'subtitle':'Python for Data Science',
    'description':'Python for Data Science',
    'sections':[
        'Basics',
        'Data Structures',
        'Flow and Functions',
        'NumPy',
        'Pandas'
    ]
    },
    {
    'bg':'secondary',
    'subtitle':'How the world works',
    'description':'How the world works',
    'sections':[
        'Fake It Til You Make It',
        'Mean Models & Linear Regression',
        'Polynomial Regression & Model Parameters',
        'Decision Trees & Model Tuning',
        'Unseen Data & The Search for Empirical Truth',
    ]
    },
    {
    'bg':'info',
    'subtitle':'Real-Estate Tycoon',
    'description':'Real-Estate Tycoon',
    'sections': [
            'Exploratory Analysis',
            'Data Cleaning',
            'Feature Engineering',
            'Regression Model Selection',
            'Model Training',
            ]
    },
    {
    'bg':'success',
    'subtitle':'Know your people',
    'description':'Know your people, know your power',
    'sections': [
            'Exploratory Analysis 2',
            'ABT',
            'Classification Model Selection',
            'Model Evaluation',
            'Production Prediction',
        ]
    },
    {
    'bg':'danger',
    'subtitle':'Super swaggy',
    'description':'Super swaggy',
    'sections': [
            'Data Wrangling',
            'Dimensionality Reduction',
            'PCA',
            'Clustering Model Selection',
            'Cluster Analysis',
        ]
    },
    {
    'bg':'warning',
    'subtitle':'To the stars',
    'description':'To the stars',
    'sections': [
            'To The Stars',
            'The Mission',
            'The Launch',
            'The Voyage',
            'The Arrival',
            'The New Planet'
        ]},
]
page_render = dict(zip(list(pages), page_data))
def write(text):
    if "<" in text:
        lit.write(text, unsafe_allow_html=True)
    else:
        lit.write(text)
