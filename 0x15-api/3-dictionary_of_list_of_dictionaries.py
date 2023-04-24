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

    data = {user.get('id'): [{"task": todo.get('title'),
              "completed": todo.get('completed'),
              "username": user.get('username')}
              for todo in todos_data]
              for user in user_data}

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
