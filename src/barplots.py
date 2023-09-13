import seaborn as sns
import matplotlib.pyplot as plt

from src.detect_outliers import detect_outliers
from src.settings import dimensions

def barplots():
    # Get data without outliers
    data = detect_outliers()

    # Rearrange data for barplots
    barplot_df = data['valence'].merge(data['arousal'], on=['scene', 'participant'])
    barplot_df = barplot_df.merge(data['dominance'], on=['scene', 'participant'])
    barplot_df = barplot_df.drop(['participant'], axis=1)

    # Barplots
    for dim in dimensions:
        sns.set_style("whitegrid")
        ax = sns.barplot(x="scene", y=dim, data=barplot_df, color="tab:blue")
        sns.despine()
        ax.set_xlabel("Scene name", fontsize = 15)
        ax.set_ylabel("Mean %s ratings" % (dim), fontsize = 15)
        plt.ylim(1, 9)
        plt.savefig('figures/barplot_%s.png' % (dim), dpi = 300)
        plt.show()

