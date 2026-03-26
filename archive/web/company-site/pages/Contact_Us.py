import streamlit as st, pandas as pd
from send_mail import send_mail

data = pd.read_csv('web/company-site/files/topics.csv')
print("Data:\n", data)
topics_list = data["topic"].tolist()

with st.form(key='contact_form'):
    email = st.text_input(label='Email')
    topic = st.selectbox(label='Topic', options=topics_list)
    message = st.text_area(label='Message')
    email = f"""\
Subject: {topic}

From: {email}
{message}
"""
    if st.form_submit_button(label='Submit'):
        send_mail(email)
        st.info('Form submitted successfully!')