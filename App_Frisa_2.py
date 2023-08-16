import streamlit as st
#import plotly.express as px
import pandas as pd
import warnings

st.set_page_config(page_title='Fundacion Frisa',page_icon=':man-woman-boy-boy:',layout='wide')

st.title(' :man-woman-boy-boy: 	:earth_americas: Fundacion Frisa')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(':file uploader: Sube un archivo',type=(["csv","txt","xlsx","xls"]))
sidebar = st.sidebar
@st.cache
def load_data():
    df = pd.read_csv(filename)
    return df
df = load_data()

st.header("Dataset")
agree = sidebar.checkbox("Quieres ver la base de datos ? ")
if agree:
    st.dataframe(df)

if fl is not None:
    filename = fl.name
    #st.write(filename)
    df = pd.read_csv(filename)
#else:
    #Nombre del archivo dentro del GitHub
    #df = pd.read_csv('Prueba_de_datos.csv')

st.header('Archivo existente')
st.write(df)

st.sidebar.header('Opciones')
options_form = st.sidebar.form('options_form')
# Crear los espacios para subor los datos
user_name = options_form.text_input("Nombre")
user_flastname = options_form.text_input("Apellido paterno")
user_slastname = options_form.text_input("Apellido materno")
user_mail = options_form.text_input("Correo Electronico")
user_phone = options_form.text_input("Telefono")
user_type = options_form.text_input("Convocatoria")
add_data = options_form.form_submit_button()
if add_data:
    #cada variable nueva con la columna donde ira
    new_data = {'Nombre': user_name,"Apellido paterno":user_flastname,"Apellido materno":user_slastname,
                "Correo Electronico":user_mail,"Telefono":int(user_phone),"Convocatoria":user_type}
    new_row = pd.Series(new_data)
    #df.append(new_row, ignore_index=True)
    df.loc[len(df)] = new_data
    #Nombre del archivo dentro del GitHub para actualizarlo
    df.to_csv('Prueba_de_datos.csv',index=False)
st.write(df)
