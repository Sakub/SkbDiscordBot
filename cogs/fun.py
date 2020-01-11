import discord
from discord.ext import commands
import random
from config import Config

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        await ctx.send(random.choice(Config.eBallAnswers()))


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')

    @commands.command(aliases=['hOt'])
    async def headsOrTails(self, ctx):
        await ctx.send(random.choice(Config.headsOrTails()))
def setup(client):
    client.add_cog(Fun(client))