import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
iris=sns.load_dataset('iris')
s=iris[iris['species']=='setosa']
v=iris[iris['species']=='versicolor']
s_length=s['petal_length']
v_length=v['petal_length']
t_stat,p_value=stats.ttest_ind(s_length,v_length)
alpha=0.05
if p_value<alpha:
    print("Reject the null hypothesis")
    print("There is a significant difference between the petal length of Iris setosa and Iris versicolor.")
else:
    print("Fail to reject the null hypothesis")
    print("There is no significant difference between the petal length of Iris setosa and Iris versicolor.")
model=ols('sepal_length ~ C(species)',data=iris).fit()
anova_table=sm.stats.anova_lm(model,typ=2)
print("\nOne-Way ANOVA Results(statsmodels):")
print(anova_table)
p_value=anova_table['PR(>F)'].iloc[0]
alpha=0.05
if p_value<alpha:
    print("Reject the null hypothesis: There is a significant difference between sepal length among the species.")
else:
    print("Fail to reject the null hypothesis: No significant difference between sepal length among the species.")
