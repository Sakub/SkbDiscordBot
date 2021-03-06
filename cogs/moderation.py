import discord
from discord.ext import commands
from discord.utils import get
from config import Config

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

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await member.ban(reason = reason)
        except Exception as e:
            await ctx.send(f'Something went wrong!')
        else:
            await ctx.send(f'Banned {member}! Reason: {reason}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')


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

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def mute(self,ctx, member : discord.Member, *, reason = None):
        user = ctx.message.author
        try:
            role = discord.utils.get(user.guild.roles, name='Muted')
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been muted! Reason: {reason}')
        except Exception as e:
            await ctx.send(f'Something went wrong!')
        
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def unmute(self, ctx, member: discord.Member):
        user = ctx.message.author
        try:
            role = discord.utils.get(user.guild.roles, name='Muted')
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been unmuted!')
        except Exception as e:
            await ctx.send(f'Something went wrong!')

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def warn(self, ctx, member: discord.Member, *, reason = None):
        await ctx.send(f'{member.mention}! You have been warned! Reason: {reason}')
    
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')



    @commands.command(pass_context = True)
    @commands.has_role('Admin')
    async def announc(self, ctx, *, message = None):
        await ctx.send('@here')
        await ctx.send(f'```Attention! \n{message}```')

    @announc.error
    async def announc_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    @commands.command()
    @commands.has_role('Admin')
    async def clear(self, ctx, amount = 3):
        try:
            if amount > 50:
                await ctx.send('Number of messages to clear is too high!')
            elif amount < 1:
                await ctx.send(f"Can't clear {amount} message(s)")
            else:
                await ctx.channel.purge(limit=amount)
        except Exception as e:
            await ctx.send(f'Something went wrong!')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{self.permissionErrorMessage(ctx)}')

    def permissionErrorMessage(self, ctx):
        author = ctx.message.author.mention
        message = f'{author} {Config.permissionErrorMessage()}'
        return message


def setup(client):
    client.add_cog(Moderation(client))