"""
Imports all the CSV files collected during the experiment
"""

import os
import pandas as pd

from src.settings import d


def read_data():
    # Define path to folder
    data_folder_path = d + "/data-analysis/data/sam/"
    # Build list with responses
    responses_list = []
    for root, dirs, files in os.walk(data_folder_path):
        for file in files:
            if file.endswith(".csv"):
                f = pd.read_csv(data_folder_path + "/" + file, names=["participant", "date", "sceneStartTime", "sceneName", "valence", "arousal", "dominance"])
            responses_list.append(f)

    responses_pd = pd.concat(responses_list)
    # Drop unnecessary columns
    responses_pd = responses_pd.drop(['date', 'sceneStartTime'], axis=1).drop_duplicates()
    responses_pd.columns = ['participant', 'scene', 'valence', 'arousal', 'dominance']

    return responses_pd


if __name__ == "__main__":
    read_data()
