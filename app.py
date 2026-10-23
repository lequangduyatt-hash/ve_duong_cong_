import streamlit as st
import numpy as np
st.set_page_config(page_title="Vẽ Vết HHVP")
import plotly.graph_objects as go
from sympy import symbols, lambdify

st.title("DUY IU BÉ VÂN")
st.write("Dựa trên định nghĩa $c(t)$ trong Không gian $\mathbb{R}^2$ và $\mathbb{R}^3$")

# Chọn không gian
khong_gian = st.radio("Chọn không gian tọa độ:", ["R^2 (Mặt phẳng)", "R^3 (Không gian)"])

# Giao diện nhập tham số t
col1, col2 = st.columns(2)
t_min = col1.number_input("Giá trị t nhỏ nhất (a)", value=-5.0)
t_max = col2.number_input("Giá trị t lớn nhất (b)", value=5.0)

t_sym = symbols('t')
t_vals = np.linspace(t_min, t_max, 1000)

try:
    if khong_gian == "R^2 (Mặt phẳng)":
        x_str = st.text_input("Tọa độ x(t):", "t**2 - 4")
        y_str = st.text_input("Tọa độ y(t):", "t**3 - 4*t")
        
        # Chuyển chuỗi toán học thành hàm số
        func_x = lambdify(t_sym, x_str, "numpy")
        func_y = lambdify(t_sym, y_str, "numpy")
        
        x_vals = func_x(t_vals)
        y_vals = func_y(t_vals)
        
        fig = go.Figure(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Vết (C)'))
        fig.update_layout(width=700, height=700)
        st.plotly_chart(fig)

    else:
        x_str = st.text_input("Tọa độ x(t):", "sin(t)")
        y_str = st.text_input("Tọa độ y(t):", "cos(t)")
        z_str = st.text_input("Tọa độ z(t):", "t")
        
        func_x = lambdify(t_sym, x_str, "numpy")
        func_y = lambdify(t_sym, y_str, "numpy")
        func_z = lambdify(t_sym, z_str, "numpy")
        
        x_vals = func_x(t_vals)
        y_vals = func_y(t_vals)
        z_vals = func_z(t_vals)
        
        fig = go.Figure(go.Scatter3d(x=x_vals, y=y_vals, z=z_vals, mode='lines', line=dict(width=4, color='blue')))
        fig.update_layout(width=700, height=700)
        st.plotly_chart(fig)
        
except Exception as e:
    st.error("Có lỗi trong cú pháp toán học. Hãy dùng các phép toán cơ bản (ví dụ: `sin(t)`, `t**2`).")