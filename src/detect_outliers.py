"""
Detects and removes outliers
"""

import seaborn as sns
import matplotlib.pyplot as plt

from src.settings import dimensions
from src.read_data import read_data


def detect_outliers():

    data = read_data().reset_index(drop=True)
    not_outliers = {}
    for dim in dimensions:
        # Boxplots
        ax = sns.boxplot(x='scene', hue='scene', y=dim, data=data)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set(xlabel='Scene', ylabel = "Mean ratings in the %s scale" % (dim))
        plt.savefig(('figures/boxplot_%s.png' % (dim)), dpi=300, bbox_inches='tight')
        plt.show()

        # Perform IQR
        scale = data[[dim]]
        scenes_participants = data[['scene', 'participant']]

        Q1 = scale.quantile(0.25)
        Q3 = scale.quantile(0.75)
        IQR = Q3 - Q1

        # Return the values that are not outliers
        data_out = scale[~((scale < (Q1 - 1.5 * IQR)) | (scale > (Q3 + 1.5 * IQR))).any(axis=1)]
        data_with_labels = data_out.join(scenes_participants)
        not_outliers[dim] = data_with_labels

        # Print number of outliers detected
        n_outliers = len(data_out) - len(data)
        print(n_outliers, "outliers have been detected in dimension", dim)

    return not_outliers


if __name__ == "__main__":
    detect_outliers()