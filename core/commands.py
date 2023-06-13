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
    await ctx.respond(response, ephemeral=False)


@client.slash_command(name='sentiment', description='Return text sentiment')
async def sentiment_extraction(ctx, text):
    """
    Return text polarity
    """
    sentiment = GraphQLQuery.lisa_sentiment_extraction(text)

    await ctx.respond(sentiment, ephemeral=False)


@client.slash_command(name='text_offense', description='Return text offense level')
async def text_offense(ctx, text):
    """
    Return text offense level
    """
    embed = discord.Embed(color=0x1E1E1E, type='rich')
    data = GraphQLQuery.text_offense_level(text)

    if 'ERROR' in data:
        return await ctx.respond(data, ephemeral=False)


    embed.add_field(name='Text:', value=text, inline=False)
    embed.add_field(name='Average:', value=data.get('average'), inline=True)
    embed.add_field(name='Is offensive:', value=data.get('isOffensive'), inline=True)

    await ctx.respond('', embed=embed, ephemeral=False)
