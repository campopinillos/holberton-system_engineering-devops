#!/usr/bin/python3
"""Python script that using a REST API, for a given employee ID,
returns information about  TODO list progress"""

if __name__ == '__main__':
    import sys
    import requests
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = requests.get(url + 'users/{}'.format(sys.argv[1]))
    t_do = requests.get(url + 'todos', params={'userId': sys.argv[1]})

    u_id_json = u_id.json()
    t_do_json = t_do.json()

    EMPLOYEE = u_id_json.get('name')
    DONE = sum(tasks.get("completed")
               for tasks in t_do_json if tasks)
    TASK = len(t_do_json)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE,
                                                          DONE,
                                                          TASK))
    [print("\t {}".format(task.get('title')))
     for task in t_do_json if task.get("completed")]
