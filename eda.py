# importing packages

import streamlit as st 
import pandas as pd
from PIL import Image 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def eda():
	df = pd.read_csv("heart.csv")
	dt = pd.read_csv("renamed_data.csv")

	submenu = ["Descriptive", "Plots"]
	choice = st.sidebar.selectbox("Submenu", submenu)

	if choice == "Descriptive":
		st.subheader("This is our data")
		st.dataframe(df)

		st.subheader("Here are the statistical values for all the numerical columns")
		st.dataframe(df.describe())

		col1, col2 = st.columns(2)

		with col1: 
			st.subheader("Data Types")
			st.dataframe(df.dtypes)

		with col2:
			st.subheader("Basic Information about the data")
			img = Image.open("info.jpeg")
			st.image(img)


		col3, col4  = st.columns(2)

		with col3:
			with st.expander("Column Sex"):
				st.dataframe(dt["sex"].value_counts())
		
		with col4:
			with st.expander("Rest ECG"):
				st.dataframe(dt['rest_ecg'].value_counts())


		col5, col6  = st.columns(2)
			
		with col5:
			with st.expander("Chest Pain Type"):
				st.dataframe(dt['chest_pain_type'].value_counts())

		with col6:
			with st.expander("Slope"):
				st.dataframe(dt['st_slope'].value_counts())


		

		
	
	else:

		i = Image.open("plots.jpeg")
		st.image(i)

		with st.expander("EDA Information"):

			st.write("""

# EDA Using Plots 

Data visualization is the graphical representation of information and data. By using visual elements 
like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, 
outliers, and patterns in data.

### Count plots and Bar Plots

A countplot is kind of likea histogram or a bar graph for some categorical area. It simply shows the number 
of occurrences of an item based on a certain type of category.

A barplot (or barchart) is one of the most common types of graphic. It shows the relationship between a 
numeric and a categoric variable. Each entity of the categoric variable is represented as a bar. The size of the bar represents its numeric value.

### Pie Chart

A pie chart shows how some total amount is divided among distinct categories as a circle
 (the namesake pie) divided into radial slices. Each category is associated with a single slice whose 
 size corresponds with the category's proportion of the total.

### KDE Plots

A density plot is a representation of the distribution of a numeric variable. It uses a kernel density 
estimate to show the probability density function of the variable (see more). It is a smoothed version of 
the histogram and is used in the same concept.

### Scatter Plot

A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a 
type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables 
for a set of data.

### Box Plot

In descriptive statistics, a box plot or boxplot is a method for graphically depicting groups of numerical data
 through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability
  outside the upper and lower quartiles

### Heat Maps

A heat map (or heatmap) is a data visualization technique that shows magnitude of a phenomenon as color in 
two dimensions. The variation in color may be by hue or intensity, giving obvious visual cues to the reader 
about how the phenomenon is clustered or varies over space.

### Pair Plot

Pair Plots are a really simple (one-line-of-code simple!) way to visualize relationships between each variable.
It produces a matrix of relationships between each variable in your data for an instant examination of our data.
It can also be a great jumping off point for determining types of regression analysis to use

# The Visualization Plots

""")











		with st.expander("Based on Column Target"):
			choose = st.selectbox("Choose the plot you want to view", ["Target", "Target wrt SEX",
				"Target wrt Fasting Blood Sugar", "Target wrt Exercise induced angina"])


			if choose == "Target":
				a = px.histogram(dt, x = "target", color = "target")
				st.plotly_chart(a)

			elif choose == "Target wrt SEX":
				b = px.histogram(dt, x = "target", color = "sex", barmode = "group")
				st.plotly_chart(b)

			elif choose == "Target wrt Fasting Blood Sugar":
				c = px.histogram(dt, x = "target", color = "fasting_blood_sugar")
				st.plotly_chart(c)

			elif choose == "Target wrt Exercise induced angina":
				d = px.histogram(dt, x = "target", color = "exercise_induced_angina", barmode = "group")
				st.plotly_chart(d)
		

		
		with st.expander("Frequency Distibution Plots"):
			choose = st.selectbox("Choose the plot you want to view", ["Based on Chest Pain Type", 
	    		"Based on the Maximum heart rate achieved", "Based on the Age"])

			if choose == "Based on Chest Pain Type":
				e = px.pie(dt, names = "chest_pain_type")
				st.plotly_chart(e)

			elif choose == "Based on the Maximum heart rate achieved":
				f, ax = plt.subplots(figsize = (10,8))
				ax = sns.distplot(dt["max_heart_rate_achieved"], bins = 10)
				st.pyplot(f)

			elif choose == "Based on the Age":
				g, ax = plt.subplots(figsize = (10,8))
				ax = sns.distplot(dt["age"], bins = 10, color = "red")
				st.pyplot(g)
			
		with st.expander("Scatter Plots"):
			choose = st.selectbox("Choose the plot you want to view", ["Age vs Resting Blood Pressure", 
	    		"Age vs Cholestrol", "Cholestrol vs Maximum heart rate achieved"])

			if choose == "Age vs Resting Blood Pressure":
				h, ax = plt.subplots(figsize = (10,8))
				ax = sns.scatterplot(x = "age", y = "resting_blood_pressure", data = dt)
				st.pyplot(h)

			elif choose == "Age vs Cholestrol":
				i = px.scatter(dt, x = "age", y = "cholesterol")
				st.plotly_chart(i)

			elif choose == "Cholestrol vs Maximum heart rate achieved":
				j = plt.figure()
				plt.scatter(dt["cholesterol"], dt["max_heart_rate_achieved"])
				st.pyplot(j)

		with st.expander("Outlier Detection"):
			choose = st.selectbox("Choose the plot you want to view", ["Age", "Resting blood Pressure", 
	    		"Cholestrol", "Maximum Heart rate achieved", "St_depression"])

			if choose == "Age":
				k = px.box(dt, x = "age")
				st.plotly_chart(k)

			elif choose == "Resting blood Pressure":
				l = plt.figure()
				sns.boxplot(dt["resting_blood_pressure"])
				st.pyplot(l)

			elif choose == "Cholestrol":
				m = plt.figure()
				plt.boxplot(dt["cholesterol"])
				st.pyplot(m)

			elif choose == "Maximum Heart rate achieved":
				n = px.box(dt, x = "max_heart_rate_achieved")
				st.plotly_chart(n)

			else:
				o = plt.figure()
				sns.boxplot(dt["st_depression"])
				st.pyplot(o)

		with st.expander("HatMaps and PairPlots"):
	    	
			choose = st.selectbox("Choose the plot you want to view", ["Heat Map", "Pair Plot"])

			if choose == "Heat Map":
				cor = df.corr()
				p = px.imshow(cor)
				st.plotly_chart(p)

			else:
				img = Image.open("pairplot.jpeg")
				st.image(img)