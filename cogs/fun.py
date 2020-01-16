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

    @commands.command(aliases=['rMeme'])
    async def redditmeme(self, ctx, subreddit = 'DankMemes', amount = 3):
        try:
            subr = Config.redditClient().subreddit(subreddit)
            hotSubr = subr.hot(limit=amount)
            for submission in hotSubr:
                if not submission.stickied:
                    if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                        await ctx.send(submission.url)
        except:
            await ctx.send(f'Error! Subreddit: {subr} not found!')
def setup(client):
    client.add_cog(Fun(client))