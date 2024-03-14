# Python file for all the "background tasks" such as verifying and sorting lists
import main
from datetime import date

bot = main.bot
blacklist = [] #blacklist of news that should no longer appear on messages sent by the bot.

def getArticles(keywords,count,time,sortBy):
    global blacklist
    articles = main.newsapi.get_everything(q=(f"{keywords}"), language="en", from_param=time, sort_by=sortBy)["articles"]
    articles = list(filter( lambda item: item not in blacklist, articles))
    articles = articles[:int(verifyCountIntegrity(count))]
    blacklist = blacklist + articles
    return articles

def verifyCountIntegrity(count: str):
    if count == None:
        return 1
    if count.isdigit():
        return count
    else:
        print(f"{count} isn't a number")
        return 1

def verifyChannelIntegrity(channel:str):
    if channel == None:
        return None
    if channel.isdigit():
        return channel
    else:
        return None

def verifyDateIntegrity(time:str):
    datechar = list(time)
    temp = ''
    datechar.pop[4]
    datechar.pop[6] #pop where the "-" should be in the dates "####-##-##"
    temp = str(datechar)
    if temp.isdigit():
        return time
    else:
        return "2024-01-01"
    
def getCurrentDay():
    return date.today()

def formatNews(news):
    message = ''
    for article in news:
            if len(message) > 1500:
                return message
            message = message + (f"{article['title']}: \n {article['url']} \n")
    return message

def getActiveChannel(channel):
    global active_channel
    try:
        active_channel = bot.get_channel(int(verifyChannelIntegrity(channel)))
        return active_channel
    except Exception as e:
        print("No channel ID, or invalid channel ID was given")

def setGlobalActiveChannel(channel):
    global active_channel
    active_channel = channel

def getGlobalActiveChannel():
    global active_channel
    try:
        return active_channel
    except Exception as e:
        if active_channel != None:
            print(f"No active channel set? {e}")