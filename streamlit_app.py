import streamlit
import pandas

streamlit.title(' 🥣 My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('Sandwich')
streamlit.text('Juice')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick som efruits:", list(my_fruit_list.index),['Avocado','Apple'])
streamlit.dataframe(my_fruit_list)
