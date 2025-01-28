from nextcord.ext import commands
import nextcord

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")
                
def setup(bot):
    bot.add_cog(Events(bot))