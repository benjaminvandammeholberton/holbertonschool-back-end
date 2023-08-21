#!/usr/bin/python3
"""
This module using a REST API for a given employee ID,
returns information about his/her TODO list progress
and export data in the JSON format
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    file_name = f"{user_id}.json"
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)
    users = response_users.json()
    todos = response_todos.json()

    for user in users:
        if user["id"] == int(user_id):
            user_name = user["username"]

    my_list = []
    my_dict = {}
    for todo in todos:
        if todo["userId"] == int(user_id):
            my_list.append({
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_name
                })
    my_dict = {user_id: my_list}

    print(my_dict)

    with open(file_name, "w") as json_file:
        json.dump(my_dict, json_file)
