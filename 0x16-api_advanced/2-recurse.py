#!/usr/bin/python3
"""Python script that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all hot articles
    for a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0', }
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get("data").get("children")
    [hot_list.append(post.get("data").get("title")) for post in posts]
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    recurse(subreddit, hot_list, after)
