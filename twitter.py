#!/usr/bin/env python

#need to install tweepy library, in cmd line:
#pip install tweepy
#docs.tweepy.org

import tweepy

api_key = 'l7XmHUEJV1YlpCp6o27bv9kyG'
api_secret = 'iz9QIRWFNequnOQPmSoi3B37jYZO894fQAuErBq9f6aCMPpQVk'
auth_key = '412671286-uTOog7J2MRchcKocj4AoG1RRBvIodmSuI7ch2DYr'
auth_secret = 'QfNDMdMMHXxEkMoFWzrihPv8HjfChBhLdehm97VqtixdY'

auth = tweepy.OAuthHandler(api_key, api_secret) #create authorization access with tweepy OAuthHandler
auth.set_access_token(auth_key, auth_secret) #give auth object authorization

api = tweepy.API(auth) #call a method on the auth object

my_account = api.me()

#looks like most of the information is stored as dicts

#for follower in api.followers():
#	print follower.name #good guess that name is the key

#for friend in api.friends():
#	print friend.name

#to update status:
#api.update_status(status = "...")

out_file = open('output.txt','w') #output file opened for writing

redsox_tweets = tweepy.Cursor(api.search,q="#redsox",lang="en",since_id="2015-05-13",until="2015-05-14").items() #if no number in parenthetical for item, returns all

for tweet in redsox_tweets:
	line = '{}\n{}\n\n'.format(tweet.created_at, tweet.text.encode('utf-8'))
	out_file.write(line)

###
content = open('output.txt').read()
tweets = content.split('\n\n')
new_tweets = []
for tweet in tweets:
	time, text = tweet.split('\n')
	new_tweets.append(dict(time=time,text=text))
