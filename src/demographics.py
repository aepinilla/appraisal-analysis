"""
Basic demographics
"""

import os
import pandas as pd

def demographics():
    d = os.path.dirname(os.getcwd())
    data = pd.read_csv(d + '/data-analysis/data/demographics.csv')
    data.columns = ['timestamp', 'age', 'gender', 'need_glasses', 'using_glasses']

    demographics_dict = {
        'mean_age': round(data.age.mean(), 2),
        'sd_age': round(data.age.std(), 2),
        'gender': data.groupby('gender').count(),
        'min_age': data.age.min(),
        'max_age': data.age.max()
    }

    print(demographics_dict)


if __name__ == "__main__":
    demographics()