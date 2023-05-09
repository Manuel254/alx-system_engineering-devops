#!/usr/bin/python3

"""This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
    for a given subreddit
    """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/88.0.4324.188'}
    limit = {'limit': 10}

    res = requests.get(url, headers=header, params=limit)

    if not res:
        print(None)
    else:
        posts = res.json().get('data').get('children')

        for post in posts:
            title = post.get('data').get('title')
            print(title)
