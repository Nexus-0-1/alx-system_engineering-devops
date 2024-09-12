#!/usr/bin/python3

"""Script that returns info about TODO list for given employee ID"""

import json
import requests
import sys

def get_employee_data():
    employee_id = int(sys.argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    url2 = '%s/todos' % url1
    todoList = requests.get(url2).json()
    user = requests.get(url1).json()

    completed_List = []
    for todo in todoList:
        if todo.get('completed') is True:
            completed_List.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): "
          .format(user.get('name'), len(completed_List), len(todoList)))
    for todo in completed_List:
        print("\t {}".format(todo))

if __name__ == '__main__':
    get_employee_data()
