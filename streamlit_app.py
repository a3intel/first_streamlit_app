import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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

try:
  choice = streamlit.text_input('What fruit you need info on ?')
  if not choice:
    streamlit.error('Please select')
  else:
    response = requests.get("https://fruityvice.com/api/fruit/" + choice)
    streamlit.dataframe(pandas.json_normalize(response.json()))
except URLError as e:
     streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit List:")
streamlit.dataframe(my_data_row)


choice2 = streamlit.text_input('What would you like to add ?')
my_fruit_list2 = my_data_row
fruits_selected2 = streamlit.multiselect("Pick some fruits:", list(my_fruit_list2))
streamlit.write('Fruit Selected :', fruits_selected2)
my_cur.execute("Insert into fruit_load_list values ('from streamlit')")
