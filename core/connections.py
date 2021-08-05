"""
Connects with data sources.
"""
import requests
from lisa.settings import BACKEND_URL


class GraphQLQuery:
    """
    GraphQL Queries
    """
    @staticmethod
    def lisa_service_version():
        payload = '{ lisa }'
        request = requests.post(BACKEND_URL, json={'query': payload})

        err_msg = 'Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('lisa', [err_msg])

        return response_message[-1]

    @staticmethod
    def lisa_sentiment_extraction(text):
        payload = f'''
        query{{
        sentimentExtraction(text: "{text}")
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})
        
        err_msg = 'Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('sentimentExtraction', err_msg)
        
        return response_message
