#!/usr/bin/python3
"""
Using recursion, navigate through all the listing and print the number of
keyword occurences
if the subreddit is not found return 0
"""
import re
import requests


def count_words(subreddit, word_list, after={}):
    """ prints the number of occurences of a given keywords """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-agent": 'Shoji'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("")
        return None
    if after is None:
        return {}
    try:
        counts = {k: 0 for k in word_list}
        parent = response.json()
        children = parent['data']['children']
        for child in children:
            for k, v in counts.items():
                reg_key = k.upper()
                reg = re.compile(r'\b{}\b'.format(reg_key))
                count = re.findall(reg, child['data']['title'].upper())
                counts[k] = counts[k] + len(count)
        after_copy = parent['data']['after']
        ret_count = count_words(subreddit, word_list, after_copy)
        if ret_count:
            for k in counts.keys():
                counts[k] = counts[k] + ret_count[k]
        if after == {}:
            for key in sorted(counts, key=lambda k: (-counts[k], k)):
                if counts[key] > 0:
                    print("{}: {}".format(key, counts[key]))

        return counts

    except Exception as e:
        print("failed {}".format(e))
        return None
