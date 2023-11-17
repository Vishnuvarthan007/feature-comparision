import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
ch = {
    'chart': ['bar', 'line', 'scatter', 'box', 'histogram', 'pie'],
}
ch = pd.DataFrame(ch)
st.title("EV Comparisons")
df = pd.read_csv("featurecomp/Cheapestelectriccars-EVDatabase.csv")
user_input_text_1 = st.multiselect("Select Car Types", df['Name'].unique())
user_input_text_2 = st.selectbox("Select Parameter", df.columns)
selected_chart = st.selectbox("Select Chart Type", ch['chart'].unique())
if st.button("Generate chart"):
    filtered_df = df[df['Name'].isin(user_input_text_1)]
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
    st.plotly_chart(fig)
