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
        'bg': 'primary',
        'subtitle': 'Python for Data Science',
        'description': 'Python for Data Science',
        'sections': {
            'Data Structures': "Lists, Tuples, Sets & Dictionaries",
            # 'Data Structures': "I. Lists are mutable sequences of objects. \n II. Tuples are immutable sequences of objects. \n III. Sets are collections of unique objects. \n IV. Dictionaries are collections of key-value pairs.",
            'Flow and Functions': "IF, FOR, List comprehensions, Functions",
            'NumPy': "encore",
            'Pandas': "broads in Atlanta"
        }
    },
    {
        'bg': 'secondary',
        'subtitle': 'How the world works',
        'description': 'How the world works',
        'sections': {
            'Fake It Til You Make It': "nah",
            'Mean Models & Linear Regression': "mean good",
            'Polynomial Regression & Model Parameters': "poly",
            'Decision Trees & Model Tuning': "trees",
            'Unseen Data & The Search for Empirical Truth': "da truff",
        }
    },
    {
        'bg': 'info',
        'subtitle': 'Real-Estate Tycoon',
        'description': 'Real-Estate Tycoon',
        'sections': {
            'Exploratory Analysis': "explore",
            'Data Cleaning': 'Data Cleaning',
            'Feature Engineering': 'Feature Engineering',
            'Regression Model Selection': 'Regression Model Selection',
            'Model Training': 'Model Training',
        }
    },
    {
        'bg': 'success',
        'subtitle': 'Know your people',
        'description': 'Know your people, know your power',
        'sections': {
            'Exploratory Analysis 2': 'Exploratory Analysis 2',
            'ABT': 'ABT',
            'Classification Model Selection': 'Classification Model Selection',
            'Model Evaluation': 'Model Evaluation',
            'Production Prediction': 'Production Prediction',
    }
    },
    {
        'bg': 'danger',
        'subtitle': 'Super swaggy',
        'description': 'Super swaggy',
        'sections': {
            'Data Wrangling': 'Data Wrangling',
            'Dimensionality Reduction': 'Dimensionality Reduction',
            'PCA': 'PCA',
            'Clustering Model Selection': 'Clustering Model Selection',
            'Cluster Analysis': 'Cluster Analysis',
        }
    },
    {
        'bg': 'warning',
        'subtitle': 'To the stars',
        'description': 'To the stars',
        'sections': {
            'To The Stars': 'To The Stars',
            'The Mission': 'The Mission',
            'The Launch': 'The Launch',
            'The Voyage': 'The Voyage',
            'The Arrival': 'The Arrival',
            'The New Planet': 'The New Planet'
        }
    },
]
page_render = dict(zip(list(pages), page_data))


def write(text):
    if "<" in text:
        lit.write(text, unsafe_allow_html=True)
    else:
        lit.write(text)
