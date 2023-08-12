

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
df = pd.read_csv("/content/starbucks_drinkMenu_expanded.csv")
df.head()

#storing the dataset into another data frame
df1=df.copy()
df1.info()

df1[' Total Fat (g)'].astype(str).astype(float)

df1["Caffeine (mg)"].replace(np.nan,df["Caffeine (mg)"].mode()[0],inplace=True)
df1["Caffeine (mg)"].isnull().sum()

df1.groupby("Beverage_category")["Calories"].mean()

df1['Beverage_category']=  df1["Beverage_category"].replace(["Frappuccino® Blended Coffee","Frappuccino® Blended Crème","Smoothies","Signature Espresso Drinks"],"High_calorie_drinks")
df1['Beverage_category'] = df1['Beverage_category'].replace(["Frappuccino® Light Blended Coffee","Shaken Iced Beverages","Tazo® Tea Drinks","Classic Espresso Drinks"],"Medium_calorie_drinks")
df1['Beverage_category'] = df1['Beverage_category'].replace(["Coffee"],"Low_calorie_drinks")

sns.countplot(x="Beverage_category",data=df1)

import scipy.stats as stats
df_hcal=df1[df1.Beverage_category=="High_calorie_drinks"]
calorie_values=df_hcal.Calories.tolist()
fat_of_hcal=np.array(df_hcal[' Total Fat (g)'])
df_mcal=df1[df1.Beverage_category=="Medium_calorie_drinks"]
fat_of_mcal=np.array(df_mcal[' Total Fat (g)'])
print(np.var(fat_of_hcal), np.var(fat_of_mcal))
#As you can see, the ratio is 10.104/6.902,
#which is less than 4:1. So we can say that the variances of the data groups are equal
print(stats.ttest_ind(fat_of_hcal,fat_of_mcal, equal_var=True))

from scipy.stats import t
fig, ax =plt.subplots (figsize= (8, 4))
dof = 236
x = np.linspace(t.ppf(0.01,dof),t.ppf(0.99,dof),1000)
ax.plot(x, t.pdf(x, dof),'r-',lw=5, alpha=0.9, label ='t pdf')
plt.axvline(x=t.ppf(0.05, dof), label='Critical value for alpha=0.1', color='g')
plt.axvline(x=t.ppf(0.95, dof), label='Critical value for alpha=0.1', color='g')
plt.axvline (3.485276427350298, label='t-test score')
plt.legend ()
plt.ylim(0, 0.5)
plt.plot ( )

sns.distplot(df_hcal['Calories'],hist = False, kde = True, label='high calorie drink')

from scipy.stats import skew
from scipy.stats import skewtest
from scipy.stats import kurtosis
print(skew(calorie_values, axis=0, bias=True))
print(kurtosis(calorie_values, axis=0, bias=True))
print(skewtest(calorie_values))

import statsmodels.api as sm
import pylab as py
import statistics
from scipy.stats import norm
t=np.linspace(0.01,0.99,1000)
q1=np.quantile(calorie_values,t)
q2=norm.ppf(t,loc=np.mean(calorie_values),scale=np.std(calorie_values))
plt.plot(q1,q2)
plt.plot([min(q1),max(q1)],[min(q2),max(q2)])
plt.xlim((min(q1),max(q1)))
plt.ylim((min(q2),max(q2)))
plt.xlabel("calories")
plt.ylabel("nd")
plt.show()

from scipy.stats import shapiro #Shapiro-Wilk test is a test of normality, it determines whether the given sample comes from the normal distribution or not. Shapiro-Wilk’s test or Shapiro test is a normality test in frequentist statistics.
shapiro(calorie_values)

import scipy.stats as stats
from statistics import mean
print(mean(calorie_values))
stats.ttest_1samp(calorie_values,280)

"""Accept the null hypothesis"""

df1.info()

df1.groupby("Beverage_prep")[" Total Fat (g)"].mean()

df1['Beverage_prep']=  df1["Beverage_prep"].replace(["2% Milk","Whole Milk","Soymilk"],"High_fat_drinks")
df1['Beverage_prep'] = df1['Beverage_prep'].replace(["Short Nonfat Milk","Tall Nonfat Milk","Venti Nonfat Milk","Grande Nonfat Milk"],"medium_fat_drinks")
df1['Beverage_prep'] = df1['Beverage_prep'].replace(["Doppio","Grande","Short","Tall","Venti","Solo"],"Low_fat_drinks")
df1

sns.countplot(x="Beverage_prep",data=df1)

df1["Beverage_prep"].unique()

import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('Calories~ C(Beverage_prep) + C(Beverage_category) + C(Beverage_prep):C(Beverage_category)', data=df1).fit()
sm.stats.anova_lm(model, typ=2)

from scipy.stats import chi2_contingency
from scipy.stats import chi2
chisqt = pd.crosstab(df1.Beverage_prep, df1.Beverage_category, margins=True)
value = np.array([chisqt.iloc[0][0:5].values,
                  chisqt.iloc[1][0:5].values])
print(chi2_contingency(value)[0:3])



# plotting correlation heatmap
dataplot = sns.heatmap(df1.corr(), cmap="Blues", annot=True)


# displaying heatmap
plt.show()

df1["Beverage"].unique()