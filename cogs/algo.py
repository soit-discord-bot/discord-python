import discord
from discord.ext import commands
import json

class Algorithm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """
        Checks for Ping for bot
        """
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases = ['algo', 'algorithm'])
    async def _algoType(self, ctx, *, request):
        """
        Checks if Algorithm has a Sub Type and sends respective embed
        """
        # Loads Json File
        f = open('data_final.json',)
        data = json.load(f)

        # Separating Algorithms with their presence of subtypes
        others = ['binary', 'bfs', 'dfs', 'dijkstra', 'bellman', 'floyd', 'prim', 'kruskal']

        # Checks if Algorithm is a Sub Type
        if request.lower() in others:

            # if Algorithm has no sub types, sets appropriate json hierachy
            for i in range(1, len(data)):
                for j in range(len(data[i]['algos'])):
                    if request.lower() in data[i]['algos'][j]['algo_name'].lower():

                        # Sets Algorithm
                        algorithm = data[i]['algos'][j]

                        # Calls Embed Creation Function
                        await ctx.invoke(self.client.get_command('algoSend2'), algorithm=algorithm)

        elif request.lower() not in others:

            # if Algorithm has sub types, sets appropriate json hierachy
            for i in range(len(data[0]['algo_subtype'])):
                for j in range(len(data[0]['algo_subtype'][i]['algos'])):

                    if request.lower() in data[0]['algo_subtype'][i]['algos'][j]['algo_name'].lower():

                        # Sets Algorithm Sub Type and Algorithm
                        algorithm = data[0]['algo_subtype'][i]['algos'][j]
                        sub_name = data[0]['algo_subtype'][i]['algo_subtype_name']

                        # Calls Embed Creation Function
                        await ctx.invoke(self.client.get_command('algoSend'), algorithm=algorithm, sub_name=sub_name)


    @commands.command()
    async def algoSend(self, ctx, algorithm: object, sub_name: str):
        """
        Creates Embed for Algorithm with Sub Type
        """
        # Sets variables
        title = algorithm['algo_name']
        span = algorithm['algo_name']

        # Sets Description
        description = ""
        for i in range(len(algorithm['algo_desc'])):
            description += algorithm['algo_desc'][i] + "\n\n"

        # Creates Embed
        algoEmbed = discord.Embed(title=title, description=sub_name, color=0x00ff00)
        algoEmbed.add_field(name="Description\n", value=description, inline=False)

        algo_props = algorithm['algo_props']
        for i in range(len(algo_props)):
            algoEmbed.add_field(name=algo_props[i]['algo_props_title'], value=algo_props[i]['algo_props_desc'][0], inline=False)

        algo_complexity = algorithm['algo_complexity']
        algoEmbed.add_field(name="Algorithm Time Compelxity", value=algo_complexity['time'][0], inline=False)
        algoEmbed.add_field(name="Algorithm Space Complexity", value=algo_complexity['aux_space'][0], inline=False)

        # Sends Embed
        await ctx.channel.send(embed=algoEmbed)

    @commands.command()
    async def algoSend2(self, ctx, algorithm: object):
        """
        Creates Embed for Algorithm without Sub Type
        """
        # Sets variables
        title = algorithm['algo_name']
        span = algorithm['algo_name']

        # Sets Description
        description = ""
        for i in range(len(algorithm['algo_desc'])):
            description += algorithm['algo_desc'][i] + "\n\n"

        # Creates Embed
        algoEmbed = discord.Embed(title=title, description=title, color=0x00ff00)
        algoEmbed.add_field(name="Description\n", value=description, inline=False)

        algo_props = algorithm['algo_props']
        for i in range(len(algo_props)):
            algoEmbed.add_field(name=algo_props[i]['algo_props_title'], value=algo_props[i]['algo_props_desc'], inline=False)

        algo_complexity = algorithm['algo_complexity']
        algoEmbed.add_field(name="Algorithm Time Compelxity", value=algo_complexity['time'][0], inline=False)

        # Sends Embed
        await ctx.channel.send(embed=algoEmbed)

def setup(client):
    client.add_cog(Algorithm(client))
