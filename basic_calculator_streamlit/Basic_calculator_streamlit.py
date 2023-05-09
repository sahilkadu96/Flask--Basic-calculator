import streamlit as st

st.title('Basic Calculator')
st.header('Operations of two numbers')

num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

if st.sidebar.button('Add'):
    res = num1 + num2
    st.write(f"Addition of two numbers is {res}")

if st.sidebar.button('Subtract'):
    res = num1 - num2
    st.write(f"Subtraction of two numbers is {res}")

if st.sidebar.button('Multiply'):
    res = num1*num2
    st.write(f"Multiplication of two numbers is {res}")

if st.sidebar.button('Divide'):
    if num2 == 0:
        st.error('Cannot divide by 0')
    else:
        res = num1/num2
        st.write(f"Division of two numbers is {res}")