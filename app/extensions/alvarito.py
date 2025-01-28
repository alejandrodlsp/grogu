from nextcord.ext import commands
import nextcord
from random import randint

class Alvarito(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command()
    async def random(self, ctx):
        ran = randint(0, 10)
        await ctx.send(f"Numero random: {ran}")
        
def setup(bot):
    bot.add_cog(Alvarito(bot))