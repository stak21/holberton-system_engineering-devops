#!/usr/bin/python3
"""
Function: Queries the Reddit API and returns the number of subscribers for a
given subreddit
If invalid subreddit, return 0
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'shoji'},
                     allow_redirects=False)
    data = r.json()
    if not r.status_code == 200:
        return 0
    try:
        sub = data.get("data")
        children = sub.get("children")
        subreddit = children[0].get("data")
        subscriber_count = subreddit.get("subreddit_subscribers")
    except Exception as e:
        print("Something went wrong\n {}".format(e))
        return 0

    return subscriber_count
