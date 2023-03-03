import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("advertisement_clicks.csv")

#separate data
values_A = df.loc[df['advertisement_id'] == "A", 'action'].values
values_B = df.loc[df['advertisement_id'] == "B", 'action'].values

#find size
size_A = len(values_A)
size_B = len(values_B)

#find current mean
mean_A = np.mean(values_A)
mean_B = np.mean(values_B)

print("A", size_A, mean_A)
print("B", size_B, mean_B)

#t-test
t_t, p_t = stats.ttest_ind(values_A, values_B)
print('T-test: ', t_t, p_t)

#welch t-test
t_w, p_w = stats.ttest_ind(values_A, values_B, equal_var=False)
print('Welch T-test: ', t_w, p_w)


