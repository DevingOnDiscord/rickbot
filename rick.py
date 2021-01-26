import discord
from discord.ext import commands


client=commands.Bot(command_prefix="r?")

client.remove_command("help")

TOKEN = "Nzg4MTQwMDAxOTg4MzEzMDg5.X9fKkw.hy7ELPpK4QJL-ZsLBf7I76ksXsA"

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")
    await client.change_presence(activity=discord.Game('r?help | Rickbot V1.0'))


@client.command()
async def help(ctx):
    embed=discord.Embed(title="Rickbot V1.0 by Smirf123#5911")
    embed.add_field(name="`r?help`", value="Shows this menu")
    embed.add_field(name="`r?rick`", value="Rickrolls the server, it does have a cooldown so don't spam this command")
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rick(ctx):
    embed = discord.Embed(title="You now regret this", description="You have to wait to use this again", inline=True)
    embed.add_field(name="\u200b", value="Never gonna give you up", inline=True)
    embed.add_field(name="\u200b", value="Never gonna let you down", inline=True)
    embed.add_field(name="\u200b", value="Never gonna run around and desert you", inline=True)
    embed.add_field(name="\u200b", value="Never gonna make you cry", inline=True)
    embed.add_field(name="\u200b", value="Never gonna say goodbye", inline=True)
    embed.add_field(name="\u200b", value="Never gonna tell a lie and hurt you", inline=True)
    await ctx.send(embed=embed)

@rick.error
async def rick_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('You are on cooldown, wait a bit before doing it again')
client.run(TOKEN)
