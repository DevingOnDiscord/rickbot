import discord
from discord.ext import commands


client=commands.Bot(command_prefix="r?")

client.remove_command("help")

TOKEN = "No Token 4 U"

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
    await ctx.channel.send("Never gonna give you up")
    await ctx.channel.send("Never gonna let you down")
    await ctx.channel.send("Never gonna run around and desert you")
    await ctx.channel.send("Never gonna make you cry")
    await ctx.channel.send("Never gonna say goodbye")
    await ctx.channel.send("Never gonna tell a lie and hurt you")
    await ctx.channel.send("Now you gotta wait before I can rickroll again")

@rick.error
async def rick_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('You are on cooldown, wait a bit before doing it again')
client.run(TOKEN)
