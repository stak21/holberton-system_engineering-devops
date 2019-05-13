#!/usr/bin/python3
"""
Function: Queries the Reddit API and print the titles of the top 10 hot posts
If invalid subreddit, return 0
"""
import requests


def top_ten(subreddit):
    """
    Return the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'shoji'},
                     allow_redirects=False)
    if not r.status_code == 200:
        print(None)
        return None
    data = r.json()
    try:
        sub = data.get("data")
        children = sub.get("children")
        count = len(children) if len(children) <= 10 else 10
        for child_number in range(count):
            subreddit = children[child_number].get("data")
            print(subreddit.get("title"))

    except Exception as e:
        print(None)
