from nextcord.ext import commands
import nextcord

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Bienvenido, {member.mention}!")
            
    @commands.command()
    async def hola(self, ctx, *, member: nextcord.Member = None):
        """Dice hola"""
        member = member or ctx.author
        await ctx.send(f'Hola {member.name}~')
        
    @commands.command()
    async def caracola(self, ctx):
        """Dice caracola"""
        await ctx.send("Caracola jijiji")
    
    @hola.error
    async def hola_error(self, ctx, error):
        await ctx.send(f'Hola {error.message} ha fallado')
        
def setup(bot):
    bot.add_cog(Greeting(bot))