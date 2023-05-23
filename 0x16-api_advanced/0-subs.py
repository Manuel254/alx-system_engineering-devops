#!/usr/bin/python3

"""This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for an existing
    subreddit
    Return:
        number of subscribers (int)
    """
    if subreddit is None:
        return 0

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/88.0.4324.188'}

    res = requests.get(url, headers=header, allow_redirects=False)
    
    try:
        data = res.json().get('data')
        return data.get('subscribers')
    except Exception:
        return 0
