import nextcord
import main
from nextcord import Interaction
from nextcord.ext import commands
from slash.autonews import getFetch

class offnews(commands.Cog):
    bot = main.bot

    @nextcord.slash_command(name="stopautonews", description="Stops bot from sending news")
    async def offNews(self,Interaction:Interaction):
        global running
        running = False
        try:
            autofetch = await getFetch()
            autofetch.cancel()
            await Interaction.response.send_message(content=(f"No longer sending news articles!"), ephemeral=True)
            print("STOPPPP")
        except Exception as e:
            print(f"Task Cancelled? {e}")
            await Interaction.response.send_message(f"It doesn't seem like the bot is automatically fetching news... or an error occured. {e}")

def setup(bot):
    bot.add_cog(offnews(bot))
