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


    def save_results(results_df, button_press, kms_biked, location_visited):
        results_df.at[button_press, 'kms_biked'] = kms_biked
        results_df.at[button_press, 'location_visited'] = location_visited
        results_df.to_csv('bike_to_work.csv', index=None)
        return None
    
    @st.cache
    def load_data():
        # If this is your first run, create an empty csv file with
        # columns kms_biked and location_visited        
        fl = st.file_uploader(':file uploader: Sube un archivo',type=(["csv","txt","xlsx","xls"]))
        if fl is not None:
            filename = fl.name
            #st.write(filename)
            df = pd.read_csv(filename)
        return df

    options_form = st.form('options_form')
    # Crear los espacios para subor los datos
    user_name = options_form.text_input("Nombre")
    user_flastname = options_form.text_input("Apellido paterno")
    user_slastname = options_form.text_input("Apellido materno")
    user_mail = options_form.text_input("Correo Electronico")
    user_phone = options_form.text_input("Telefono")
    user_type = options_form.text_input("Convocatoria")
    add_data = options_form.form_submit_button()
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
