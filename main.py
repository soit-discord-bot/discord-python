import discord
from discord.ext import commands
# from boto.s3.connection import S3Connection

# Use this for development
import os
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Bot is ready')


client.run(os.getenv('TOKEN'))
