from src.demographics import demographics
from src.descriptive_statistics import descriptive_statistics
from src.heatmaps import heatmaps
from src.histograms import histograms
from src.statistical_tests import statistical_tests
from src.barplots import barplots


def analyse_data():
    demographics()
    descriptive_statistics()
    heatmaps()
    histograms()
    statistical_tests()
    barplots()


if __name__ == "__main__":
    analyse_data()
