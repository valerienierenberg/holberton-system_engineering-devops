#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0."""
import requests
from sys import argv
import json


def number_of_subscribers(subreddit):
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    u_agent = "Holberton-Reddit-API-project"

    subscribers_sub = requests.get(url, headers={'User-Agent': u_agent})

    if subscribers_sub.status_code != 200:
        return (0)
    else:
        jsondata = subscribers_sub.json()
        count = jsondata.get('data').get('subscribers')
        return count
