"""
Creates histograms for exploratory analysis
"""

import seaborn as sns
import matplotlib.pyplot as plt

from src.settings import scenes, d
from src.detect_outliers import detect_outliers


def heatmaps():
    # Get data without outliers
    data = detect_outliers()

    # Rearrange data for heatmaps
    heatmap_df = data['valence'].merge(data['arousal'], on=['scene', 'participant'])
    heatmap_df = heatmap_df.merge(data['dominance'], on=['scene', 'participant'])
    heatmap_df = heatmap_df.drop(['participant'], axis=1)

    for s in scenes:
        heatmap_scene = heatmap_df.loc[heatmap_df['scene'] == s]
        heatmap_scene = heatmap_scene.drop(['scene'], axis=1)
        plt.figure(figsize=(20,10))
        corr = heatmap_scene.corr()
        sns.heatmap(corr,cmap="BrBG", annot=True, annot_kws={'size':36})
        sns.set(font_scale=2.0)
        plt.savefig((d + '/data-analysis/figures/heatmap_%s.png' % (s)), dpi = 300)
        plt.show()


if __name__ == "__main__":
    heatmaps()