'''
MAIN SCRIPT
This is the main script that runs which loads all cogs.
'''
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import json

#Loading the config file which has the bot token and default prefix stored

with open('Data/Config.json') as file:
    config = json.load(file)

token = config["token"]
prefix = config["prefix"]
botDevelopers = config["botDevelopers"]

#Listing all the cogs
startup_extensions = ["Eval", "Info", "Mod"]

#Defining the bot's default prefix and description
client = Bot(description='A multitasking bot created by Hades#6871!', command_prefix=prefix)

#Removing the built-in help command
client.remove_command('help')

#Changing the playing status and adding some console logs when the bot is started
@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name = 'Type {}help'.format(prefix)))
    print("-" * 20)
    print("Logged in as: {}".format(client.user.name))
    print("BOT ID: {}".format(client.user.id))
    print("Guilds: {}".format(str(len(client.guilds))))
    print("Members: {}".format(str(sum(1 for _ in client.get_all_members()))))
    print("Discord.py version: {}".format(discord.__version__))
    print("Python version: {} \n".format(platform.python_version()))
    print("Invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8 \n".format(client.user.id))
    print("Status: Under development \n")
    print("Developed by the Pluto Development Team")
    print("\t> Hades#6871")
    print("\t> jacob#0513")
    print("\t> Greem.exe#5501")
    print("-" * 20)

#Broadcast command that sends a message to all server owners. DO NOT USE UNLESS URGENT
@client.command()
async def broadcast(ctx, msg : str):
    if ctx.author.id in botDevelopers:
        for guild in client.guilds:
            await guild.owner.send(msg)
    else:
        pass

#Command to change the playing status of the bot [Bot Developers only]
@client.command()
async def changestatus(ctx, *status : str):
    if ctx.author.id in botDevelopers:
        await client.change_presence(game = discord.Game(name = status))
        embed = discord.Embed(title='Bot status change!', description='**Current/New status**: {}'.format(status), color = 0x195ac4)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        pass

#Command to shutdown the bot [Bot Developers only]
@client.command(aliases = ['logout', 'disconnect'])
async def shutdown(ctx):
    if ctx.author.id in botDevelopers:
        embed = discord.Embed(title = "Shutting down...", description = ":zzz:", color = 0x195ac4)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        await client.logout()
        exit()
    else:
        pass

#Loading the cogs in the list (startup_extensions)
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run(token)
