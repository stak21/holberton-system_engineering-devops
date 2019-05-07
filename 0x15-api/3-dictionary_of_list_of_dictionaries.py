#!/usr/bin/python3
"""
Script: Request from the given api for all employees and export the
information to json format
"""
import json
import requests


todo_url = "https://jsonplaceholder.typicode.com/todos/"
users_url = "https://jsonplaceholder.typicode.com/users/"
user_dict = {}
users_r = requests.get(users_url)
todo_r = requests.get(todo_url)
users = json.loads(users_r.text)
for user in users:
    employee_id = user['id']
    user_dict["{}".format(employee_id)] = []
    for task in json.loads(todo_r.text):
        if task['userId'] == int(employee_id):
                user_dict[str(employee_id)].append(
                                        dict({"task": task['title'],
                                              "completed": task['completed'],
                                              "username": user['username']}))
with open("todo_all_employees.json", mode='w') as employee_file:
    json.dump(user_dict, employee_file)
