#!/usr/bin/python3
""" this module contains a python script that, using the JSONplaceholder
API, for a given employee ID, returns information about his/her
todo list progress """
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId), verify=False).json()
    # todo variable = grabs all todos (completed or not) for the user passed in
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId), verify=False).json()
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(name.get('name'), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))
