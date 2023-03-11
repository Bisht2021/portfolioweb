import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg",width= 450)

with col2:
    st.title("Prateek Bisht")
    content="""
    Hello ! My name is Prateek Bisht I have Graduated from Global Institute of Technology stream ECE in year 2014.
    Now I started learning Python and bulid some Small projects on Python.
    In This page you can see My all projects and aLso please give me suggestion for my projects.
    """
    st.info(content)

st.write("Below are some of my apps you can find. please free to contact me:. I will aso bulid some apps for youe ")
col3,empty_col,col4= st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[source code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")
