import tweepy
import time

CONSUMER_KEY = 'Z21yF4w1lrcTj4gL042ypnpYX'
CONSUMER_SECRET = 'XmmVZPseQGMENqqvaLe0Teqjnov8UUryHSosxv77XV41QhyMH2'
ACCESS_KEY = '1380934327869968388-We48AbT8z7CkZKldO0p2n7H4xbYCL1'
ACCESS_SECRET = 'BQbVLqYhOeYFvaA3OqbJMdxCUa60fxDCT3L9pl3aiEQUe'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

print("Authcodes approved!")

twitter_API = tweepy.API(auth)

def mention_followers():
    followers = twitter_API.followers()
    for follower in followers:
        twitter_API.update_status('Hello @' + follower.screen_name)

#twitter_API.update_status('Hello World')

def get_memes(query, count):
    tweets = []
    fetch_tweets = twitter_API.search(query,count)

    for tweet in fetch_tweets:
        tweet


def handle_mention_food():
    #TODO Handle when someone tweets the bot with a meme and reply with a food recommendation
    return

def handle_mention_meme():
    #TODO Handle when someone tweets the both with a food item and reply with a meme
    return

while True:
    new_mentions = twitter_API.mentions_timeline(20)
    if(len(new_mentions) > 0):
        time.sleep(1)
        # TODO if food
        #   handle_mention_food
        # TODO if meme
        #   handle_mention_meme
    time.sleep(120)



