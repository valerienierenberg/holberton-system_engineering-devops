#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the
function should return None."""
import json
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after="null"):
    """ docstring """
"""
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/hot.json??limit=100&after={}".format(
        subreddit, after)
    u_agent = "Holberton-Reddit-API-project"

    hot_response = requests.get(url, headers={'User-Agent': u_agent})

    if hot_response.status_code != 200:
        return(None)
    else:
        jsondata = hot_response.json()
        data = jsondata.get('data')
        after = data.get('after')

    if after is None:
        return hot_list
    else:
        children = data.get('children')
        hot_list = hot_list + children
        return recurse(subreddit, hot_list, after)
"""
