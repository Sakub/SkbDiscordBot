import discord
from discord.ext import commands
from discord.utils import get

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        try:
            await member.kick(reason = reason)
        except Exception as e:
            await ctx.send(f'Something went wrong!')
        else:
            await ctx.send(f'Kicked {member}! Reason: {reason}')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await member.ban(reason = reason)
        except Exception as e:
            await ctx.send(f'Something went wrong!')
        else:
            await ctx.send(f'Banned {member}! Reason: {reason}')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            memberName, memberDiscriminator = member.split('#')
            for banned_user in banned_users:
                user = banned_user.user

                if (user.name, user.discriminator) == (memberName, memberDiscriminator):
                    await ctx.guild.unban(user)
        except Exception as e:
            await ctx.send(f'Something went wrong!')
        else:
            await ctx.send(f'{user.name} has been unbanned!')
            return

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def unmute(self, ctx, member: discord.Member):
        user = ctx.message.author
        try:
            role = discord.utils.get(user.guild.roles, name='Muted')
            await member.remove_roles(role)
            await ctx.send(f'{member} has been unmuted!')
        except Exception as e:
            await ctx.send(f'Something went wrong!')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def warn(self, ctx, member: discord.Member, *, reason = None):
        await ctx.send(f'{member}! You have been warned! Reason: {reason}')
    
    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def announc(self, ctx, *, message = None):
        await ctx.send('@here')
        await ctx.send(f'```Attention! \n{message}```')
        

def setup(client):
    client.add_cog(Moderation(client))