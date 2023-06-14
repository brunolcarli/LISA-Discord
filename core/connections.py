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
        
        err_msg = 'ERROR: Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('sentimentExtraction', err_msg)
        
        return response_message

    @staticmethod
    def text_offense_level(text):
        payload = f'''
        query {{
            textOffenseLevel(text: "{text}") {{
                text
                average
                isOffensive
            }}
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})
        err_msg = 'ERROR: Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('textOffenseLevel', err_msg)
        
        return response_message

    @staticmethod
    def similarity(a, b):
        payload = f'''
        query {{
            similarity(firstToken: "{a}" secondToken: "{b}")
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})
        err_msg = 'ERROR: Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('similarity', err_msg)
        
        return response_message

    @staticmethod
    def part_of_speech(text):
        payload = f'''
        query {{
            partOfSpeech(text: "{text}") {{
                token
                description
            }}
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})
        err_msg = 'ERROR: Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('partOfSpeech', err_msg)
        
        return response_message
