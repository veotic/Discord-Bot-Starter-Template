import discord
from discord.ext import commands
import random

# Creates discord client starter command
client = commands.Bot(command_prefix='c!')

# Command that inform users the version of the bot
@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Bot Name", description="#", color=0x1C1EB0)
    myEmbed.add_field(name="Version:", value="#", inline=False)
    myEmbed.add_field(name="Date Released:", value="#", inline=False)
    myEmbed.set_footer(text="#")

    await context.message.channel.send(embed=myEmbed)


# You put the command names here. Change it for your preference
@client.command(name="commands")
async def commands(ctx):
    # Put command list here. For EX: "Commands: `c!version`, `c!copy @message`, `c!randompic`, `c!memes`, `c!roastme`, `c!roast @ping`, `c!compliment @ping`"
    await ctx.send("#P")


@client.command()
async def copy(ctx, arg):
    await ctx.send(arg)


# This command will send users a random picture
@client.command(name="randompic")
async def randompic(context):
    # Put images here
    images = ["#", "#", "#"]

    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))


# This command will send users a random meme
@client.command(name="memes")
async def memes(context):
    # Put images here
    images1 = ["#", "#", "#"]

    random_image1 = random.choice(images1)

    await context.send(file=discord.File(random_image1))


@client.command(name="roastme")
async def roastme(ctx):
    # Put the roast messages here
    variables2 = ["#", "#", "#"]

    # This command will let users ping others with a message
    await ctx.send(f"{ctx.author.mention} {random.choice(variables2)}")


# This command will let users ping others for a requested roast. The bot will then ping the mentioned users with the roast
@client.command(name="roast")
async def roast(ctx, user: discord.Member):
    # Put the roast messages here
    variables3 = ["#", "#", "#"]

    await ctx.send(f"{user.mention} {random.choice(variables3)}")


@client.command(name="compliment")
async def compliment(ctx, user: discord.Member):
    variables4 = ["#", "#", "#"]

    await ctx.send(f"{user.mention} {random.choice(variables4)}")


# Runs the client on the server
client.run('#Put the secret token here from Discord')


