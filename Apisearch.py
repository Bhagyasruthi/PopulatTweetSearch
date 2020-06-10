from os import system, name 
import twitter_credentials
from tweepy import OAuthHandler
import tweepy
import json
import threading
import time
from prettytable import PrettyTable
c = threading.Condition()
#create a empty list to store the tweets
tweets = []
#create a empty string to store a input tweet_search
tweet_search = ""
#define a function clear() to refresh the terminal
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
#define a function analyse() to extracting  the  data from twitter and using the data to display top 5 most popular
def analyse():
    #with variable(fetch_status) where value(query='tweet_search', result_type='return only the most popular results in the response',language ="english")
     fetched_status = api.search(q=tweet_search, result_type="popular",lang="en")
     for item in fetched_status:
        #json.loads() takes in a string and returns a json object(item._json).
        #json.dumps() takes in a json object(item._json) and returns a string
        item = json.loads(json.dumps(item._json))
        #append 'items' to tweets list
        tweets.append(item)
      #sort the tweets with key(retweet_count) in decending order and disaplay top 5 
     sorted_tweets = sorted(tweets, key=lambda x : x['retweet_count'], reverse=True)[:5]
     #create a table with prettytable to display in tabular formate with attributes name,retweet_count,tweet
     table = PrettyTable(['name', 'retweet_count','tweet'])
     #for each tweet in sorted_tweets list perform table formate and display
     for tweet in sorted_tweets:
         #using tweeted person username , posted retweeted count and text created a table for each iteiration
        table.add_row([tweet['user']['name'],tweet['retweet_count'],tweet['text']])
       #print the out in table formate 
     print(table)

#create class threading to analyse and print the out 
class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        while True:
            #acquire the thread 
            c.acquire()
            #clearing the cache of tweet
            tweets.clear()
            #call the analyse function
            analyse()
            #thread is at rest position for 5secs
            time.sleep(5)
            #clear the terminal
            clear()
            #release the thread to run again after holding 5secs
            c.release()



if __name__ == "__main__":
    #get authorizations credentials from twitter
    auth     =  OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) 
    #pass the authorized credential to twitter API
    api = tweepy.API(auth)
    #take  a user input-->
    tweet_search = input("tweet search...")
    #create a object for class Thread_A
    a = Thread_A("myThread_name_A")
    #start the thread 
    a.start()
