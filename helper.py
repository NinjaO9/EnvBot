# Python file for all the "background tasks" such as verifying and sorting lists
import main
from datetime import date

def getArticles(keywords,count,date):
    articles = main.newsapi.get_everything(q=(f"{keywords}"), language="en", from_param=date)["articles"]
    return articles[:int(verifyCountIntegrity(count))]

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

def verifyDateIntegrity(date:str):
    datechar = list(date)
    temp = ''
    datechar.pop[4]
    datechar.pop[6] #pop where the "-" should be in the dates "####-##-##"
    temp = str(datechar)
    if temp.isdigit():
        return date
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
    try:
        active_channel = main.client.get_channel(int(verifyChannelIntegrity(channel)))
        return active_channel
    except Exception as e:
        print("No channel ID, or invalid channel ID was given")