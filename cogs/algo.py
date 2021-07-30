import discord
from discord.ext import commands
import json

class Algorithm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases = ['algo', 'algorithm'])
    async def _algoType(self, ctx, *, request):
        f = open('data.json',)
        data = json.load(f)
        for i in range(len(data)):
            await ctx.send(data[i])

def setup(client):
    client.add_cog(Algorithm(client))
