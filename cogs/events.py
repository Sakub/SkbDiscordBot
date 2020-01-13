import discord
from discord.ext import commands
from config import Config

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged as {self.client.user}')

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        print(f'{user} is writting a message on channel: {channel}')
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(f'{self.client.user} has deleted a message! Content: {message.content}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{message.author} has sent a message! Content: {message.content}')

def setup(client):
    client.add_cog(Events(client))
