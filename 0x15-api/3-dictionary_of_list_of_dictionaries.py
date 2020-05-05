#!/usr/bin/python3
"""Python script that using a REST API, for a given employee ID,
returns information about list progress"""

if __name__ == '__main__':
    import json
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = requests.get(url + "users").json()

    dic = {}
    for user in u_id:
        dic[user.get("id")] = [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in requests.get(url + "todos",
                                   params={"userId": user.get("id")}).json()]

    with open("todo_all_employees.json", "w", newline='') as f:
        json.dump(dic, f)
