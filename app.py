import discord
from discord.ext import commands
from config import Config
import random
import os
bot = commands.Bot(command_prefix='!')

@bot.command()
async def clear(ctx, amount = 3):
    try:
        if amount > 50:
            await ctx.send('Number of messages to clear is too high!')
        elif amount < 1:
            await ctx.send(f"Can't clear {amount} message(s)")
        else:
            await ctx.channel.purge(limit=amount)
    except Exception as e:
        await ctx.send(f'Something went wrong! Error message: {e}')

@bot.command(pass_context=True)
async def greet(ctx):
    user = ctx.message.author.name
    await ctx.send(f'Hello {user}')

@bot.command()
async def users(ctx):
    guild = discord.utils.find(lambda g: g.name==Config.guildName(), bot.guilds)
    await ctx.send('```List of users:```')
    for index, member in enumerate(guild.members, start=1):
        await ctx.send(f'```{index}. {member}```')

@bot.command(pass_context = True)
async def bye(ctx):
    user = ctx.message.author.name
    await ctx.send(f'Bye {user}!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded')


for filename in os.listdir(Config.cogsPath()):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(Config.token())