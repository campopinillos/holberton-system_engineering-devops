#!/usr/bin/python3
"""Python script that using a REST API, for a given employee ID,
returns information about list progress"""

if __name__ == '__main__':
    import sys
    import csv
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    u_id = requests.get(url + 'users?', params={'id': user_id}).json()
    t_do = requests.get(url + 'todos?', params={'userId': user_id}).json()
    employee = u_id[0].get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',',
                            quotechar='"')
        [writer.writerow([user_id, employee, task.get("completed"),
                          task.get("title")]) for task in t_do]
