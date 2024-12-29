# -*- coding: utf-8 -*-
"""E_Commarce_EDA_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DK5Y3b9W78PIS1yJOb7o1cpOwPAO1NuR
"""

import pandas as pd

# Try loading the dataset with a different encoding, like 'latin-1'
df = pd.read_csv('/content/E-Commerce Data.csv', encoding='latin-1')

# Display the first few rows
df.head()

# Shape of the dataset
print("Shape of the dataset:", df.shape)

# Info about the dataset
print("Info about the dataset:")
df.info()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Handling missing values
# For numerical columns, fill with mean
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# For categorical columns, fill with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify no missing values remain
print(df.isnull().sum())

# Descriptive statistics
df.describe()

# Print column names to find the correct column names for Price and Quantity
print("Column names:", df.columns)

# Plot histograms for all numerical columns
for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical columns:", categorical_cols)

# Bar plot for a categorical feature (example: 'Country')
plt.figure(figsize=(10, 6))
sns.countplot(y='Country', data=df, order=df['Country'].value_counts().index)
plt.title('Counts of Different Countries')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()

# Scatter plot for 'UnitPrice' vs 'Quantity'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='UnitPrice', y='Quantity', data=df)
plt.title('Unit Price vs Quantity')
plt.xlabel('Unit Price')
plt.ylabel('Quantity')
plt.show()

# Box plot (example: 'UnitPrice' distribution by 'Country')
plt.figure(figsize=(10, 6))
sns.boxplot(x='Country', y='UnitPrice', data=df)
plt.title('Unit Price Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Unit Price')
plt.xticks(rotation=90)
plt.show()

# Convert 'InvoiceDate' to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Set 'InvoiceDate' as the index
df.set_index('InvoiceDate', inplace=True)

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Line plot for a time series feature (example: total 'Quantity' over time)
plt.figure(figsize=(12, 6))
df['Quantity'].resample('M').sum().plot()
plt.title('Total Monthly Quantity')
plt.xlabel('Date')
plt.ylabel('Total Quantity')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 8))
# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

import pandas as pd

# Load data from a CSV file
# Replace 'your_data.csv' with the actual file path if it's in a different directory
# file_path = '/content/E-Commerce Data.csv'  # Update with the correct path
df = pd.read_csv('/content/E-Commerce Data.csv', encoding='latin-1')

# Repeat Customers
repeat_customers = df.groupby('CustomerID').size().reset_index(name='Counts')
repeat_customers = repeat_customers[repeat_customers['Counts'] > 1]
total_customers = df['CustomerID'].nunique()
repeat_customers_percentage = (len(repeat_customers) / total_customers) * 100
print(f"Repeat Customers: {repeat_customers_percentage:.2f}% of total customers")