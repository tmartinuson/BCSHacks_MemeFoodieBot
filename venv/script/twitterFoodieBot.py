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
    #Guide function for mentionee's handle name
    followers = twitter_API.followers()
    for follower in followers:
        twitter_API.update_status('Hello @' + follower.screen_name)


def handle_mention(mention_object):
    #TODO Pull the text from the mention_object and store it into a string to be used for a google query
    query = mention_object.text[15:]
    print(query)



    #TODO Query google using test string from the mention object and store the restaurant url as a string (for now, we have to see how twitter handles restaurant retweets)
    # query

    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")


    query = "Ice cream Vancouver"

    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)


    #TODO Call twitter_API to reply to the mention handle with the URL of the restaurant
    ## FORMAT: @'mentioneehandle' https://www.somerestaurant.com


    #Possible TODO - reply with a screen shot of the google query
    return

while True:

    mentions = twitter_API.mentions_timeline(20)
    for mention in tweepy.Cursor(twitter_API.mentions_timeline).items():
        #Checks to see if we have already replied to this mention (Don't want to reply to the same user multiple times)
        if not mention.favorited:
            handle_mention(mention)
            id = mention.id
            #Favorites tweet as not to reply
            #twitter_API.create_favorite(id = id)
            print(mention.text)
    time.sleep(120)



