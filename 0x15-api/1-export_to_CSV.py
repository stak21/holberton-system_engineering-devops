#!/usr/bin/python3
"""
Script: Request from the given api for a given employee ID and return
infrmation about the todo list
"""
import csv
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
    with open('somefile.csv', mode='w') as employee_file:
        for task in json.loads(todo_r.text):
            if task['userId'] == int(employee_id):
                USER_ID = employee_id
                USERNAME = user['username']
                TASK_COMPLETED_STATUS = task['completed']
                TASK_TITLE = task['title']
                employee_writer = csv.writer(employee_file, delimiter=',',
                                             quoting=csv.QUOTE_ALL)
                employee_writer.writerow([USER_ID, USERNAME,
                                         TASK_COMPLETED_STATUS, TASK_TITLE])
