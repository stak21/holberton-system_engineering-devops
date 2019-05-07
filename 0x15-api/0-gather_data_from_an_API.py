#!/usr/bin/python3
"""
Script: Request from the given api for a given employee ID and return
infrmation about the todo list
"""
import json
import requests
import sys


todo_url = "https://jsonplaceholder.typicode.com/todos/"
users_url = "https://jsonplaceholder.typicode.com/users/"
completed_tasks = 0
total_tasks = 0
tasks = []
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
    for task in json.loads(todo_r.text):
        if task['userId'] == int(employee_id):
            total_tasks += 1
            if task["completed"]:
                tasks.append(task)
                completed_tasks += 1
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"], completed_tasks, total_tasks
            )
        )
    for task in tasks:
        if task['userId'] == int(employee_id):
            print("\t {}".format(task["title"]))
