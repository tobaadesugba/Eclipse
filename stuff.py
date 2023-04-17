from JB_generation_pack.job_desc_module import JobDesc

prefix_message=str(input('Enter the job title:')) # taking input from frontend
job_desc = JobDesc("Frontend Developer")

job_description = job_desc.get_job_desc()
print(job_description)

