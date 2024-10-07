# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:59:32 2024

@author: ratan.deshpande
"""
import streamlit as st
from sympy import symbols, Derivative, sin, cos, sympify, SympifyError, latex, simplify, diff, integrate, lambdify
import numpy as np


x, y = symbols('x y')
#Title of the App
st.title("Integral of a Function")
#Display text
st.write("This is simple app to generate integral of a given function defined by user")

expression_input = st.text_input("Enter a SymPy expression (in terms of x and y):", value="x**2 + y**2")
## Parsing the input expression into a SymPy object
try:
    expression = sympify(expression_input)
    st.write(f"Expression: {expression_input}")
except (SympifyError, ValueError):
    st.error("Invalid expression!")
    st.stop()

# Display the parsed expression using LaTeX (SymPy -> LaTeX -> Streamlit markdown)
st.latex(latex(expression))

# Perform some symbolic operations
st.write("Operations on the expression:")

# Simplify the expression
simplified_expr = simplify(expression)
st.write("Simplified Expression:")
st.latex(latex(simplified_expr))



# Take the integral with respect to y
integral_expr = integrate(expression, x)
st.write("Integral with respect to x:")
st.latex(latex(integral_expr))


# Title of the app
