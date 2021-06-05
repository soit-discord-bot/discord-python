import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Bot is ready')


client.run('TOKEN')