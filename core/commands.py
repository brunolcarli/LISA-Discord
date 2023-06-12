import discord
from discord.ext import commands
from lisa.settings import BACKEND_URL, __version__
from core.connections import GraphQLQuery



intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix='l:', intents=intents)


@client.event
async def on_ready():
    print('Runnin smooth!')


@client.slash_command(name='version', description='Return bot current version')
async def version(ctx):
    """
    Bot version
    """
    service_version = GraphQLQuery.lisa_service_version()
    response = f'''
    Bot version: {__version__}
    Service version: {service_version}
    '''
    await ctx.respond(response, ephemeral=True)

@client.command()
async def sentiment_extraction(ctx, *text):
    """
    Versão do bot
    """
    text=" ".join(i for i in text)
    sentiment = GraphQLQuery.lisa_sentiment_extraction(text)

    return await ctx.send(sentiment)