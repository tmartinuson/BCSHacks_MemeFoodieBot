# import the module
import tweepy

# assign the values accordingly
consumer_key = "Z21yF4w1lrcTj4gL042ypnpYX"
consumer_secret = "XmmVZPseQGMENqqvaLe0Teqjnov8UUryHSosxv77XV41QhyMH2"
access_token = "1380934327869968388-We48AbT8z7CkZKldO0p2n7H4xbYCL1"
access_token_secret = "BQbVLqYhOeYFvaA3OqbJMdxCUa60fxDCT3L9pl3aiEQUe"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# the ID of the status
id = 1268080321590935553


# fetching the status
status = api.get_status(id)

print("The text is : " + status.text)
print("The place is : " + str(status.place))