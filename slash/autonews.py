import nextcord
import main, helper, asyncio
from nextcord import Interaction
from nextcord.ext import commands

class autonews(commands.Cog):
    global autofetch
    bot = main.bot
    background_tasks = set()
    running = False

    @nextcord.slash_command(name="startautonews", description="Makes the bot automatically send any recent news when found")
    async def autoNews(self, Interaction:Interaction, keywords:str, channel:str):
        global autokeywords, autofetch
        print("Running 'Auto News' command...")
        try:
            news = (helper.getArticles(keywords, None, "2024-01-01", "relevancy"))
            message = ''
            autokeywords = keywords
            try:
                active_channel = helper.getActiveChannel(channel)
            except:
                print("This error probably occured because an auto command is being ran")
            if news == []:
                await Interaction.response.send_message(content=f"There were/are no more articles with the keyword '{keywords}' found !", ephemeral=True)
            else:
                message = helper.formatNews(news)
                try:
                    await active_channel.send(message)
                    await Interaction.response.defer(ephemeral=True, with_message=False)
                except:
                    await Interaction.response.send_message(message)
                if not self.running:
                    self.running = True
                    autofetch = asyncio.create_task(autonews.fetchNews(self, active_channel, autokeywords))
                    await getFetch()
                    self.background_tasks.add(autofetch)
        except Exception as e:
            await Interaction.response.send_message(content=f"An Error Occured: {e}", ephemeral=True)

    async def fetchNews(self, active_channel, autokeywords):
        while self.running:
            try:
                await asyncio.sleep(6000) # In seconds (60 = 1 min)
                news = helper.getArticles(autokeywords, "1", helper.getCurrentDay(), "relevancy")
                message = helper.formatNews(news)
                await active_channel.send(message)
            except Exception as e:
                print(f"An Error Occured! {e}")

async def getFetch():
    return autofetch

def setup(bot):
    bot.add_cog(autonews(bot))
