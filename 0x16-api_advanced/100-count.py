#!/usr/bin/python3
"""
Using recursion, navigate through all the listing and print the number of
keyword occurences
if the subreddit is not found return 0
"""
import re
import requests


def count_words(subreddit, word_list, after={}, count={}):
    """ prints the number of occurences of a given keywords """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": 'Shoji'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("")
        return None
    if after is None:
        return count
    try:
        parent = response.json()
        children = parent['data']['children']
        for child in children:
            for word in child['data']['title'].split():
                for k in word_list:
                    if k not in count.keys():
                        count[k] = 0
                    if word.upper() == k.upper():
                        count[k] += 1
        after_copy = parent['data']['after']
        count = count_words(subreddit, word_list, after_copy, count)
        if after == {}:
            for key in [v[0] for v in
                        sorted(count.items(), key=lambda k: (-k[1], k[0]))]:
                if count[key] > 0:
                    print("{}: {}".format(key, count[key]))

        return count

    except Exception as e:
        print("failed {}".format(e))
        return None
