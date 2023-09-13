"""
Creates histograms for exploratory analysis
"""

import seaborn as sns
import matplotlib.pyplot as plt

from src.settings import dimensions, emotion_types, d
from src.read_data import read_data
from src.detect_outliers import detect_outliers


def histograms():
    # Get data without outliers
    data = detect_outliers()

    # Rearrange data for histograms
    hist_df = data['valence'].merge(data['arousal'], on=['scene', 'participant'])
    hist_df = hist_df.merge(data['dominance'], on=['scene', 'participant'])
    hist_df = hist_df.drop(['participant'], axis=1)

    for dim in dimensions:
        hist_df.loc[hist_df[dim] > 5, '%s_type' % (dim)] = ('high_%s' % (dim))
        hist_df.loc[hist_df[dim] < 5, '%s_type' % (dim)] = ('low_%s' % (dim))
        hist_df.loc[hist_df[dim] == 5, '%s_type' % (dim)] = ('neutral_%s' % (dim))

        for et in emotion_types:
            emotion_type_mask = hist_df[('%s_type' % (dim))] == ('%s_%s' % (et, dim))
            subset = hist_df[emotion_type_mask]
            ax = sns.countplot(x = subset.scene, order = list(['Neutral', 'Exciting', 'Stressing', 'Calming', 'Depressing']))
            ax.set(xlabel='Scene', ylabel = "Count")
            plt.savefig((d + '/data-analysis/figures/hist_%s_%s.png' % (et, dim)), dpi = 300, bbox_inches='tight')
            plt.show()


if __name__ == "__main__":
    histograms()
