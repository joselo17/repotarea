import streamlit as st
import mymodel as m
st.write("""# PRUEBA MUNDO MI PODER""")
st.write("""# texto para probar app""")
window=st.slider("heloo desliza")
st.write(m.run(window=window))
