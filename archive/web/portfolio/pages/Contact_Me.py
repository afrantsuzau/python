import streamlit as st
from send_mail import send_mail

st.header("Contact Form")

with st.form(key='contact_form'):
    name = st.text_input(label='Name')
    email = st.text_input(label='Email')
    message = st.text_area(label='Message')
    email = f"""\
Subject: New message from {name}

From: {email}
{message}
"""
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        send_mail(email)
        st.info('Form submitted successfully!')