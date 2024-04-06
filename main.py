import nextcord, os, getkeys
from nextcord.ext import commands
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Init bot
load_dotenv()
intents = nextcord.Intents.default()
bot = commands.Bot(intents=intents)

# Set keys and stuff
newsapi = NewsApiClient(api_key=os.getenv('API_KEY')) 
bottoken = (os.getenv('BOT_TOKEN')) 
serverid = (getkeys.key_list[0])

# Set up slash commands
command_list = []

for file in os.listdir("./slash"):
    if file.endswith(".py"):
        command_list.append("slash." + file[:-3])

#Incase something is missing upon installation
if newsapi == None or bottoken == None or serverid == None:
    print("You're missing an initilizing value! Check the 'keys.txt' file!")

def getActiveChannelID(channel):
    return bot.get_channel(channel)
# Alert the user that the bot is ready
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("---------------------------------")
    print("         Bot is online!          ")
    print("---------------------------------")


for file in command_list:
    print(f"loading '{file[6:]}' command...")
    bot.load_extension(file)
bot.run(token=bottoken)

#-------------------------------------------------------
# Envbot by NinjaO9 @https://github.com/NinjaO9/EnvBot
#-------------------------------------------------------