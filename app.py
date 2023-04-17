import streamlit as st
from JB_generation_pack.job_desc_module import JobDesc

st.header("Eclipse Job Description Generator")
allow_editing = st.checkbox("Tick the box if you want to edit the generated job description")
input_data = st.text_area("Enter the job title and press \"ctrl+enter\" when done")

button = st.button('Generate Job Description')


def generate_job():
    with st.spinner('Wait for it, the job description is generating...'):
        job_desc = JobDesc(input_data)
        job_description = job_desc.get_job_desc()
    st.success('Done!')
    return job_description


if allow_editing and button:
    output = st.text_area("Edit and press \"ctrl+enter\" when done", value=generate_job())
    if st.button("Send to job portal"):
        st.success("On its way to the specified job portals")
elif not allow_editing and button:
    output = st.text(generate_job())
    if st.button("Send to job portal"):
        st.success("On its way to the specified job portals again")
