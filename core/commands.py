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


@client.slash_command(name='similarty', description='Return similarity between two words separated by ,')
async def similarity(ctx, text):
    """
    Return similarity between two words
    """

    if ',' not in text:
        return await ctx.respond('Separate two words by `,`', ephemeral=False)

    a, b, *_ = text.split(',')

    data = GraphQLQuery.similarity(a, b)

    await ctx.respond(data, ephemeral=False)


@client.slash_command(name='pos_tag', description='Return the Part of Speech Tags')
async def pos_tag(ctx, text):
    """
    Return part of speech tags
    """
    embed = discord.Embed(color=0x1E1E1E, type='rich')
    data = GraphQLQuery.part_of_speech(text)

    if 'ERROR' in data:
        return await ctx.respond(data, ephemeral=False)


    embed.add_field(name='Text:', value=text, inline=False)
    for i in data:
        embed.add_field(name=i.get('token'), value=i.get('description'), inline=True)

    await ctx.respond('', embed=embed, ephemeral=False)


@client.slash_command(name='dependency', description='Return the dependency parse of the text')
async def dependency(ctx, text):
    """
    Return dependency parse of the text
    """
    embed = discord.Embed(color=0x1E1E1E, type='rich')
    data = GraphQLQuery.dependency_parse(text)

    if 'ERROR' in data:
        return await ctx.respond(data, ephemeral=False)

    embed.add_field(name='Text:', value=text, inline=False)
    for i in data:
        children = ' - '.join(i.get('children')).strip()
        ancestors = ' - '.join(i.get('ancestors')).strip()
        value = f'Children: {children}\nAncestors: {ancestors}'
        embed.add_field(name=i.get('element'), value=value, inline=False)

    await ctx.respond('', embed=embed, ephemeral=False)