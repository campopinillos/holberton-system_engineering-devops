#!/usr/bin/python3
"""Python script that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0', }
    top = {'limit': 10}
    response = requests.get(url, headers=headers, params=top,
                            allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return
    results = response.json().get('data')
    for top in results.get("children"):
        print(top.get("data").get("title"))
