import streamlit as st
import plotly.graph_objects as go
import numpy as np
import math

def rotate_x(x, y, z, alpha):
    cos_alpha = math.cos(math.radians(alpha))
    sin_alpha = math.sin(math.radians(alpha))
    y_new = y * cos_alpha - z * sin_alpha
    z_new = y * sin_alpha + z * cos_alpha
    return x, y_new, z_new

def rotate_y(x, y, z, beta):
    cos_beta = math.cos(math.radians(beta))
    sin_beta = math.sin(math.radians(beta))
    x_new = x * cos_beta + z * sin_beta
    z_new = -x * sin_beta + z * cos_beta
    return x_new, y, z_new

def rotate_z(x, y, z, gamma):
    cos_gamma = math.cos(math.radians(gamma))
    sin_gamma = math.sin(math.radians(gamma))
    x_new = x * cos_gamma - y * sin_gamma
    y_new = x * sin_gamma + y * cos_gamma
    return x_new, y_new, z

def translate_coordinates(x, y, z, delta_x, delta_y, delta_z, delta_alpha=0, delta_beta=0, delta_gamma=0):
    x_new = x + delta_x
    y_new = y + delta_y
    z_new = z + delta_z

    x_new, y_new, z_new = rotate_x(x_new, y_new, z_new, delta_alpha)
    x_new, y_new, z_new = rotate_y(x_new, y_new, z_new, delta_beta)
    x_new, y_new, z_new = rotate_z(x_new, y_new, z_new, delta_gamma)

    return x_new, y_new, z_new

def plot_coordinates(x, y, z, system_name):
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=5))])
    fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    title=f'{system_name} Coordinate System',
                    margin=dict(l=0, r=0, b=0, t=40),
                    scene_aspectmode='cube')
    return fig

def main():
    st.title("Coordinate System Translation App")

    x = st.sidebar.number_input("X", value=10.0)
    y = st.sidebar.number_input("Y", value=5.0)
    z = st.sidebar.number_input("Z", value=2.0)
    alpha = st.sidebar.number_input("Alpha", value=30.0)
    beta = st.sidebar.number_input("Beta", value=45.0)
    gamma = st.sidebar.number_input("Gamma", value=60.0)

    delta_x = st.sidebar.number_input("Delta X", value=2.0)
    delta_y = st.sidebar.number_input("Delta Y", value=-1.0)
    delta_z = st.sidebar.number_input("Delta Z", value=0.5)
    delta_alpha = st.sidebar.number_input("Delta Alpha", value=5.0)
    delta_beta = st.sidebar.number_input("Delta Beta", value=-2.0)
    delta_gamma = st.sidebar.number_input("Delta Gamma", value=3.0)

    x_new, y_new, z_new = translate_coordinates(x, y, z, delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma)

    fig_primary = plot_coordinates([x], [y], [z], "Primary")
    fig_secondary = plot_coordinates([x_new], [y_new], [z_new], "Secondary")

    st.plotly_chart(fig_primary, use_container_width=True)
    st.plotly_chart(fig_secondary, use_container_width=True)

if __name__ == "__main__":
    main()
