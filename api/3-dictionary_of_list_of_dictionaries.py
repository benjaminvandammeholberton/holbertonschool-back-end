#!/usr/bin/python3
"""
This module using a REST API for a given employee ID,
returns information about his/her TODO list progress
and export data in the JSON format
"""
if __name__ == "__main__":
    import json
    import requests

    file_name = f"todo_all_employees.json"
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)
    users = response_users.json()
    todos = response_todos.json()

    main_dict = {}
    for user in users:
        main_dict[user["id"]] = []

    my_dict = {}
    for todo in todos:
        for user in users:
            if todo["userId"] == user["id"]:
                username = user["username"]

        if todo["userId"] in main_dict:
            userId = todo["userId"]
            dict_item = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"],
            }
            main_dict[userId].append(dict_item)

    with open(file_name, "w") as json_file:
        json.dump(main_dict, json_file, indent=4)
