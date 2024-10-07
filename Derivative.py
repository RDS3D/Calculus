# -*- coding: utf-8 -*-
"""


@author: ratan.deshpande

"""
import streamlit as st
from sympy import symbols, Derivative, sin, cos, sympify, SympifyError, latex, simplify, diff, integrate, lambdify
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols('x y')
#Title of the App
st.title("Derivative of a Function")
#Display text
st.write("This is simple app to generate derivative of a given function defined by user")

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

# Take the derivative with respect to x
derivative_expr = diff(expression, x)
st.write("Derivative with respect to x:")
st.latex(latex(derivative_expr))




# # Title of the app
# st.title("Matplotlib Plot in Streamlit")

# # Adding user inputs for plot parameters
# x_min = st.slider('x-axis minimum', -10, 0, -10)
# x_max = st.slider('x-axis maximum', 0, 10, 10)
# num_points = st.slider('Number of points', 10, 1000, 100)

# # Generating data
# x1 = np.linspace(x_min, x_max, num_points)
# y1 = lambdify(x,derivative_expr)
# y2 = y1(x1)
# y2 = y2.reshape((100,1))

# y_exp = lambdify(x,simplified_expr)
# y_exp = y_exp(x1)
# y_exp = y_exp.reshape((100,1))

# # Create a Matplotlib figure
# fig, ax = plt.subplots()
# ax.plot(x1, y2, label="Diff")

# ax.plot(x1, y_exp, label="Expr")
# ax.set_xlabel('x')
# ax.set_ylabel('Diff(x)')
# ax.set_title('Derivative')

# st.pyplot(fig)
