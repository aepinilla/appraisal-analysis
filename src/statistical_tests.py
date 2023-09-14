
from statsmodels.stats.anova import AnovaRM
import scikit_posthocs
from statsmodels.multivariate.manova import MANOVA
from scipy import stats

from src.detect_outliers import detect_outliers
from src.settings import dimensions, scenes

def statistical_tests():

    # Read data without outliers
    data = detect_outliers()

    # Assumptions
    ## Assumption of normality: Shapiro-Wilks Test
    all_shapiro_results = {}
    for dim in dimensions:
        dimension_data = data[dim]
        shapiro_results_dim = {}
        for s in scenes:
            df = dimension_data.loc[dimension_data['scene'] == s]
            shapiro_test = stats.shapiro(df[dim])
            shapiro_results_dim[s] = round(shapiro_test[1], 3)
        all_shapiro_results[dim] = shapiro_results_dim

    # Residuals are normally distributed in 3 of the 10 cells of the experimental design

    ## Homogeneity of variances: Levene Test
    levene_results = {}
    for dim in dimensions:
        levene_dimension = data[dim].pivot(index='participant', columns='scene')
        levene_dimension.columns = ['Calming', 'Depressing', 'Exciting', 'Neutral', 'Stressing']
        levene_test = stats.levene(levene_dimension['Calming'],
                                   levene_dimension['Depressing'],
                                   levene_dimension['Exciting'],
                                   levene_dimension['Neutral'],
                                   levene_dimension['Stressing'])
        levene_results[dim] = round(levene_test[1], 3)

    # Variances are equal between groups
    print("P-values obtained with Levene's test:", levene_results)

    # MANOVA
    manova_df = data['valence'].merge(data['arousal'], on=['scene', 'participant'])
    manova_df = manova_df.merge(data['dominance'], on=['scene', 'participant'])
    maov = MANOVA.from_formula('valence + \
                                 arousal  ~ scene', data=manova_df)
    print(maov.mv_test())
    print("Number of participants:", len(manova_df.participant.unique()))

    # One Way ANOVAs
    for dim in dimensions:
        aov_dimension = AnovaRM(data=manova_df, depvar=dim, subject='participant', within=['scene']).fit()
        print(dim, aov_dimension)

    # Tukey post-hoc test
    tukey_results = {}
    for dim in dimensions:
        tukey_dim_results = scikit_posthocs.posthoc_tukey(manova_df, val_col=dim, group_col='scene')
        tukey_results[dim] = tukey_dim_results
        print(dim, tukey_dim_results)

