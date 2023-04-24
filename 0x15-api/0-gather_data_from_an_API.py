#!/usr/bin/python3

"""This module handles the fetching of an employee's
TODO list progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    emp_id = int(argv[1])
    todos = requests.get(
          'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(
          'https://jsonplaceholder.typicode.com/users/{}'.
          format(emp_id))

    todos_data = todos.json()
    user_data = users.json()

    emp_data = list(filter(
             lambda emp: emp_id == emp.get('userId'), todos_data))
    num_tasks = len(emp_data)
    done_tasks = len(list(filter(
               lambda done: done.get('completed'), emp_data)))
    emp_name = user_data.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
          emp_name, done_tasks, num_tasks))

    for task in emp_data:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
