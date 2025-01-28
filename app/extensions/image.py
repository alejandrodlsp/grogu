from nextcord.ext import commands
from nextcord import File
import nextcord

from app.helpers.image.generation import ImageText

class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command()
    async def perro(self, ctx, *args):
        """Dice hola"""
        msg = " ".join(args)
        img = ImageText("resources/images/dog.jpg", msg, (500, 260), 50)
        img_path = img.generate()
        
        with open(img_path, "rb") as f:
            await ctx.channel.send(file=File(f, filename="perro.png"))
        img.purge()
    
    @perro.error
    async def perro_error(self, ctx, error):
        await ctx.send(f'El comando ha fallado con error: {error.message}')
        
def setup(bot):
    bot.add_cog(Image(bot))