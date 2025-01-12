import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clean_data(data):
    data = data.drop_duplicates()
    data = data.ffill()
    return data

def visualize_data(data):
    numeric_cols = data.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
    plt.show()
