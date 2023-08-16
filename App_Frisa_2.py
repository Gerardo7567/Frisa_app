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

name_label = 'Nombre'
flastname_label = 'Apellido Paterno'
slastname_label = 'Apellido Materno'
mail_label = 'Correo Electronico'
phone_label = 'Telefono'
type_label = 'Convocatoria'
button_label = 'Submit'

with st.sidebar:
    form = st.form(key='form1',clear_on_submit=True)
    add_name = form.text_input(label=f"{name_label}",value="input 1 name")
    add_flastname = form.text_input(label=f"{flastname_label}")
    add_slastname = form.text_input(label=f"{slastname_label}")
    add_mail = form.text_input(label=f"{mail_label}")
    add_phone = form.text_input(label=f"{phone_label}")
    add_type = form.text_input(label=f"{type_label}")
    button_press = form.form_submit_button(label=f"{button_label}")

    if button_press:
        new_data = {'Nombre':add_name,'Apellido Paterno':add_flastname,'Apellido Materno':add_slastname,
                    'Correo Electronico':add_mail,'Telefono':add_phone,'Convocatoria':add_type}
        new_row = pd.Series(new_data)
        #df.append(new_row, ignore_index=True)
        df.loc[len(df)] = new_data
        #Nombre del archivo dentro del GitHub para actualizarlo
        df.to_csv('Prueba_de_datos.csv',index=False)

st.write(df)
