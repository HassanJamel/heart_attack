# 1: Import library

import streamlit as st 
from PIL import Image

# 1.1: Importing the files
from eda import eda
from ml import ml

# 2: Create mnue

def main():

	

	menu = ["Home","Exploratery Data Analysis","Predection Section","About"]

	choes = st.sidebar.selectbox("Menu",menu)

	if choes =="Home":
		# st.header("This is our Home page")
		img = Image.open("heart.jpeg")
		st.image(img)

		st.title("This is the Heart Attack App")

		st.write("""
		The data that we use in this particular app contain the features of a newly heart disease patient 
		or a diabetic patient.

		### DataScource

		- https://archive.ics.uci.edu/ml/datasets/heart+disease

		### App Content

		- This app has four sections
		1) Home Page - The page you are currently in

		2) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

		3) Prediction- The page in which you will be asked to give the information on all the medical aspects
		and we will predict the desired the output

		4) About - This Page is about me

			""")

	elif choes =="Exploratery Data Analysis":
		eda()
	elif choes =="Predection Section":
		ml()
	


	else:
		st.subheader("Hassan Jameel - Senior Data Analyst @ Sizal Group Company | Artificial Intelligence | Data Science | Machine Learning | Deep Learning | Master, Data Science")

		img = Image.open("hassanj.PNG")
		st.image(img)

		st.text("""
		• 18+ years of experience in the Implementation of different types of
		systems such as Odoo, Oracle Fusion, Microsoft Dynamic Ax, Infor,
		Retail Pro, Foodex, and Magento in fields of ERP, Retail and POS, BI,
		Datawarehouse, and Data Analyst, ECommerce, Implementation and
		integration.

		""")
		

		expander = st.expander("My Contacts")
		expander.write('Email: hassan.j.a@hotmail.com')
		expander.write('Phone: 0509684720')
		expander.write('Linkedin : https://www.linkedin.com/in/hassanjameel')
		expander.write('Kaggle : https://www.kaggle.com/hassanjameelahmed')	

main()