# Popular Tweet Search 

PopulaTweetSearch is a simple python application that extracts , analyses and displays the top 5 popular tweets using tweepy api. 

## How does it look ? 
![PopularTweetSearch](screenshot.png?raw=true "PopularTweetSearch")


## How does it work ? 
Taking the user input ( search string ) in a multi-threading environment, application will search the twitter database for all occurrences of search string. Then, app will sort all the responses in descending order with reference to number of retweets. And it will extract the top 5 tweets from sorted list and displays in a tabular format. 
>The above steps will be repeated every 5 seconds in a different thread so that, at any given point in time the table will always displays up to date and most popular tweets .  

### Modules used:
1. os
2. tweepy
3. json
4. threading
5. time
6. PrettyTable
