import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        user = ctx.message.author.name
        try:
            await member.kick(reason = reason)
        except Exception as e:
            await ctx.send(f'{user} you dont have permissions to do that!')
        else:
            await ctx.send(f'Kicked {member}! Reason: {reason}')

    @commands.command(pass_context = True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        user = ctx.message.author.name
        try:
            await member.ban(reason = reason)
        except Exception as e:
            await ctx.send(f'{user} you dont have permissions to do that!')
        else:
            await ctx.send(f'Banned {member}! Reason: {reason}')

    @commands.command(pass_context = True)
    async def unban(self, ctx, *, member):
        author = ctx.message.author.name
        try:
            banned_users = await ctx.guild.bans()
            memberName, memberDiscriminator = member.split('#')
            for banned_user in banned_users:
                user = banned_user.user

                if (user.name, user.discriminator) == (memberName, memberDiscriminator):
                    await ctx.guild.unban(user)
        except Exception as e:
            await ctx.send(f'{author} you dont have permissions to do that!')
        else:
            await ctx.send(f'{user.name} has been unbanned!')
            return
        

def setup(client):
    client.add_cog(Moderation(client))