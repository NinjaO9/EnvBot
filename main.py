import nextcord
import asyncio
import GetKeys
import helper
from nextcord import Interaction, Client
from newsapi import NewsApiClient
from typing import Optional
from datetime import date

# Init bot
intents = nextcord.Intents.default()
client = Client(intents=intents)

background_tasks = set()
running = False

# Set keys and stuff
newsapi = NewsApiClient(api_key=GetKeys.key_list[0]) 
bottoken = (GetKeys.key_list[1]) 
serverid = (GetKeys.key_list[2]) 

def getArticles(keywords,count,date):
    articles = newsapi.get_everything(q=(f"{keywords}"), language="en", from_param=date)["articles"]
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
        active_channel = client.get_channel(int(verifyChannelIntegrity(channel)))
        return active_channel
    except Exception as e:
        print("No channel ID, or invalid channel ID was given")


# Alert the user that the bot is ready
@client.event
async def on_ready():
    print(f"Bot is online!")

##################################
#        Slash Commands          #
##################################

# Set the current channel
@client.slash_command(name="setchannel",description="sets the channel where further commands will be executed")
async def setChannel(Interaction:Interaction, channel: str):
    global active_channel
    try:
        active_channel = client.get_channel(int(verifyChannelIntegrity(channel)))
        await Interaction.response.send_message(content=f"Active channel has now been set to {active_channel}",ephemeral=True)
    except Exception as e:
        await Interaction.response.send_message(content=f"Invalid channel ID",ephemeral=True)
        print("No channel ID, or invalid channel ID was given")

# Retrieve news command
@client.slash_command(name="retrievenews", description="See news concerning enviornmental science")
async def getNews(Interation:Interaction, keywords:str, count:Optional[str], channel: Optional[str], date: Optional[str]):          
    global active_channel
    try:
        news = (getArticles(keywords, count, date))
        if channel != None:
            active_channel = getActiveChannel(channel)
        if news == []:
            await Interation.response.send_message(content=f"There were no articles with the keyword '{keywords}' found!", ephemeral=True)
        else:
            message = formatNews(news)
            try:
                await active_channel.send(message)
                await Interation.response.defer(ephemeral=True)
            except:
                await Interation.response.send_message(message)
    except Exception as e:
        await Interation.response.send_message(content=f"An Error Occured: {e}", ephemeral=True)

# Begin fetching news automatically
@client.slash_command(name="startautonews", description="Makes the bot automatically send any recent news when found")
async def autoNews(Interaction:Interaction, keywords:str, channel:str):
    global active_channel, running, autokeywords, autofetch
    try:
        news = (getArticles(keywords, None, "2024-03-01"))
        message = ''
        autokeywords = keywords
        try:
            active_channel = getActiveChannel(channel)
        except:
            print("This error probably occured because an auto command is being ran")
        if news == []:
            await Interaction.response.send_message(content=f"There were no articles with the keyword '{keywords}' found as of {date}", ephemeral=True)
        else:
            message = formatNews(news)
            try:
                await active_channel.send(message)
                await Interaction.response.defer(ephemeral=True, with_message=False)
            except:
                await Interaction.response.send_message(message)
            if not running:
                running = True
                autofetch = asyncio.create_task(fetchNews())
                background_tasks.add(autofetch)
    except Exception as e:
        await Interaction.response.send_message(content=f"An Error Occured: {e}", ephemeral=True)

async def fetchNews():
    global running
    while running:
        try:
            date = "2024-03-01"
            await asyncio.sleep(10) # recheck every second TODO: MAKE THIS INTO 1 HOUR (6000)
            print("Got past sleep")
            news = getArticles(autokeywords, "4", date)
            print("Fetched news")
            message = formatNews(news)
            print("Obtained message")
            await active_channel.send(message)
            #await autoNews(interaction=None, keywords=autokeywords, channel=None)
            print("Shouldve been sent I think")
        except Exception as e:
            print(f"An Error Occured! {e}")


@client.slash_command(name="stopautonews", description="Stops the bot from sending news. Or you can just turn it off")
async def offNews(Interaction:Interaction):
    global running, autofetch
    running = False
    try:
        autofetch.cancel()
    except Exception as e:
        print(f"Task Cancelled? {e}")
    await Interaction.response.send_message(f"No longer sending news articles!")
    print("STOPPPP")

#Incase something is missing upon installation
if newsapi == None or bottoken == None or serverid == None:
    print("You're missing an initilizing value!")

client.run(token=bottoken)
    

"plastic pollution recycle energy plants waste"