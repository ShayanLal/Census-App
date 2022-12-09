import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():

	data_file = "adult.csv"
	df = pd.read_csv(data_file, header=None)

	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	df.head()


	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	df.dropna(inplace=True)

	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)
# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title("Census Data Visualization App")
st.sidebar.title("Exploratory Data Analysis")
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox('Show raw data'):
  st.subheader('Census Data set')
  st.dataframe(census_df)
  st.write(f"Number of rows: {census_df.shape[0]}")
  st.write(f"Number of columns: {census_df.shape[1]}")

# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualisation Selector")

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_list = st.sidebar.multiselect('Select the charts or plots:', ('Box Plot', 'Count Plot', 'Pie Chart'))

# Display pie plot using matplotlib module and 'st.pyplot()'
if 'Pie Chart' in plot_list:
  st.subheader('Pie Chart')
  
  plt.figure(figsize = (15, 10))
  income_counts = census_df['income'].value_counts()
  plt.pie(income_counts, labels = income_counts.index, autopct = '%.2f%%', explode = [.05, .05])
  plt.title("Distribution of records for different income groups")
  st.pyplot()

  plt.figure(figsize = (15, 10))
  gender_counts = census_df['gender'].value_counts()
  plt.pie(gender_counts, labels = gender_counts.index, autopct = '%.2f%%', explode = [.05, .05])
  plt.title("Distribution of records for different gender groups")
  st.pyplot()
# Display box 
# Display box plot using matplotlib module and 'st.pyplot()'
if 'Box Plot' in plot_list:
  st.subheader('Box Plot for the Hours Worked Per Week')

  plt.figure(figsize = (15,10))
  plt.title(f'Distribution of hours worked per week for different income groups')
  sns.boxplot(census_df['hours-per-week'], census_df['income'])
  st.pyplot()

  plt.figure(figsize = (15,10))
  plt.title(f'Distribution of hours worked per week for different gender groups')
  sns.boxplot(census_df['hours-per-week'], census_df['gender'])
  st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if 'Count Plot' in plot_list:
  st.subheader('Count plot for the distribution of records for unique work class groups')
  plt.figure(figsize = (15,10))
  sns.countplot(census_df['workclass'])
  st.pyplot()

