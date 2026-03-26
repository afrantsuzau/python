import streamlit as st
import pandas as pd

file_path = 'web/company-site/files'

data = pd.read_csv(f'{file_path}/data.csv')
topics = pd.read_csv(f'{file_path}/topics.csv')

st.set_page_config(page_title='Company Site', page_icon=':smile:', layout='wide')

st.title('Company Site')
st.write('This is a company site built with Streamlit')

st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

def team_info(first_name, last_name, role, image):
  st.markdown(f"""
                ##### {first_name.title()} {last_name.title()}
                *{role.capitalize()}*
              """)
  st.image(f'{file_path}/images/{image}', width=200)

with col1:
  for index, row in data[:4].iterrows():
    team_info(row['first name'], row['last name'], row['role'], row['image'])

with col2:
  for index, row in data[4:-4].iterrows():
    team_info(row['first name'], row['last name'], row['role'], row['image'])
    
with col3:
  for index, row in data[-4:].iterrows():
    team_info(row['first name'], row['last name'], row['role'], row['image'])