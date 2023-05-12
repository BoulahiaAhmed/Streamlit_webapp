import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


"""
streamlit
psycopg2-binary
numpy
pandas
plotly
"""

# add /?embedded=true for the iframe link to host streamlit Community Cloud apps on Personal website



# HOSTED CODE ON GITHUB STARTS FROM HERE


url = 'https://raw.githubusercontent.com/BoulahiaAhmed/Streamlit_webapp/main/table2.csv'
result_df = pd.read_csv(url)


#Streamlit App


st.write("APP WITH STATIC DATA")

st.write("Our first attempt at using data to create a table:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(result_df)



# simple Graph

fig = px.bar(result_df, x='phase', y='num_sponsor')
st.plotly_chart(fig, use_container_width=True)




x = st.slider('input')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

if st.checkbox('Show dataframe'):
    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option    


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")





# Hide settings and "made with streamlit" label from users
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)









