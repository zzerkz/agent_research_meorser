import pandas as pd
import statsmodels.formula.api as smf

##Reads csv file into a pandas dataframe and creates a new column 'Sport'
##1 if the 'Sport_NonSport' column is 'Sport', and 0 otherwise
##Serious is set as the reference category
df = pd.read_csv('~/Documents/Kalshi Data Sets/Processed final data - Sheet1.csv')
df['Sport'] = (df['Sport_NonSport'] == 'Sport').astype(int)
df['Category'] = pd.Categorical(df['Category'], categories={'Serious', 'Meme', 'Grey'})

##Model 1: Bivariate regression of volume on meme/grey
model_1 =smf.ols('Volume ~ C(Category)', data=df).fit()

##Model 2: Multivariate regression of sport/non-sport
##note: 0 of 121 Meme-category rows are sports bets, so the coefficent 
##is undefined (perfect separation) reported as N/A

in_meme_sport = df.loc[df['Category'] == 'Meme', 'Sport'].sum()
model_2 = smf.ols('Volume ~ C(Category) + Sport', data=df).fit()

##Model 3: Multivariate regression of market duration (days) on meme/grey and sport/non-sport
model_3 = smf.ols('Volume ~ C(Category) + Sport + market_duration_days', data=df).fit()

##Dislay large volume numbers in millions, e.g. 1.70M
def fmt_m(x):
    return f'{x/1e6:.2f}M' if abs(x) >= 1e6 else f'{x:,.0f}'

##Display everything in terminal in a organized manner
print(f'\n{"="*60}\nModel 1: Volume ~ Category\n{"="*60}')
print(model_1.summary())
print('\nCoefficients in plain terms:')
for label, val in model_1.params.items():
    print(f' {label}:{fmt_m(val)}')

print(f'\n{"="*60}\nModel 2: Sport ~ Category\n{"="*60}')
print(model_2.summary())
print(f'\nMeme coefficient: N/A ({in_meme_sport} of 121 meme rows are sports bets -- perfect separation)')

print(f'\n{"="*60}\nModel 3: Duration ~ Category + Sport\n{"="*60}')
print(model_3.summary())
      
                  