import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title(' 🥣 My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('Sandwich')
streamlit.text('Juice')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick som efruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


choice = streamlit.text_input('What fruit you need info on ?','Kiwi')
streamlit.write('Fruit Selected :', choice)
response = requests.get("https://fruityvice.com/api/fruit/" + choice)
streamlit.dataframe(pandas.json_normalize(response.json()))


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
