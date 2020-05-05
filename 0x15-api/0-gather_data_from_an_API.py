#!/usr/bin/python3
"""Python script that using a REST API, for a given employee ID,
returns information about list progress"""

if __name__ == '__main__':
    import requests
    import sys
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    u_id = requests.get(url + 'users?', params={'id': user_id}).json()
    t_do = requests.get(url + 'todos?', params={'userId': user_id}).json()

    EMPLOYEE = u_id[0].get('name')
    DONE = sum(tasks.get("completed")
               for tasks in t_do if tasks)
    TASK = len(t_do)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE,
                                                          DONE,
                                                          TASK))
    [print("\t {}".format(task.get('title')))
     for task in t_do if task.get("completed")]
