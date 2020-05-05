#!/usr/bin/python3
"""Python script that using a REST API, for a given employee ID,
returns information about list progress"""

if __name__ == '__main__':
    import sys
    import json
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    u_id = requests.get(url + 'users?', params={'id': user_id}).json()
    t_do = requests.get(url + 'todos?', params={'userId': user_id}).json()
    employee = u_id[0].get("username")

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": employee} for task in t_do]}, f)
