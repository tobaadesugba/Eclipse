from JB_generation_pack.job_desc_module import JobDesc

# prefix_message=str(input('Enter the job title:')) # taking input from frontend
job_desc = JobDesc("")

job_description = job_desc.get_job_desc_with_exceptions()
if job_description['status'] == 'error':
    print(job_description['content'])

