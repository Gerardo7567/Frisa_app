import streamlit as st
#import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title='Fundacion Frisa',page_icon=':man-woman-boy-boy:',layout='wide')

st.title(' :man-woman-boy-boy: 	:earth_americas: Fundacion Frisa')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(':file uploader: Sube un archivo',type=(["csv","txt","xlsx","xls"]))

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename)
else:
    #Nombre del archivo dentro del GitHub
    df = pd.read_csv('Prueba_de_datos.csv')

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
    new_data = pd.DataFrame({'Nombre': user_name,"Apellido paterno":user_flastname,"Apellido materno":user_slastname,
                "Correo Electronico":user_mail,"Telefono":int(user_phone),"Convocatoria":user_type})
    df = df.append(pd.DataFrame([new_data],columns=df.columns))
    #df = pd.concat([new_data,df.loc[:]]).reset_index(drop=True)
    #df = df.append(new_data, ignore_index=True)
    #Nombre del archivo dentro del GitHub para actualizarlo
    df.to_csv('Prueba_de_datos.csv',index=False)
