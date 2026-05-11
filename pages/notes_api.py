from fixtures.auth_client import post, get , delete
def login_api(email, password):
    response = post("https://practice.expandtesting.com/notes/api/users/login", {"email": email, "password": password})
    return response
def create_note_api(token, title, description, category, completed):
    response = post(
        "https://practice.expandtesting.com/notes/api/notes/",
        {
            "title": title,
            "description": description,
            "category": category,
            "completed": completed
        },
        token
    )
    return response
def delete_note_api(token, note_id):
    response = delete(
        f"https://practice.expandtesting.com/notes/api/notes/{note_id}",
        token
    )
    return response
def get_notes_api(token):
    response = get(
        "https://practice.expandtesting.com/notes/api/notes/",
        token
    )
    return response
def get_note_by_id_api(token, note_id):
    response = get(
        f"https://practice.expandtesting.com/notes/api/notes/{note_id}",
        token
    )
    return response
def update_note_api(token, note_id, title=None, description=None, category=None, completed=None):
    payload = {}
    if title is not None:
        payload["title"] = title
    if description is not None:
        payload["description"] = description
    if category is not None:
        payload["category"] = category
    if completed is not None:
        payload["completed"] = completed

    response = post(
        f"https://practice.expandtesting.com/notes/api/notes/{note_id}",
        payload,
        token
    )
    return response
