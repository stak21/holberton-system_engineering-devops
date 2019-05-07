#!/usr/bin/python3
"""
Script: Request from the given api for a given employee ID and export the
information to json format

"""
import json
import requests
import sys


todo_url = "https://jsonplaceholder.typicode.com/todos/"
users_url = "https://jsonplaceholder.typicode.com/users/"
user_dict = {}
if len(sys.argv) >= 2:
    employee_id = sys.argv[1]
    try:
        int(employee_id)
    except ValueError:
        print("Argument requires an integer")
        sys.exit()
    users_r = requests.get(users_url + employee_id)
    if users_r.status_code != 200:
        print("User does not exist")
        sys.exit()
    todo_r = requests.get(todo_url)
    user = json.loads(users_r.text)
    user_dict["{}".format(employee_id)] = []
    for task in json.loads(todo_r.text):
        if task['userId'] == int(employee_id):
                user_dict[str(employee_id)].append(
                                        dict({"task": task['title'],
                                             "completed": task['completed'],
                                              "username": user['username']}))
    with open('{}.json'.format(employee_id), mode='w') as employee_file:
        json.dump(user_dict, employee_file)
