from app.app import bot
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    
    discord_token = os.environ['DISCORD_TOKEN']
    
    bot.run(discord_token)