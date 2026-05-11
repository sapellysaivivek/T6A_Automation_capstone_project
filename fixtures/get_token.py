from fixtures.auth_client import post
def get_token(email, password):
    response = post("https://practice.expandtesting.com/notes/api/users/login", {"email": email, "password": password})
    return response.json().get("data" , {}).get("token")
