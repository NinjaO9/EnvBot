import nextcord
import main, helper
from typing import Optional
from nextcord import Interaction
from nextcord.ext import commands

class getnews(commands.Cog):
    bot = main.bot

    @nextcord.slash_command(name="retrievenews", description="See news concerning enviornmental science")
    async def getNews(self, Interation:Interaction, keywords:str, count:Optional[str], channel: Optional[str], date: Optional[str]):          
        global active_channel
        try:
            news = (helper.getArticles(keywords, count, date))
            if channel != None:
                active_channel = helper.getActiveChannel(channel)
            if news == []:
                await Interation.response.send_message(content=f"There were no articles with the keyword '{keywords}' found!", ephemeral=True)
            else:
                message = helper.formatNews(news)
                try:
                    try:
                        active_channel = helper.getGlobalActiveChannel()
                    except:
                        print(None)
                    await active_channel.send(message)
                    await Interation.response.defer(ephemeral=True)
                except:
                    await Interation.response.send_message(message)
        except Exception as e:
            await Interation.response.send_message(content=f"An Error Occured: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(getnews(bot))