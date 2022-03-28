# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = lyft_drivers
df['end_year'] = df['end_date'].dt.year
df.query('end_year == "2018"').shape[0]
#df2 = df.dropna(subset = ['end_year'])

df1 = df.pivot_table(columns = 'end_year', values = 'index', aggfunc = 'count').melt()

#print(df1)
#df1.melt(var_name = 'ey', value_name = 'count')
df1['pre'] = df1.value.shift(1).fillna(0)

#df1['cmpr'] = (df1['value'] > df1['pre']).apply(lambda x: 'increase' if x == True else 'decrease')

#df1['cmpr'] = df1.assign(cmpr = lambda x: x[['vaule', 'pre']].apply(lambda y: 'increase' if y.value > y.pre else 'crease' ))

df1['cmp'] = np.where(df1.value > df1.pre, 'increase', np.where(df1.value == df1.pre, 'no change', 'decrease'))

df1
