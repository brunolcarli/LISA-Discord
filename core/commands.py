import discord
from discord.ext import commands
from lisa.settings import BACKEND_URL, __version__


bot = commands.Bot(command_prefix='l>')


@bot.event
async def on_ready():
    print('Runnin smooth!')


@bot.command(aliases=['v'])
async def version(ctx):
    """
    Bot version
    """
    return await ctx.send(__version__)
