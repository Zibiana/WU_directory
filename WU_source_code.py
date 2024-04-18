import streamlit as st
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

st.set_page_config(page_title="WU Directory", layout="wide")
st.title('Directory at Westminster University')
st.write("This is an enhanced alternatives to the employee [directory](https://westminsteru.edu/campus-directory/index.html) at Westminster University.")

#Fixing the data
data = pd.read_csv('WU_directory.csv') 
data.loc[57]["Contract"]="FULL-TIME"
data.loc[57]["Role"]="Faculty"
data.loc[57]["Title"]="Associate Professor"


department = st.selectbox(label = 'Choose one department from below:', options = np.insert(np.sort(data["Department"].unique()),0,"All Departments"))
st.write('You selected:', department)

#filter data by the choice
if department != "All Departments":
    #option 1: Using a mask:
#    mask=data["Department"]==department
#    data=data[mask]
    data = data.query("Department== '{}'".format(department))



col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Role:") # add a text 
    st.text("Type of Contract:") # add a text 

with col2:
    role_faculty = st.checkbox('Faculty', value=1) # default value is checked. 
    role_full_time = st.checkbox('FULL-TIME', value=1) # default value is checked. 

with col3:
    role_staff = st.checkbox('Staff', value=1) # default value is checked. 
    role_part_time = st.checkbox('PART-TIME', value=1) # default value is checked. 



 
col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Professor Title:") # add a text 
with col2:
    title_assistant = st.checkbox('Assistant Professor', value=1) # default value is checked. 

with col3:
    title_associate = st.checkbox('Associate Professor', value=1) # default value is checked. 
 
with col4:
    title_full = st.checkbox('Full', value=1) # default value is checked. 

col1, col2 = st.columns([0.5,.5])
with col1:
    name = st.text_input('Name')
    if name:
        st.write('Thy name is', name)
with col2:
    reg_ex= st.checkbox("Regular Expression", value=0)


############################################################################################
###################################### all the conditionals ###############################
############################################################################################


if role_faculty==False:
    data = data.query("Role!='Faculty'")

if role_staff==False:
    data = data.query("Role!='Staff'")



if role_full_time==False:
    data = data.query("Contract!='FULL-TIME'")

if role_part_time==False:
    data = data.query("Contract!='PART-TIME'")


#Add checkboxes for assistant professor, associate professor, and professor



if not title_assistant:
    mask_assist=data["Title"].str.contains("Assistant Professor")
    data = data[~mask_assist]
    #data.query("Title!='Assistant Professor'")

if not title_associate:
    mask_assoc=data["Title"].str.contains("Associate Professor")
    data = data[~mask_assoc]
    #data = data.query("Title!='Associate Professor'")

if not title_full:
    mask=data["Title"].str.contains("^Professor") 
    data=data[~mask]

#Add a textbox for naming searching. The searching is not case sensitive when re is not turned on.


if name:
    if reg_ex==True:
        data=data[data["Name"].str.contains(name, regex=True)]
    else:
        data=data[data["Name"].str.contains(name,regex=False)]    



#Add a checkbox of regular expression. If it is checked, the textbox starts accepting regular expression.
#

st.dataframe(data, hide_index=True) #hide_index deletes the index stamps








##### Screwing around down here
#data2 = pd.read_csv('SJ_education_resources.csv') 
#st.dataframe(data2, hide_index=True)

