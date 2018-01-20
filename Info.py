import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
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
            embed = discord.Embed(title = "**Help Categories**", description = "\n:tools: **Moderation** :tools:\n\n\n:notepad_spiral: **Info** :notepad_spiral:\n\n\n:space_invader: **Fun** :space_invader:\n\n\n:musical_note: **Music** :musical_note:\n\n\n:gem: **PlutoBits** :gem:\n\n\n:robot: **CleverBot** :robot:\n\n\n:scroll: **Roles** :scroll:\n\n\n**Type >>help <category> to know more about a module!**\n", color = 0x195ac4)
            embed.set_thumbnail(url = ctx.guild.icon_url)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    #Sub-command for Moderation help
    @help.command(aliases = ['Moderation', 'mod', 'Mod'])
    async def moderation(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Moderation**", color = 0x195ac4)
        embed.add_field(name = "**Purge**", value = '```bash\nUse ">>purge <number>" to delete up to 100 messages.\n Alias: prune```', inline = False)
        embed.add_field(name = "**Mute**", value = '```bash\nUse ">>mute <user>" to mute a user.\n Alias: gag```', inline = False)
        embed.add_field(name = "**Unmute**", value = '```bash\nUse ">>unmute <user>" to unmute a user.\n Alias: ungag```', inline = False)
        embed.add_field(name = "**Kick**", value = '```bash\nUse ">>kick <@name>" to kick a user from the server.```', inline = False)
        embed.add_field(name = "**Ban**", value = '```bash\nUse ">>ban <@name>" to permanently ban a user from the server.```', inline = False)
        embed.set_thumbnail(url = 'https://pbs.twimg.com/profile_images/861759703864401920/HsF77Zw2.jpg')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Info help
    @help.command(aliases = ['Info'])
    async def info(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Info**", color = 0x195ac4)
        embed.add_field(name = "**Ping**", value = '```bash\nUse ">>ping" to test the latencyof the bot.```', inline = False)
        embed.add_field(name = "**Roles**", value = '```bash\nUse ">>roles" to see the roles in the server in hierarchy.```', inline = False)
        embed.add_field(name = "**Server Stats**", value = '```bash\nUse ">>server" for server stats.```', inline = False)
        embed.add_field(name = "**Bot Stats**", value = '```bash\nUse ">>about" for bot stats.\n Aliases: bot```', inline = False)
        embed.add_field(name = "**Member**", value = '```bash\nUse ">>member <first letters of user>" to return a user matching your query.```', inline = False)
        embed.set_thumbnail(url = 'https://cdn.pixabay.com/photo/2016/03/31/19/13/information-1294813_960_720.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Fun help
    @help.command(aliases = ['Fun'])
    async def fun(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Fun**", color = 0x195ac4)
        embed.add_field(name = "**Choose**", value = '```bash\nUse ">>choose <value>, <value>," etc. to choose between multiple things.```', inline = False)
        embed.add_field(name = "**Say**", value = '```bash\nUse ">>say <something>" to say something via the bot.```', inline = False)
        embed.add_field(name = "**Gif Search**", value = '```bash\nUse ">>gif <query>" to display a random gif related to your query.```', inline = False)
        embed.add_field(name = "**Embed**", value = '```bash\nUse ">>embed <something>" to embed your message with a random color.```', inline = False)
        embed.add_field(name = "**Silent Say**", value = '```bash\nUse ">>ssay <something>" to say something anonymously via the bot.```', inline = False)
        embed.add_field(name = "**Urban**", value = '```bash\nUse ">>urban <query>" to look up your query on UrbanDictionary.```', inline = False)
        embed.add_field(name = "**RPS**", value = '```bash\nUse ">>rps <rock/paper/scissors>" to play RPS with the bot.```', inline = False)
        embed.add_field(name = "**Translate**", value = '```bash\nUse ">>translate <whatever you want to translate> <language>" to translate. Not all languages supported.```', inline = False)
        embed.add_field(name = "**Drink**", value = '```bash\nUse ">>drink <mocktail/cocktail>" for a fresh drink idea. [Under Dev]```', inline = False)
        embed.set_thumbnail(url = 'http://d2trtkcohkrm90.cloudfront.net/images/emoji/apple/ios-10/256/alien-monster.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Music help
    @help.command(aliases = ['Music'])
    async def music(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Music**", color = 0x195ac4)
        embed.add_field(name = "**Join**", value = '```bash\nUse ">>join <voice channel>" to make the bot join a specific voice channel!```', inline = False)
        embed.add_field(name = "**Summon**", value = '```bash\nUse ">>summon" to summon the bot into the voice channel you are in!```', inline = False)
        embed.add_field(name = "**Play**", value = '```bash\nUse ">>play <song>" to add a song to the queue!```', inline = False)
        embed.add_field(name = "**Volume**", value = '```bash\nUse ">>volume <amount>" to set the volume of the playing song!```', inline = False)
        embed.add_field(name = "**Resume**", value = '```bash\nUse ">>resume" to resume the current song!```', inline = False)
        embed.add_field(name = "**Stop**", value = '```bash\nUse ">>stop" to make the bot disconnect and clear the queue!```', inline = False)
        embed.add_field(name = "**Skip**", value = '```bash\nUse ">>skip" to start a skip vote for the current song!```', inline = False)
        embed.add_field(name = "**Now Playing**", value = '```bash\nUse ">>playing" to display the current playing status of the bot!```', inline = False)
        embed.set_thumbnail(url = "https://www.drupal.org/files/cta/graphic/noun_538325_media_dk_gray_0.png")
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for CleverBot help
    @help.command(aliases = ['Cleverbot', 'CleverBot'])
    async def cleverbot(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - CleverBot**\n\n\nThe CleverBot module has not been developed by the creator of PlutoBot and uses the CleverBot.io API to function.\n\n\n**Mention the bot and type something to have a casual conversation with the bot.**\n\n\n**CleverBot website:** https://cleverbot.io", color = 0x195ac4)
        embed.set_image(url = "https://www.fastly.com/cimages/6pk8mg3yh2ee/7dXMrGRkKkUQOsGWikEoI/e6660b7ef79961dd8c70fe669ebcb2ca/cleverbot.png?auto=webp&height=300")
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for Roles help
    @help.command(aliases = ['Roles'])
    async def roles(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - Roles**", color = 0x195ac4)
        embed.add_field(name = "**Roles List**", value = '```bash\nUse ">>roles" to view a list of server roles, self roles, and auto roles.```', inline = False)
        embed.add_field(name = "**Use Self Roles**", value = '```bash\nUse ">>sroles enable/disable" to enable/disable the module for your server.```', inline = False)
        embed.add_field(name = "**Add Self Role**", value = '```bash\nUse ">>sroleadd <role>" to allow users to give themselves that role.```', inline = False)
        embed.add_field(name = "**Remove Self Role**", value = '```bash\nUse ">>sroleremove <role>" to remove allowing users to give themselves that role.```', inline = False)
        embed.add_field(name = "**Add Role**", value = '```bash\nUse ">>addme <role>" to add yourself to a role in the self given roles list.```', inline = False)
        embed.add_field(name = "**Remove Role**", value = '```bash\nUse ">>removeme <role>" to remove a role that you gave yourself.```', inline = False)
        embed.add_field(name = "**Self Roles List**", value = '```bash\nUse ">>srolelist" to view a list of the roles that you can give yourself.```', inline = False)
        embed.add_field(name = "**Use Auto Roles**", value = '```bash\nUse ">>aroles enable/disable" to enable/disable auto roles.```', inline = False)
        embed.add_field(name = "**Add Auto Role**", value = '```bash\nUse ">>addarole <role>" to give a role to users automatically when they join```', inline = False)
        embed.add_field(name = "**Remove Auto Role**", value = '```bash\nUse ">>removearole <role>" to remove a role from the auto role list.```', inline = False)
        embed.add_field(name = "**Auto Roles List**", value = '```bash\nUse ">>arolelist" to view a list of the roles that are automatically added to new members.```', inline = False)
        embed.set_thumbnail(url = 'http://www.subseatarget.com/wp-content/themes/subseatarget/images/st-roles-big.png')
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Sub-command for PlutoBits help
    @help.command(aliases = ['Plutobits', 'PlutoBits', 'pbits'])
    async def plutobits(self, ctx):
        embed = discord.Embed(title = "", description = "**Help - PlutoBits**", color = 0x195ac4)
        embed.add_field(name = "**PlutoBits**", value = '```bash\nUse ">>pbits enable/disable" to enable/disable the currency for PlutoBot.```', inline = False)
        embed.add_field(name = "**Register Account**", value = '```bash\nUse ">>register" to create a PlutoBits account.```', inline = False)
        embed.add_field(name = "**Delete Account**", value = '```bash\nUse ">>deleteaccount" to delete your existing PlutoBits account.```', inline = False)
        embed.add_field(name = "**Transfer PlutoBits**", value = '```bash\nUse ">>transfer <amount> <@user>" to tranfer a certain amount of PlutoBits from your account to the specified account.```', inline = False)
        embed.add_field(name = "**Account Balance**", value = '```bash\nUse ">>account" to check your current PlutoBits.```', inline = False)
        embed.add_field(name = "**Daily Reward**", value = '```bash\nUse ">>daily" to get your daily PlutoBits reward.```', inline = False)
        embed.add_field(name = "**Slots**", value = '```bash\nUse ">>slots" to spin the slot machine!```', inline = False)
        embed.set_thumbnail(url = "https://i.imgur.com/qhcAgPu.png")
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    #Returns info about the bot
    @commands.command(aliases = ['bot'])
    async def about(self, ctx):
        embed = discord.Embed(title = "PlutoBot Stats", description = "Created by **Hades#6871**\n\n**jacob#0513** and **Greem.exe#5501** helped in development\n\nCurrently running **Version** ``3.0.1``\n\nConnected to **{}** servers\n\nUsed by **{}** people\n\nHere's an invite to our Discord - **https://discord.gg/qTNEgPD** - anyone can join!\n\nUse **https://bot.discord.io/plutobot** to invite **PlutoBot** to your own server!\n\nLibrary: discord.py {}".format(str(len(self.bot.guilds)),str(len(set(self.bot.users))), discord.__version__), color = 0x195ac4)
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
        with open('Data/Selfroles.json', 'r') as f:
            rolelist = json.load(f)
            f.close()
        if ctx.guild.id in rolelist:
            serverlist = ""
            for i in rolelist[ctx.guild.id]:
                serverlist += i + "\n"
            if serverlist == "":
                embed1 = discord.Embed(title = "", description = "**Self Roles**\nNone", color = 0x195ac4)
            else:
                embed1 = discord.Embed(title = "", description = "**Self Roles**\n" + serverlist, color = 0x195ac4)
        else:
            embed1 = discord.Embed(title = "", description = "**Self Roles**\nNone", color = 0x195ac4)
        with open('Data/Autoroles.json', 'r') as f:
            rolelist = json.load(f)
            f.close()
        if ctx.guild.id in rolelist:
            serverlist = ""
            for i in rolelist[ctx.guild.id]:
                serverlist += i + "\n"
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
        member = discord.utils.find(lambda m: m.name.startswith(mquery), ctx.guild.members)
        if member is not None:
                embed = discord.Embed(title = "*Searching for: :mag_right:*", description = mquery, color = 0x195ac4)
                embed.add_field(name = "**Member found**".format(member.id), value = "<@{}> matches your query".format(member.id), inline = False)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                embed1 = discord.Embed(title = "Search Log", description = "{} searched for {}".format(ctx.author, mquery), color = 0x17d139)
                embed1.add_field(name = "Result:", value = "{}".format(member))
                logs_channel = discord.utils.get(self.bot.get_all_channels(), name="pluto-bot-logs")
                await ctx.send(embed = embed)
                if logs_channel is None:
                    pass
                else:
                    await logs_channel.send(embed = embed1)
        else:
                embed = discord.Embed(title = "*Searching for: :mag_right:*", description = mquery, color = 0xce141d)
                embed.add_field(name = "**Looks like no one with that name exists on the server!**", value = "Try again?", inline = False)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                embed1 = discord.Embed(title = "Search Log", description = "{} searched for {}".format(ctx.author, mquery), color = 0x17d139)
                embed1.add_field(name = "Result:", value = "No member found".format(member))
                logs_channel = discord.utils.get(self.bot.get_all_channels(), name="pluto-bot-logs")
                await ctx.send(embed = embed)
                if logs_channel is None:
                    pass
                else:
                    await self.bot.send_message(logs_channel, embed = embed1)

#Adding this cog to the bot
def setup(bot):
    bot.add_cog(Info(bot))
    print('"Info" has been loaded successfully.')
