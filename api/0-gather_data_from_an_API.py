#!/usr/bin/python3
"""
This module using a REST API for a given employee ID and
returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)
    users = response_users.json()
    todos = response_todos.json()

    for user in users:
        if user["id"] == int(user_id):
            user_name = user["name"]

    number_of_tasks = 0
    number_of_completed_tasks = 0
    tasks_completed = []
    for todo in todos:
        if todo["userId"] == int(user_id):
            number_of_tasks += 1
            if todo["completed"] is True:
                number_of_completed_tasks += 1
                tasks_completed.append(todo["title"])

    print(f"Employee {user_name} is done with\
        tasks({number_of_completed_tasks}/{number_of_tasks}):")
    for task in tasks_completed:
        print(f"     {task}")
