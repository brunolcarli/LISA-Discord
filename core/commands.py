import discord
from discord.ext import commands
from lisa.settings import BACKEND_URL, __version__
from core.connections import GraphQLQuery

bot = commands.Bot(command_prefix='l>')


@bot.event
async def on_ready():
    print('Runnin smooth!')


@bot.command(aliases=['v'])
async def version(ctx):
    """
    Bot version
    """
    service_version = GraphQLQuery.lisa_service_version()
    response = f'''
    Bot version: {__version__}
    Service version: {service_version}
    '''
    return await ctx.send(response)
