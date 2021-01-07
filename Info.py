import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
import aiohttp
import json

class Info:
    def __init__(self, bot):
        self.bot = bot

    #Creating a command group for help
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title = "**Help Categories**", description = "\n:tools: **Moderation** :tools:\n\n\n:notepad_spiral: **Info** :notepad_spiral:\n\n\n:space_invader: **Fun** :space_invader:\n\n\n:scroll: **Roles** :scroll:\n\n\n:warning: **Warning** :warning:\n\n\n:pushpin: Tags :pushpin:\n\n\n**Type help <category> to know more about a module!**\n", color = 0x195ac4)
            embed.set_thumbnail(url = ctx.guild.icon_url)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    #Sub-command for Moderation help
    @help.command(aliases = ['Moderation', 'mod', 'Mod'])
    async def moderation(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Moderation**", color = 0x195ac4)
        embed.add_field(name = "**Set prefix**", value = '```bash\nUse "setprefix <prefix>" to change the server prefix```', inline = False)
        embed.add_field(name = "**Lockdown**", value = '```bash\nUse "lockdown <reason>" to lockdown a channel or the entire server```', inline = False)
        embed.add_field(name = "**Lift lockdown**", value = '```bash\nUse "unlock <reason>" to unlock a channel or the entire server```', inline = False)
        embed.add_field(name = "**Logging**", value = '```bash\nUse "logging" to setup loggin for your server```', inline = False)
        embed.add_field(name = "**Purge**", value = '```bash\nUse "purge <number>" to delete up to 100 messages.\n Alias: prune```', inline = False)
        embed.add_field(name = "**Mute**", value = '```bash\nUse "mute <user> <reason>" to mute a user.\n Alias: gag```', inline = False)
        embed.add_field(name = "**Unmute**", value = '```bash\nUse "unmute <user> <reason>" to unmute a user.\n Alias: ungag```', inline = False)
        embed.add_field(name = "**Kick**", value = '```bash\nUse "kick <@name> <reason>" to kick a user from the server.```', inline = False)
        embed.add_field(name = "**Ban**", value = '```bash\nUse "ban <@name> <numbers of days of message deletion> <reason>" to permanently ban a user from the server.```', inline = False)
        embed.add_field(name = "**Unban**", value = '```bash\nUse "unban <name> <reason>" to unban a user from the server.```', inline = False)
        embed.set_thumbnail(url = 'https://pbs.twimg.com/profile_images/861759703864401920/HsF77Zw2.jpg')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Info help
    @help.command(aliases = ['Info'])
    async def info(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Info**", color = 0x195ac4)
        embed.add_field(name = "**Ping**", value = '```bash\nUse "ping" to test the latency of the bot.```', inline = False)
        embed.add_field(name = "**Roles**", value = '```bash\nUse "roles" to see the roles in the server in hierarchy.```', inline = False)
        embed.add_field(name = "**Server Stats**", value = '```bash\nUse "server" for server stats.```', inline = False)
        embed.add_field(name = "**Bot Stats**", value = '```bash\nUse "about" for bot stats.\n Aliases: bot```', inline = False)
        embed.add_field(name = "**Member**", value = '```bash\nUse "member <first letters of user>" to return a user matching your query.```', inline = False)
        embed.set_thumbnail(url = 'https://cdn.pixabay.com/photo/2016/03/31/19/13/information-1294813_960_720.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Fun help
    @help.command(aliases = ['Fun'])
    async def fun(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Fun**", color = 0x195ac4)
        embed.add_field(name = "**Choices**", value = '```bash\nUse "choose <value> <value> <value>" to choose between multiple things. There is a required argument of three choices.```', inline = False)
        embed.add_field(name = "**Giphy Search**", value = '```bash\nUse "gif <query>" to display a random gif related to your query.```', inline = False)
        embed.add_field(name = "**Embed**", value = '```bash\nUse "embed <something>" to embed your message through the bot.```', inline = False)
        embed.add_field(name = "**Whisper**", value = '```bash\nUse "whisper <something>" to say something anonymously via the bot.```', inline = False)
        embed.add_field(name = "**Urban**", value = '```bash\nUse "urban <query>" to look up your query on UrbanDictionary.```', inline = False)
        embed.set_thumbnail(url = 'http://d2trtkcohkrm90.cloudfront.net/images/emoji/apple/ios-10/256/alien-monster.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Roles help
    @help.command(aliases = ['Roles'], name = 'roles')
    async def _roles(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Roles**", color = 0x195ac4)
        embed.add_field(name = "**Roles List**", value = '```bash\nUse "roles" to view a list of server roles, self roles, and auto roles.```', inline = False)
        embed.add_field(name = "**Use Self Roles**", value = '```bash\nUse "sroles" to enable/disable the module for your server.```', inline = False)
        embed.add_field(name = "**Add Self Role**", value = '```bash\nUse "addsrole <role>" to allow users to give themselves that role.```', inline = False)
        embed.add_field(name = "**Remove Self Role**", value = '```bash\nUse "removesrole <role>" to remove allowing users to give themselves that role.```', inline = False)
        embed.add_field(name = "**Add Role**", value = '```bash\nUse "addme <role>" to add yourself to a role in the self given roles list.```', inline = False)
        embed.add_field(name = "**Remove Role**", value = '```bash\nUse "removeme <role>" to remove a role that you gave yourself.```', inline = False)
        embed.add_field(name = "**Use Auto Roles**", value = '```bash\nUse "aroles" to enable/disable auto roles.```', inline = False)
        embed.add_field(name = "**Add Auto Role**", value = '```bash\nUse "addarole <role>" to give a role to users automatically when they join```', inline = False)
        embed.add_field(name = "**Remove Auto Role**", value = '```bash\nUse "removearole <role>" to remove a role from the auto role list.```', inline = False)
        embed.set_thumbnail(url = 'http://www.subseatarget.com/wp-content/themes/subseatarget/images/st-roles-big.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @help.command(aliases = ['Warning', 'Warnings', 'warnings', 'warns', 'warn'])
    async def warning(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Warning System**", color = 0x195ac4)
        embed.add_field(name = "**Warning**", value = '```bash\nUse "warning" to enable the bot\'s warning system```', inline = False)
        embed.add_field(name = "**Warn**", value = '```bash\nUse "warn <user mention> <reason>" to warn a user```', inline = False)
        embed.add_field(name = "**Warns**", value = '```bash\nUse "warns <user mention>" to view a user\'s warns [Staff only]. Use "warns" to view your own warns```', inline = False)
        embed.add_field(name = "**Delete warns**", value = '```bash\nUse "deletewarns <user mention>" to delete a user\'s warn(s)```', inline = False)
        await ctx.send(embed = embed)

    @help.command(aliases = ['Tag', 'tags', 'Tags'])
    async def tag(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Tags**", color = 0x195ac4)
        embed.add_field(name = "**View tags**", value = '```bash\nUse "tags" to view all tags made by you```', inline = False)
        embed.add_field(name = "**Create tag**", value = '```bash\nUse "tags create" to create a new tag```', inline = False)
        embed.add_field(name = "**View all tags**", value = '```bash\nUse "tags all" to view all the tags on the server```', inline = False)
        embed.add_field(name = "**Delete tag**", value = '```bash\nUse "tags delete" to delete a tag(s)```', inline = False)
        embed.add_field(name = "**View tag**", value = '```bash\nUse "tag <name>" to view the content of a tag```', inline = False)
        await ctx.send(embed = embed)

    #Returns info about the bot
    @commands.command(aliases = ['bot'])
    async def about(self, ctx):
        embed = discord.Embed(title = "PlutoBot Stats", description = "Created by **Hades#6871**\n\nCurrently running **Version** ``3.0.1``\n\nConnected to **{}** servers\n\nUsed by **{}** people\n\nHere's an invite to our Discord - **https://discord.gg/qTNEgPD** - anyone can join!\n\nUse **https://bot.discord.io/plutobot** to invite **PlutoBot** to your own server!\n\nLibrary: discord.py {}".format(str(len(self.bot.guilds)),str(len(set(self.bot.users))), discord.__version__), color = 0x195ac4)
        embed.set_thumbnail(url = "https://i.imgur.com/IOxDNoh.png")
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Returns a server's statistics
    @commands.command(aliases = ['guild'])
    async def server(self, ctx):
        embed = discord.Embed(title = "Server Stats", description = "This server is called **{}**\n\n**<@{}>** is the owner\n\nIt is located in **{}** region\n\nThere are **{}** members in the server\n\nThe server was created at **{} (UTC)**\n\n".format(ctx.guild, ctx.guild.owner.id, ctx.guild.region, ctx.guild.member_count, ctx.guild.created_at), color = 0x195ac4)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #A command to return the invite for PlutoBot
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title = "", description = "Want PlutoBot on your own server?\n\nClick on **https://bot.discord.io/plutobot**\nto invite **PlutoBot** to your server!", color = 0x195ac4)
        embed.set_thumbnail(url = "https://i.imgur.com/IOxDNoh.png")
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Ping command - syncs with the Discord website and returns with latency
    @commands.command()
    async def ping(self, ctx):
        session = aiohttp.ClientSession(loop = self.bot.loop)
        start = time.time()
        async with session.get("https://discordapp.com"):
            duration = time.time() - start
            session.close()
        duration = round(duration * 1000)
        embed = discord.Embed(title = "Pong? :ping_pong:", description = "It took me **{} ms** to respond. Damn.".format(duration), color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Lists all roles including self and auto roles
    @commands.command()
    async def roles(self, ctx):
        rolelist = ""
        for rolename in ctx.guild.roles:
            if str(rolename) == "@everyone":
                pass
            else:
                rolelist += "{}\n".format(rolename)
        embed = discord.Embed(title = "", description = "**All Roles**\n" + rolelist, color = 0x195ac4)
        with open('Data/selfroles.json', 'r') as f:
            rolelist = json.load(f)
        if str(ctx.guild.id) in rolelist:
            serverlist = ""
            for i in rolelist[str(ctx.guild.id)]:
                role = discord.utils.find(lambda r: r.id == i, ctx.guild.roles)
                serverlist += str(role.name) + "\n"
            if serverlist == "":
                embed1 = discord.Embed(title = "", description = "**Self Roles**\nNone", color = 0x195ac4)
            else:
                embed1 = discord.Embed(title = "", description = "**Self Roles**\n" + serverlist, color = 0x195ac4)
        else:
            embed1 = discord.Embed(title = "", description = "**Self Roles**\nNone", color = 0x195ac4)
        with open('Data/autoroles.json', 'r') as f:
            rolelist = json.load(f)
        if str(ctx.guild.id) in rolelist:
            serverlist = ""
            for i in rolelist[str(ctx.guild.id)]:
                role = discord.utils.find(lambda r: r.id == i, ctx.guild.roles)
                serverlist += str(role.name) + "\n"
            if serverlist == "":
                embed2 = discord.Embed(title = "", description = "**Auto Roles**\nNone", color = 0x195ac4)
            else:
                embed2 = discord.Embed(title = "", description = "**Auto Roles**\n" + serverlist, color = 0x195ac4)
        else:
            embed2 = discord.Embed(title = "", description = "**Auto Roles**\nNone", color = 0x195ac4)
        embed2.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        await ctx.send(embed = embed1)
        await ctx.send(embed = embed2)

    #A command that searches for a member on the server
    @commands.command()
    async def member(self, ctx, mquery : str):
        member = discord.utils.find(lambda m: m.name.lower().startswith(mquery.lower()), ctx.guild.members)
        if member is not None:
                embed = discord.Embed(title = "*Searching for: :mag_right:*", description = mquery, color = 0x195ac4)
                embed.add_field(name = "**Member found**".format(member.id), value = "<@{}> matches your query".format(member.id), inline = False)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
                embed = discord.Embed(title = "*Searching for: :mag_right:*", description = mquery, color = 0xce141d)
                embed.add_field(name = "**Looks like no one with that name exists on the server!**", value = "Try again?", inline = False)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @commands.command()
    async def donate(self, ctx):
        embed = discord.Embed(title = "Help the creator out!", description = "Hades is the sole developer working on me, and every little ounce of support from you counts immeasurably\n\nYou can donate at my Patreon - https://www.patreon.com/hades99", color = 0x195ac4)
        embed.set_thumbnail(url = 'https://www.shareicon.net/data/2016/10/05/838688_help_512x512.png')
        await ctx.send(embed = embed)


#Adding this cog to the bot
def setup(bot):
    bot.add_cog(Info(bot))
    print('"Info" has been loaded successfully.')
