import discord
from discord.ext import commands
from config import Config
import random
import os
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def greet(ctx):
    user = ctx.message.author.name
    await ctx.send(f'Hello {user}')

@bot.command()
async def users(ctx):
    listOfUsers = ''
    guild = discord.utils.find(lambda g: g.name==Config.guildName(), bot.guilds)
    await ctx.send('```List of users:```')
    for index, member in enumerate(guild.members, start=1):
        listOfUsers += f'```{index}. {member} \n```'
    await ctx.send(listOfUsers)

@bot.command(pass_context = True)
async def bye(ctx):
    user = ctx.message.author.name
    await ctx.send(f'Bye {user}!')

@bot.command()
@commands.has_role('Admin')
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension loaded')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(permissionErrorMessage(ctx))

@bot.command()
@commands.has_role('Admin')
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(permissionErrorMessage(ctx))

@bot.command()
@commands.has_role('Admin')
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded')

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(permissionErrorMessage(ctx))

def permissionErrorMessage(ctx):
    author = ctx.message.author.mention

    message = f'{author}! {Config.permissionErrorMessage()}'
    return message


for filename in os.listdir(Config.cogsPath()):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(Config.token())