# app.py

import streamlit as st
import plotly.graph_objects as go

def plot_3d_points(points_with_labels):
    x = [point[0] for point, label in points_with_labels]
    y = [point[1] for point, label in points_with_labels]
    z = [point[2] for point, label in points_with_labels]
    labels = [label for point, label in points_with_labels]

    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers+text', text=labels, textposition='top center')])
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

    st.write(fig)

def parse_input(input_text):
    lines = input_text.strip().split("\n")
    points_with_labels = []
    for line in lines:
        # ラベルと座標部分を分割
        parts = line.split("(")
        label = parts[0].strip()  # スペースやタブを取り除く
        point_str = parts[1].strip(")")
        x, y, z = map(float, point_str.split(","))
        points_with_labels.append(((x, y, z), label))
    return points_with_labels


def main():
    st.title("3D Points Visualization")

    user_input = st.text_area("Enter points as 'Label (x, y, z)' separated by new lines:")

    if st.button('Plot'):
        if user_input:
            points_with_labels = parse_input(user_input)
            plot_3d_points(points_with_labels)
        else:
            st.warning("Please enter valid points to plot.")

if __name__ == "__main__":
    main()
