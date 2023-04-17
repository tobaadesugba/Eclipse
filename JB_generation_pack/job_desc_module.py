import openai


class JobDesc:
    def __init__(self, prefix):
        self.prefix_message = prefix  # taking input from frontend
        openai.api_key = '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'

    def get_job_desc(self):
        suffix_message = "Generate a job description for "  # framework
        completion = openai.ChatCompletion.create(  # generate the job description
            model="gpt-3.5-turbo",  # select model
            messages=[
                {"role": "user", "content": suffix_message + self.prefix_message}  # combine prompts together
            ]
        )
        return completion.choices[0].message["content"]  # store description in variable
