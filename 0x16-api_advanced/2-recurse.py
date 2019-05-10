#!/usr/bin/python3
"""
Using recursion, navigate through all the listing and return the titles of each
listing
if the subreddit is not found return 0
"""
import requests


def recurse(subreddit, after={}):
    """ Returns a list of titles """
    listings = []
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-agent": 'Shoji'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    if after is None:
        return listings
    try:
        parent = response.json()
        children = parent['data']['children']
        for child in children:
            listings.append(child['data']['title'])

        after = parent['data']['after']

        ret = recurse(subreddit, after)
        if listings:
            ret.extend(listings)
        return ret
    except Exception as e:
        return None
