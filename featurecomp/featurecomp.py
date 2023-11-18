import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image



ch = {
    'chart': ['bar', 'line', 'scatter', 'box', 'histogram', 'pie'],
}

ch = pd.DataFrame(ch)

st.title("EV car Comparisons")
df = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")
sliced_df = df.drop('Name', axis=1)



user_input_text_1 = st.multiselect("Select Car Types", df['Name'].unique())
user_input_text_2 = st.selectbox("Select Parameter", sliced_df.columns)
selected_chart = st.selectbox("Select Chart Type", ch['chart'].unique())


if st.button("Generate chart"):
    # Filter the DataFrame based on selected car types
    filtered_df = df[df['Name'].isin(user_input_text_1)]

    # Create chart based on the selected type
    if selected_chart == 'histogram':
        fig = px.histogram(filtered_df, x=user_input_text_2, labels={'x': 'X-axis'}, title='Histogram comparison')
    else:
        if selected_chart == 'bar':
            fig = px.bar(filtered_df, x='Name', y=user_input_text_2, labels={'x': 'Car Type', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'line':
            fig = px.line(filtered_df, x='Name', y=user_input_text_2, labels={'x': 'Car Type', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'scatter':
            fig = px.scatter(filtered_df, x='Name', y=user_input_text_2, labels={'x': 'Car Type', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'box':
            fig = px.box(filtered_df, x='Name', y=user_input_text_2, labels={'x': 'Car Type', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'pie':
            fig = px.pie(filtered_df, names='Name', values=user_input_text_2, labels={'x': 'Car Type'}, title='Comparison')

    # Display the chart
    st.plotly_chart(fig)
