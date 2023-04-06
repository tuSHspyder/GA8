import pandas as pd
import streamlit as st

st.header('GA8')

with st.echo(code_location='below'):
  number1 = st.number_input('Insert a number 1')
  number2 = st.number_input('Insert a number 2')
  number3 = st.number_input('Insert a number 3')

  max_val = max(number1, number2, number3)
  
  st.text('The largest among the 3 given numbers is:')
  st.write(max_val)
