import requests
def get_header(token = None):
    if token:
        return {
            "x-auth-token": f"{token}"
        }   
def post(url, payload , token = None):
    headers = get_header(token)
    response = requests.post(url, json=payload, headers=headers)
    return response
def get(url, token = None):
    headers = get_header(token)
    response = requests.get(url, headers=headers)
    return response
def delete(url, token = None):
    headers = get_header(token)
    response = requests.delete(url, headers=headers)
    return response
def put(url, payload , token = None):
    headers = get_header(token)
    response = requests.put(url, json=payload, headers=headers)
    return response
def patch(url, payload , token = None):
    headers = get_header(token)
    response = requests.patch(url, json=payload, headers=headers)
    return response
