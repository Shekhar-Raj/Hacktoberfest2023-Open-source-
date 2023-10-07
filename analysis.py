dataset link --> /kaggle/input/diwali-sales-data/Diwali Sales Data.csv

CODE :
//Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

df=pd.read_csv("/kaggle/input/diwali-sales-data/Diwali Sales Data.csv",encoding= 'unicode_escape')
df.head()

df.shape

df.isnull().sum()

df.info()

#Dropping the null rows

df.drop(['Status','unnamed1'],axis=1,inplace=True)

df.isnull().sum()

df.shape

df.dropna(inplace=True)

df.shape

df['Amount']=df['Amount'].astype('int')

# The amount of data type float has been converted into int data type.
df['Amount'].dtypes

df.columns

df.describe()

df[['Age','Orders','Amount']].describe()

##EXPLORATORY DATA ANALYSIS

ax=sns.countplot(x="Gender",data=df)
for bars in ax.containers:
    ax.bar_label(bars)

df.groupby(["Gender"],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

df.groupby("Gender").sum()["Amount"].plot(kind="pie",autopct="%.2f")

## AGE

df['Age'].nunique()

ax=sns.countplot(data=df,x='Age Group',hue="Gender")
for bars in ax.containers:
    ax.bar_label(bars)
plt.legend=True

sales_age=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False)
sns.barplot(x='Age Group',y='Amount',data=sales_age)

#Total Amount/Sales from top 10 states
sales_state=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False).head(10)
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(x='State',y='Amount',data=sales_state)

#Total number of orders from top 10 states
sales_state=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending =False).head(10)
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(x='State',y='Orders',data=sales_state)

df.columns

df.groupby("Marital_Status").size().plot(kind='pie',autopct='%0.2f')

ax=sns.countplot(data=df,x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.legend=True

#Total Amount/Sales from top 10 states
sales_marital=df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False).head(10)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(x='Marital_Status',y='Amount',hue='Gender',data=sales_marital)


##OCCUPATION

sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.legend=True

sales_occupation=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Occupation',y='Amount',data=sales_occupation)

##PRODUCT CATEGORY

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)

sales_product = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_product, x = 'Product_Category',y= 'Amount')

sales_pid = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_pid, x = 'Product_ID',y= 'Orders')

# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

##CONCLUSION

##Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
