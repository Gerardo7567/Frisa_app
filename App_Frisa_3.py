import streamlit as st
def intro():
    import streamlit as st

    st.write("# :man-woman-boy-boy: :earth_americas: Bienvenido a Fundación FRISA! 👋")
    st.sidebar.success("Selecione una pestaña.")

    st.markdown(
        """
        **Mision:**
        Somos una fundación empresarial dedicada a descubrir
        e impulsar proyectos que promueven la movilidad social 
        compartiendo el éxito de la compañía.

        **Vision:**
        Las comunidades donde opera FRISA son prósperas y 
        generadoras de oportunidades de todos y para todos.

        ### Quieres saber más?

        - Check out [Fundacion Frisa](http://www.fundacionfrisa.org/)
        - Jump into our [Voluntariado](http://www.fundacionfrisa.org/voluntariado-frisa/)
        - Ask a question in our [Convocatoria](http://www.fundacionfrisa.org/convocatoria/)
    """
    )
def Ingresar_datos():
    import pandas as pd
    import numpy as np
    import streamlit as st

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")

    fl = st.file_uploader(':file uploader: Sube un archivo',type=(["csv","txt","xlsx","xls"]))

    if fl is not None:
        filename = fl.name
        #st.write(filename)
        df = pd.read_csv(filename)
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
        new_data = {'Nombre': str(user_name),"Apellido paterno":str(user_flastname),"Apellido materno":str(user_slastname),
                    "Correo Electronico":str(user_mail),"Telefono":int(user_phone),"Tipo de Convocatoria":str(user_type)}
        new_row = pd.Series(new_data)
        #df.append(new_row, ignore_index=True)
        df.loc[len(df)] = new_data
        #Nombre del archivo dentro del GitHub para actualizarlo
        df.to_csv('Prueba_de_datos.csv',index=False)
    # Agregar el botón de descarga del archivo CSV actualizado
        df = pd.DataFrame(df)
    if not df.empty:
        csv_filename = 'Prueba_de_datos_actualizado.csv'
        csv_data = df.to_csv(index=False,encoding = 'latin1')
        st.download_button(label="Descargar CSV Actualizado", data=csv_data, file_name=csv_filename)


page_names_to_funcs = {
    "Inicio": intro,
    "Ingresar datos": Ingresar_datos
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
