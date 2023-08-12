import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.decomposition import PCA
import pickle

# Load the dataset
df = pd.read_csv('starbucks_drinkMenu_expanded.csv')

# Preprocess the data
df = df.dropna()

df_short=df.loc[df.Beverage_prep == 'Short']
df_tall=df.loc[df.Beverage_prep == 'Tall']

# new pca analysis
df2= df[[' Total Fat (g)', 'Trans Fat (g) ', 'Saturated Fat (g)']]

pca = PCA(n_components=1)  # Specify the number of components you want after merging
merged_column= pca.fit_transform(df2)
df['Total Fat'] = merged_column

df3= df[[' Sugars (g)','Calories',' Total Carbohydrates (g) ']]

pca = PCA(n_components=1)  # Specify the number of components you want after merging
merged_column= pca.fit_transform(df3)
df['Calories'] = merged_column

df3= df[[' Sugars (g)','Calories',' Total Carbohydrates (g) ']]

x = df[['Total Fat'," Dietary Fibre (g)",' Sodium (mg)',"Calories"," Protein (g) "]]
y=df["Beverage_prep"]

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=42)

st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)

classifier= RandomForestClassifier(n_estimators= 75, criterion="entropy")
classifier.fit(x_train, y_train)

y_pred= classifier.predict(x_test)

# Save the trained model to disk
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(classifier, f)
