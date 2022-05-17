import requests


class StatusCodeError(Exception):
    pass


def get_post_by_id(id):
    endpoint = f'/posts/{id}'
    return rest_query(endpoint)


def get_user_by_id(id):
    endpoint = f'/users/{id}'
    return rest_query(endpoint)


def rest_query(endpoint_url):
    url = 'https://jsonplaceholder.typicode.com'

    url = url + endpoint_url

    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None

    raise StatusCodeError('Undefined status code')
