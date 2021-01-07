'''
MAIN SCRIPT
This is the main script that runs which loads all cogs.
'''
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import platform
import json
import datetime
import aiohttp
import sys
import traceback


#Loading the config file which has the bot token and default prefix stored
with open("Data/config.json", "r") as f:
    config = json.load(f)

token = config["token"]
prefix = config["prefix"]
botDevelopers = config["botDevelopers"]

async def get_pre(bot, message):
    with open("Data/prefix.json", "r") as f:
        prefixList = json.load(f)
    guild = str(message.guild.id)
    if guild in prefixList:
        return prefixList[guild]
    else:
        return prefix

#Listing all the cogs
startup_extensions = ["Eval", "Info", "Mod", "Tags", "Fun", "Giphy", "Roles"]

#Defining the bot's default prefix and description
client = Bot(description='A multitasking bot created by Aryan#6666!', command_prefix=get_pre)

#Removing the built-in help command
client.remove_command('help')


#Changing the playing status and adding some console logs when the bot is started
@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name = 'Type {}help'.format(prefix)))
    print("=" * 20)
    print("Logged in as: {}".format(client.user.name))
    print("BOT ID: {}".format(client.user.id))
    print("Guilds: {}".format(len(client.guilds)))
    print("Members: {}".format(sum(1 for user in client.get_all_members())))
    print("Discord.py version: {}".format(discord.__version__))
    print("Python version: {} \n".format(platform.python_version()))
    print("Invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8 \n".format(client.user.id))
    print("Status: Under development \n")
    print("Developed by Hades#6871")
    print("=" * 20)

#Broadcast command that sends a message to all server owners. DO NOT USE UNLESS URGENT
@client.command()
async def broadcast(ctx, msg : str):
    if ctx.author.id in botDevelopers:
        for guild in client.guilds:
            await guild.owner.send(msg)
    else:
        pass

@client.event
async def on_member_join(member):
    with open("Data/autoroles.json", "r") as f:
        arolelist = json.load(f)
    try:
        arole = arolelist[str(member.guild.id)]
        for role in arole:
            autorole = discord.utils.find(lambda r: r.id == role, member.guild.roles)
            await member.add_roles(autorole, reason = "Autorole")
    except:
        pass
    with open("Data/logging.json", "r") as f:
        loglist = json.load(f)
    try:
        logsChannel = loglist[str(member.guild.id)]['log']
        logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
        embed = discord.Embed(title = "New Member", description = ":tada: {} has just joined the server!\n\n:busts_in_silhouette: You now have ``{}`` members on your server".format(member.mention, member.guild.member_count), color = 0x195ac4)
        embed.set_thumbnail(url = member.avatar_url)
        await logsChannel.send(embed = embed)
    except:
        pass

@client.event
async def on_member_remove(member):
    with open("Data/logging.json", "r") as f:
        loglist = json.load(f)
    try:
        logsChannel = loglist[str(member.guild.id)]['log']
        logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
        embed = discord.Embed(title = "Member left", description = ":eye_in_speech_bubble: {} has just left the server\n\n:busts_in_silhouette: You now have ``{}`` members on your server".format(member.mention, member.guild.member_count), color = 0x195ac4)
        embed.set_thumbnail(url = member.avatar_url)
        await logsChannel.send(embed = embed)
    except:
        pass

@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title = "Hello - I'm PlutoBot!", description = "I'll help you keep your server in shape 24/7! You can discover my various modules by using the ``>>help`` command\n<@345318328195350528> is my creator, and you can join his support server (https://discord.gg/qTNEgPD) anytime regarding any issues or queries about me - feedback and suggestions are appreciated!", color = 0x195ac4)
    await guild.owner.send(embed = embed)

@client.event
async def on_guild_remove(guild):
    with open("Data/logging.json", "r") as f:
        loglist = json.load(f)
    try:
        del loglist[str(guild.id)]
        with open("Data/logging.json", "w") as f:
            json.dump(loglist, f)
    except:
        pass
    with open("Data/autoroles.json", "r") as f:
        arolelist = json.load(f)
    try:
        del arolelist[str(guild.id)]
        with open("Data/autoroles.json", "w") as f:
            json.dump(arolelist, f)
    except:
        pass
    with open("Data/selfroles.json", "r") as f:
        srolelist = json.load(f)
    try:
        del srolelist[str(guild.id)]
        with open("Data/selfroles.json", "w") as f:
            json.dump(srolelist, f)
    except:
        pass
    with open("Data/tags.json", "r") as f:
        taglist = json.load(f)
    try:
        del taglist[str(guild.id)]
        with open("Data/tags.json", "w") as f:
            json.dump(taglist, f)
    except:
        pass
    with open("Data/warn.json", "r") as f:
        warnlist = json.load(f)
    try:
        del warnlist[str(guild.id)]
        with open("Data/warn.json", "w") as f:
            json.dump(warnlist, f)
    except:
        pass
    with open("Data/prefix.json", "r") as f:
        prefixlist = json.load(f)
    try:
        del prefixlist[str(guild.id)]
        with open("Data/prefix.json", "w") as f:
            json.dump(prefixlist, f)
    except:
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

@client.command(name = "reload")
async def _reload(ctx, cogname):
    if ctx.author.id in botDevelopers:
        try:
            client.unload_extension(cogname)
            client.load_extension(cogname)
            embed = discord.Embed(title = "Reloading cog...", description = "**{}** has been reloaded".format(cogname), color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            await ctx.send("```{}```".format(exc))
    else:
        pass

@client.event
async def on_command_error(ctx, exception):
    if isinstance(commands.CommandNotFound, commands.UserInputError):
        return
    else:
        embed = discord.Embed(title = "Command Error Log", description = "**Guild ID**: {}\n**Guild Name**: {}\n**Command**: {}".format(str(ctx.guild.id), ctx.guild.name, ctx.command), color = 0x195ac4)
        embed.add_field(name = "Error:", value = "```{}```".format(exception))
        embed.set_footer(text = datetime.datetime.now())
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url("https://canary.discordapp.com/api/webhooks/410686627653091340/qcyKV1r7-XAAFs8aNHQWHllmTsbVKezDB0OvRcdJ0-3Y2hgRpcXf5pBn0rX7Ma8e4k4K", adapter = AsyncWebhookAdapter(session))
            await webhook.send(embed = embed)

@client.event
async def on_error(exception):
    embed = discord.Embed(title = "Client Error Log", description = "```{}```".format(exception), color = 0x195ac4)
    embed.set_footer(text = datetime.datetime.now())
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url("https://canary.discordapp.com/api/webhooks/410686627653091340/qcyKV1r7-XAAFs8aNHQWHllmTsbVKezDB0OvRcdJ0-3Y2hgRpcXf5pBn0rX7Ma8e4k4K", adapter = AsyncWebhookAdapter(session))
        await webhook.send(embed = embed)


#Loading the cogs in the list (startup_extensions)
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run(token)
