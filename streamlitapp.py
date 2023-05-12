import streamlit as st
import numpy as np
import pandas as pd
#import plotly.express as px
import psycopg2

"""streamlit==1.22.0
psycopg2==2.9.6
numpy
pandas
plotly==5.14.1
"""
# add /?embedded=true for the iframe link to host streamlit Community Cloud apps on Personal website



# Connecting to PostgreSQL Data
# Establish server connection from the Toml file
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

con = init_connection()







# Uses st.cache_data to only rerun when the query changes or after 10 min (ttl=600). 
@st.cache_data(ttl=600)
def run_query(query):
    with con.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from sponsors WHERE  nct_id = 'NCT04900857';")


# Print results.
df_try = pd.DataFrame(rows)
st.table(df_try)








# Creating cursor object
cursor_obj = con.cursor()

# SQL Query
sql_query = """SELECT
  s.phase,
  COUNT(*) AS num_trials,
  AVG(s.enrollment) AS avg_enrollment,
  MAX(s.enrollment) AS max_enrollment,
  MIN(s.enrollment) AS min_enrollment,
  COUNT(DISTINCT sp.name) AS num_sponsors
FROM
  studies s
LEFT JOIN
  sponsors sp ON s.nct_id = sp.nct_id
GROUP BY
  s.phase;"""



# executing the query
cursor_obj.execute(sql_query)

# Fetching data
result = cursor_obj.fetchall()

# Creating Pands DF
result_df = pd.DataFrame( result , columns=['phase', 'num_trials', 'avg_enrollment', 'max_enrollment', 'min_enrollment', 'num_sponsor'])





#Streamlit App



st.write("Our first attempt at using data to create a table:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(result_df)



# simple Graph

#fig = px.bar(result_df, x='phase', y='num_sponsor')
#st.plotly_chart(fig, use_container_width=True)




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









