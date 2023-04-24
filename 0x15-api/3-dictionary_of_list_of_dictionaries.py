#!/usr/bin/python3

"""This module handles the fetching of an employee's
TODO list progress and stores the data in a json file
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    todos = requests.get(
          'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(
          'https://jsonplaceholder.typicode.com/users/')

    todos_data = todos.json()
    user_data = users.json()

    new_dict = {}

    for user in user_data:
        username = user.get('username')
        user_id = user.get('id')
        todos = []
        for todo in todos_data:
            if todo.get('userId') == user_id:
                my_dict = {
                        "username": username,
                        "task": todo.get('title'),
                        "completed": todo.get('completed')}
                todos.append(my_dict)
        new_dict[user_id] = todos

    with open('todo_all_employees.json', 'w') as f:
        json.dump(new_dict, f)
