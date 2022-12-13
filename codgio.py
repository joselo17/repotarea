import streamlit as st
st.write("""# PRUEBA MUNDO MI PODER""")

for f in range(1,11):
	print(f,end=" ")
	
st.write("""# texto para probar app""")

import mymodel as m
st.write(m.run(window=15))
