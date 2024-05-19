import streamlit as st
first_number = st.number_input("Enter first number")
second_number= st.number_input("Enter second number")
st.write("Sum of two numbers is" , first_number +second_number)