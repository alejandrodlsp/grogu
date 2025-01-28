from nextcord.ext import commands
import nextcord
import os

def build_intents():
    intents = nextcord.Intents.default()
    intents.message_content = True
    return intents

bot = commands.Bot(
                    command_prefix="!", 
                    intents=build_intents()
                )

# Load Extensions
for extpath in os.listdir("app/extensions"):
    if extpath.endswith(".py"):
        bot.load_extension(f'app.extensions.{extpath[:-3]}')