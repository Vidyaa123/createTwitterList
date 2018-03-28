#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:33:33 2018

@author: Vidyaa
"""

from twython import Twython, TwythonError
import config

#create twython object with twitter credentials from config.py
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

#retrieve the recent 100 tweets with #iOS
response = twitter.search(q='"#iOSdev" -filter:retweets',result_type="recent", count=100)
                          
for tweet in response['statuses']:
    try:
        twitter.add_list_member(slug='iosengineers', owner_screen_name='vidyaash', screen_name = tweet['user']['screen_name'])
        
    except TwythonError as e:
        print(e)