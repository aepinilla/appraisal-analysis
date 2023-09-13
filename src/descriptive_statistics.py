"""
Descriptive statistics
"""

from src.settings import dimensions
from src.detect_outliers import detect_outliers

def descriptive_statistics():
    # Get data without outliers
    data = detect_outliers()

    # Descriptive statistics per dimension
    dimensions_dict = {}
    for dim in dimensions:
        dimension_data = data[dim]
        dimension_data = dimension_data.reset_index(drop = True)

        dimensions_dict[dim + '_mean' ] = round(dimension_data.iloc[:,0].mean(axis = 0), 2)
        dimensions_dict[dim + '_median' ] = round(dimension_data.iloc[:,0].median(axis = 0), 2)
        # dimensions_dict[dim + '_mode' ] = round(dimension_data.iloc[:,0].mode, 2)
        dimensions_dict[dim + '_min' ] = dimension_data.iloc[:,0].min(axis = 0)
        dimensions_dict[dim + '_max' ] = dimension_data.iloc[:,0].max(axis = 0)
        dimensions_dict[dim + '_std' ] = round(dimension_data.iloc[:,0].std(axis = 0), 2)

        mean = round(dimension_data.groupby('scene').mean(), 2)
        std = round(dimension_data.groupby('scene').std(), 2)

        print("Means for", dim, mean)
        print("Std for", dim, std)

    print(dimensions_dict)

