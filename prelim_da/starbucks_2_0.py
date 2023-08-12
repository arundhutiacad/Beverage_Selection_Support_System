

url = 'https://drive.google.com/file/d/1UbWXvQmXAPpOPzkhHgLc2PXKG19kgBs4/view?usp=share_link'
file_id = url.split('/')[-2]
read_url='https://drive.google.com/uc?id=' + file_id

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline


#importing libraries for machine learning
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

df = pd.read_csv(read_url)
df.head()

df.info()

df = df.dropna()

model = ols('Calories ~ Beverage_prep', data=df).fit()
sm.stats.anova_lm(model, typ=2)

"""DEPENDENT"""

df["Beverage_prep"].unique()

df_short=df.loc[df.Beverage_prep == 'Short']
df_tall=df.loc[df.Beverage_prep == 'Tall']

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

df.head(1)

df.columns

x = df[['Saturated Fat (g)'," Dietary Fibre (g)",' Sodium (mg)',"Calories"," Protein (g) "]]
y=df["Beverage_prep"]

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=42)

st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)

classifier= RandomForestClassifier(n_estimators= 75, criterion="entropy")
classifier.fit(x_train, y_train)

y_pred= classifier.predict(x_test)

cm= confusion_matrix(y_test, y_pred)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

svm = SVC()
svm.fit(x_train, y_train)

y_pred = svm.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Create a Naive Bayes classifier
naive_bayes = GaussianNB()

# Train the model
naive_bayes.fit(x_train, y_train)

# Make predictions on the test set
y_pred = naive_bayes.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
clf = DecisionTreeClassifier()

# Fitting the model on the training data
clf.fit(x_train, y_train)

# Making predictions on the test set
y_pred = clf.predict(x_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create and fit the logistic regression model
logreg = LogisticRegression()
logreg.fit(x_train, y_train)

# Predict on the test set
y_pred = logreg.predict(x_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)