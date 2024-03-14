import nextcord
import main, helper
from nextcord import Interaction
from nextcord.ext import commands

class resetblacklist(commands.Cog):
    bot = main.bot

    @nextcord.slash_command(name="reset_blacklist", description="Resets the current blacklist for autonews")
    async def resetList(self, Interaction: Interaction):
        helper.blacklist = []
        Interaction.response.send_message(f"The blacklist has been reset!")

def setup(bot):
    bot.add_cog(resetblacklist(bot))