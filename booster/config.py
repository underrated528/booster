#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# config.py

class api:
	consumer_key        = 'A7Z6K3EH6cuAKUjL07IthZg2U'
	consumer_secret     = 'PEjIYIlugK3QxBQULWVwd0X64whTsmk8gsLMhPZCZtLT0HUeLy'
	access_token        = '1625857606823874563-VBI7M5Wo2y4lKZtUGICP0ICJ6h2F50'
	access_token_secret = '8jxU0XwtbUVicgt9IiVIxrUJpgdYSJ7V2ss0y7XZj51Ij'

class throttle:
	favorite = 75
	follow   = 75
	message  = 750
	tweet    = 750
	unfollow = 75

class settings:
	keywords = ['500aday','autofollow','autofollowback','f4f','follow','follow4follow','followback','followtrain','instantfollow','instantfollowback','teamfollowback','wefollowback']
	message  = 'Thank you for following our Twitter account!' # Set to None to disable sending messages to new followers
	woeid    = 23424975 # Where On Earth ID (http://www.woeidlookup.com/)
