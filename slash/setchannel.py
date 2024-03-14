from typing import Optional
import nextcord
import main, helper
from nextcord import Interaction
from nextcord.ext import commands

class setchannel(commands.Cog):
    global active_channel
    bot = main.bot

    @nextcord.slash_command(name="setchannel",description="Sets the channel where further commands will be executed")
    async def setChannel(self,Interaction:Interaction, channel: str):
        global active_channel
        try:
            active_channel = self.bot.get_channel(int(helper.verifyChannelIntegrity(channel)))
            helper.setGlobalActiveChannel(active_channel)
            await Interaction.response.send_message(content=f"Active channel has now been set to {active_channel}",ephemeral=True)
        except Exception as e:
            await Interaction.response.send_message(content=f"Invalid channel ID",ephemeral=True)
            print("No channel ID, or invalid channel ID was given")

def setup(bot):
    bot.add_cog(setchannel(bot))