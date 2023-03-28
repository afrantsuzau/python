import streamlit as st

st.set_page_config(layout="wide", page_title="Aliaksandr Frantsuzau", page_icon="web/portfolio/files/images/logo.png")

col1, col2 = st.columns(2)

with col1:
    st.image("web/portfolio/files/images/photo.png", width=450)
    
with col2:
    st.title("Aliaksandr Frantsuzau")
    content = """
    Experienced DevOps Engineer with a demonstrated history of working in the information technology and services industry.
    
    Responsibilities:
    • Kubernetes cluster setup and further administration/monitoring/alerting/troubleshooting/maintainance.
    • Develop EKS cluster provisioning from scratch using Terraform.
    • Migrate Production/Staging/Demo/Testing environments into Kubernetes.
    • Traffic monitoring and management via Istio Service Mesh, canary
    deployments via Flagger.
    • Implement provisioning and configurations of AWS infrastructure with
    Terraform/Ansible/Packer.
    • Building CI/CD processes with Jenkins declarative pipelines.
    • Integrating infrastructure logging/monitoring tools
    • MySQL configuration, maintenance, version upgrade, monitoring, queries
    analysing and building proper indexes.
    """
    st.write(content)