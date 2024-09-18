# Is there any outlier in the following series? Find out the lower limit and upper limit of normal range.  
# [7, 9, 17, 45, 48, 51, 52, 63, 65, 72, 130]

import pandas as pd

data = pd.Series([7, 9, 17, 45, 48, 51, 52, 63, 65, 72, 130])

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[(data < lower_limit) | (data > upper_limit)]

print(f"Lower limit: {lower_limit}")
print(f"Upper limit: {upper_limit}")
print(f"Outliers: {outliers.tolist()}")