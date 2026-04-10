import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

#DATA CLEANING.........

#print(df.head())

#print(df.info())

#df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#df = df.dropna()

df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
#print(df.head())

#df = df.drop('customerID', axis=1)
#print(df.size)
#print(df.shape)

#BASIC ANALYSIS........

total_customers = len(df)
churn_rate = df['Churn'].mean() * 100

print("Total Customers:", total_customers)
#print("Churn Rate: {:.2f}%".format(churn_rate))

#EXPLORATORY DATA ANALYSIS........

"""sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
#plt.show()

sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.xticks(rotation=20)
#plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Churn vs Monthly Charges")
plt.show()

sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Churn vs Tenure")
plt.show()"""

#ADVANCED ANALYSIS.........

#print(df.groupby('Contract')['Churn'].mean())

df['tenure_group'] = pd.cut(df['tenure'],
                           bins=[0,12,24,48,72],
                           labels=['0-1yr','1-2yr','2-4yr','4-6yr'])
print(df.shape)
#print(df.head())

#print(df.groupby('tenure_group')['Churn'].mean())

#print(df.groupby('PaymentMethod')['Churn'].mean())

df.to_csv("cleaned_churn_data.csv", index=False)

