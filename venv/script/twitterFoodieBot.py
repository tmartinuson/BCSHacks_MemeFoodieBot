import tweepy
import time
import googlesearch

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

    query = query + "Twitter"

    restaurant_twitter_handle = ""
    restaurant_url = ""

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        #Pick a random restaurant twitter
        restaurant_twitter_handle = j + ""
        restaurant_url = j
        #print(j)

    restaurant_twitter_handle = restaurant_twitter_handle[20:].split("?")[0]

    #print(restaurant_twitter_handle)
    print(restaurant_url)

    user = twitter_API.get_user(screen_name = restaurant_twitter_handle)
    best_tweet_of_user = twitter_API.user_timeline(user_id = user.id,count = 1)[0]
    #print(user)
    #print(best_tweet_of_user)

    #TODO Call twitter_API to reply to the mention handle with the URL of the restaurant
    ## FORMAT: @'mentioneehandle' https://www.somerestaurant.com

    reply_username = mention_object.user.screen_name

    status = "Enjoy! @" + reply_username + " " + restaurant_url

    twitter_API.update_status(in_reply_to_status_id = mention_object.id, auto_populate_reply_metadata = True, status = status)

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
            print(mention.id)
    time.sleep(120)



