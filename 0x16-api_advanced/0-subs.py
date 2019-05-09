#!/usr/bin/python3
"""
Function: Queries the Reddit API and returns the number of subscribers for a
given subreddit
If invalid subreddit, return 0
"""
import requests
import json

r = requests.get("https://www.reddit.com/r/random.json", 
        headers = {'User-agent': 'shoji'})
data = r.json()
print(type(data))

