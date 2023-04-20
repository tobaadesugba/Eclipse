import openai
from openai.error import AuthenticationError, APIError, Timeout, InvalidRequestError, APIConnectionError, \
    RateLimitError, PermissionError, ServiceUnavailableError


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

    def get_job_desc_with_exceptions(self):
        message = dict()

        try:
            assert (self.prefix_message != '')
            desc = self.get_job_desc()
        except AssertionError:
            message["status"] = 'error'
            message["content"] = 'No job title has been entered'
        except (APIError, Timeout, InvalidRequestError, ServiceUnavailableError):
            message["status"] = 'error'
            message["content"] = 'There seems to be an issue, please try again or contact support'
        except APIConnectionError:
            message["status"] = 'error'
            message["content"] = 'There seems to be a connection issue, please check your network settings'
        except AuthenticationError:
            message["status"] = 'error'
            message["content"] = 'The API key is invalid or expired, please contact support'
        except PermissionError:
            message["status"] = 'error'
            message["content"] = 'It seems you don\'t have permission for the requested action, please contact support'
        except RateLimitError:
            message["status"] = 'error'
            message["content"] = 'The service is currently overloaded, please try again later or contact support'
        else:
            message["status"] = 'okay'
            message["content"] = desc

        return message
