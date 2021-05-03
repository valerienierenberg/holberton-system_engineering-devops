#!/usr/bin/python3
""" this module contains a python script that, using the JSONplaceholder
API, for a given employee ID, returns information about his/her
todo list progress """

import requests
from sys import argv

if __name__ == "__main__":
    userid = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userid), verify=False).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userid={}'
                        .format(userid), verify=False).json()
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name.get('name'), len(completed), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed))
