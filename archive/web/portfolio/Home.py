import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Aliaksandr Frantsuzau", page_icon="web/portfolio/files/images/logo.png")

col1, col2 = st.columns(2)

with col1:
    st.image("web/portfolio/files/images/photo.png", width=375)
    
with col2:
    st.title("Aliaksandr Frantsuzau")
    content = """
      ##### Experienced DevOps Engineer with a demonstrated history of working in the information technology and services industry.
      
      Key responsibilities:
      * Kubernetes cluster setup and further administration/monitoring/alerting/troubleshooting/maintainance.
      * Develop EKS cluster provisioning from scratch using Terraform.
      * Migrate Production/Staging/Demo/Testing environments into Kubernetes.
      * Traffic monitoring and management via Istio Service Mesh, canary
      deployments via Flagger.
      * Implement provisioning and configurations of AWS infrastructure with
      Terraform/Ansible/Packer.
      * Building CI/CD processes with Jenkins declarative pipelines.
      * Integrating infrastructure logging/monitoring tools
      * MySQL configuration, maintenance, version upgrade, monitoring, queries
      analysing and building proper indexes.
    """
    st.info(content)
    
col3, empty_col, col4 = st.columns([1.5, 0.15, 1.5])
data = pd.read_csv("web/portfolio/files/data.csv",sep=";")

with col3:
  for index, row in data[:10].iterrows():
    st.markdown(f"""
    ###### {row['title']}
    {row['description']}
    """)
    st.image("web/portfolio/files/images/" + row['image'])
    st.write(f"[Source Code]({row['url']})")
    
with col4:
  for index, row in data[10:].iterrows():
    st.markdown(f"""
    ###### {row['title']}
    {row['description']}
    """)
    st.image("web/portfolio/files/images/" + row['image'])
    st.write(f"[Source Code]({row['url']})")