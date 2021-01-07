import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import json

class Mod:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprefix(self, ctx, newprefix):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        guild = str(ctx.guild.id)
        with open("Data/prefix.json", "r") as f:
            prefixList = json.load(f)
        if guild not in prefixList:
            prefixList[guild] = ""
            pass
        else:
            pass
        if newprefix == ">>":
            del prefixList[guild]
            with open("Data/prefix.json", "w") as f:
                json.dump(prefixList, f)
            embed = discord.Embed(title = "Prefix Changed ✅", description = "The prefix for this guild has now been set to ``{}``".format(newprefix), color = 0x195ac4)
            embed.set_footer(text = "{}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        else:
            pass
        prefixList[guild] = newprefix
        with open("Data/prefix.json", "w") as f:
            json.dump(prefixList, f)
        embed = discord.Embed(title = "Prefix Changed ✅", description = "The prefix for this guild has now been set to ``{}``".format(newprefix), color = 0x195ac4)
        embed.set_footer(text = "{}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        try:
            logsChannel = loglist[str(ctx.guild.id)]['log']
            logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
            embed2 = discord.Embed(title = "Prefix Change Log", description = "{} set the prefix to ``{}``".format(ctx.author.mention, newprefix), color = 0x195ac4)
            embed2.add_field(name = "Reason", value = reason)
            await logsChannel.send(embed = embed2)
        except:
            pass


    @commands.command(aliases = ['gag'])
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, user : discord.Member, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        embed1 = discord.Embed(title = "Muting...", description = "{} is being muted throughout the server".format(user.mention), color = 0x195ac4)
        msg = await ctx.send(embed = embed1)
        for channel in ctx.guild.channels:
            mute_perms = channel.overwrites_for(user)
            mute_perms.send_messages = False
            await channel.set_permissions(user, overwrite = mute_perms, reason = reason)
        embed = discord.Embed(title = "Muted 🔇", description = "{} has been muted throughout the server".format(user.mention), color = 0x195ac4)
        embed.add_field(name = "Reason", value = reason)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await msg.edit(embed = embed)
        try:
            logsChannel = loglist[str(ctx.guild.id)]['log']
            logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
            embed2 = discord.Embed(title = "Mute Log", description = "{} was muted by {}".format(user.mention, ctx.author.mention), color = 0x195ac4)
            embed2.add_field(name = "Reason", value = reason)
            await logsChannel.send(embed = embed2)
        except:
            pass

    @commands.command(aliases = ['ungag'])
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, user : discord.Member, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        embed1 = discord.Embed(title = "Unmuting...", description = "{} is being unmuted throughout the server".format(user.mention), color = 0x195ac4)
        msg = await ctx.send(embed = embed1)
        for channel in ctx.guild.channels:
            unmute_perms = channel.overwrites_for(user)
            unmute_perms.send_messages = None
            await channel.set_permissions(user, overwrite = unmute_perms, reason = reason)
        embed = discord.Embed(title = "Unmuted 🔊", description = "{} has been unmuted throughout the server".format(user.mention), color = 0x195ac4)
        embed.add_field(name = "Reason", value = reason)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await msg.edit(embed = embed)
        try:
            logsChannel = loglist[str(ctx.guild.id)]['log']
            logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
            embed2 = discord.Embed(title = "Unmute Log", description = "{} was unmuted by {}".format(user.mention, ctx.author.mention), color = 0x195ac4)
            embed2.add_field(name = "Reason", value = reason)
            await logsChannel.send(embed = embed2)
        except:
            pass

    @commands.command(aliaes = ['prune'])
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount : int, user = None):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        logsChannel = discord.utils.get(ctx.guild.channels, name = "pluto-bot-logs")
        if user is None:
            num = await ctx.channel.purge(limit = amount + 1)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed = discord.Embed(title = "Purge Log", description = "{} has purged **{}** messages in **{}**".format(ctx.author.mention, len(num - 1), ctx.channel), color = 0x195ac4)
                await logsChannel.send(embed = embed)
            except:
                pass
        else:
            def is_user(m):
                return m.author.mention == user
            def is_me(m):
                return m.author == ctx.author
            await ctx.channel.purge(limit = 1, check = is_me)
            num = await ctx.channel.purge(limit = amount, check = is_user)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed = discord.Embed(title = "Purge Log", description = "{} has deleted all [**{}**] of {}'s messages in the last **{}** messages in **{}**".format(ctx.author.mention, len(num), user.mention, amount, ctx.channel), color = 0x195ac4)
                await logsChannel.send(embed = embed)
            except:
                pass

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user : discord.Member, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        embed = discord.Embed(title = "Kicked 👢", description = "{} has been kicked from the server".format(user.mention), color = 0x195ac4)
        embed.add_field(name = "Reason", value = reason)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.guild.kick(user, reason = reason)
        await ctx.send(embed = embed)
        try:
            logsChannel = loglist[str(ctx.guild.id)]['log']
            logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
            embed2 = discord.Embed(title = "Kick Log", description = "{} was kicked by {}".format(user.mention, ctx.author.mention), color = 0x195ac4)
            embed2.add_field(name = "Reason", value = reason)
            embed2.set_thumbnail(url = user.avatar_url)
            await logsChannel.send(embed = embed2)
        except:
            pass

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.Member, dmsgs = 0, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        logsChannel = discord.utils.get(ctx.guild.channels, name = "pluto-bot-logs")
        embed = discord.Embed(title = "Banned 🚨", description = "{} has been banned from the server and the user's messages from the last **{}** days have been deleted".format(user.mention, dmsgs), color = 0x195ac4)
        embed.add_field(name = "Reason", value = reason)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        embed1 = discord.Embed(title = "Banned 🚨", description = "You have been banned from **{}** by **{}**".format(ctx.guild.name, ctx.author.mention), color = 0x195ac4)
        embed1.add_field(name = "Reason", value = reason)
        await user.send(embed = embed1)
        await ctx.guild.ban(user, reason = reason, delete_message_days = dmsgs)
        await ctx.send(embed = embed)
        try:
            logsChannel = loglist[str(ctx.guild.id)]['log']
            logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
            embed = discord.Embed(title = "Ban Log", description = "{} has banned {} from the server and deleted the user's last **{}** days of messages.".format(ctx.author.mention, user.mention, dmsgs), color = 0x195ac4)
            embed.set_thumbnail(url = user.avatar_url)
            embed.add_field(name = "Reason", value = reason)
            await logsChannel.send(embed = embed)
        except:
            pass


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        banlist = await ctx.guild.bans()
        for i in banlist:
            banreason = i[0]
            banned = i[1]
            if str(banned).startswith(user):
                embed = discord.Embed(title = "Banned user found", description = "We found **{}** to match your unban request\n\n**Banned for**: {}".format(banned.mention, banreason), color = 0x195ac4)
                embed.add_field(name = "Are you sure you want to unban this user?", value = "Please type in ``confirm`` or ``deny``")
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                def response(m):
                    return ((m.content).lower() == "confirm" or (m.content).lower() == "deny") and m.author == ctx.author
                msg = await self.bot.wait_for("message", check = response, timeout = 20.0)
                if msg.content == "confirm":
                    embed = discord.Embed(title = "Unbanned ✅", description = "**{}** has been unbanned from the server".format(banned.mention), color = 0x195ac4)
                    embed.add_field(name = "Reason", value = reason)
                    embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    await ctx.guild.unban(banned, reason = reason)
                    await ctx.send(embed = embed)
                    try:
                        logsChannel = loglist[str(ctx.guild.id)]['log']
                        logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                        embed = discord.Embed(title = "Unban Log", description = "{} has unbanned **{}** from the server.".format(ctx.author.mention, banned.mention), color = 0x195ac4)
                        embed.add_field(name = "Reason", value = reason)
                        await logsChannel.send(embed = embed)
                    except:
                        pass
                elif msg.content == "deny":
                    await msg.add_reaction("\u2705")
                else:
                    pass
                break
            else:
                pass

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lockdown(self, ctx, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        everyone = ctx.guild.default_role
        for channel in ctx.guild.channels:
            if (channel.overwrites_for(everyone)).send_messages is False:
                embed = discord.Embed(title = "Error ❌", description = "Looks like this server/guild is already in lockdown", color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                pass
        embed = discord.Embed(title = "Lockdown Initiating 🔓", description = "Type in ``server`` or ``guild`` to initiate\na server-wide lockdown, or type ``channel`` to\ninitiate a lockdown for this channel\n\nType ``cancel`` to disable lockdown", color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        mesg = await ctx.send(embed = embed)
        def corgcheck(m):
            return (m.content.lower() == "server" or m.content.lower() == "guild" or m.content.lower() == "channel" or m.content.lower() == "cancel") and m.author == ctx.author
        msg = await self.bot.wait_for("message", check = corgcheck, timeout = 20.0)
        if msg.content == "server" or "guild":
            embed = discord.Embed(title = "Server/Guild Lockdown Initiated 🔒", description = "The ``everyone`` role now has ``Send Messages`` permissions as ``False`` for the server/guild\n\nUse ``unlock`` to lift the active lockdown", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            for channel in ctx.guild.channels:
                lockdownperms = channel.overwrites_for(everyone)
                lockdownperms.send_messages = False
                await channel.set_permissions(everyone, overwrite = lockdownperms, reason = reason)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Lockdown Log", description = "{} locked down the server".format(ctx.author.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass
        elif msg.content == "channel":
            if (channel.overwrites_for(everyone)).send_messages is False:
                embed = discord.Embed(title = "Error ❌", description = "Looks like this channel is already in lockdown", color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                pass
            lockdownperms = ctx.channel.overwrites_for(everyone)
            lockdownperms.send_messages = False
            embed = discord.Embed(title = "Channel Lockdown Initiated 🔒", description = "The ``everyone`` role now has ``Send Messages`` permissions as ``False`` for the channel\n\nUse ``unlock`` to lift the active lockdown", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.channel.set_permissions(everyone, overwrite = lockdownperms, reason = reason)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Lockdown Log", description = "{} locked down the channel {}".format(ctx.author.mention, ctx.channel.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass
        elif msg.content == "cancel":
            embed = discord.Embed(title = "Lockdown Cancelled 🔓", description = "", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
        else:
            pass

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def unlock(self, ctx, *, reason = "Not specified"):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        everyone = ctx.guild.default_role
        for channel in ctx.guild.channels:
            if (channel.overwrites_for(everyone)).send_messages is None or (channel.overwrites_for(everyone)).send_messages is True:
                embed = discord.Embed(title = "Error ❌", description = "Looks like this server/guild is already unlocked", color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                pass
        embed = discord.Embed(title = "Disabling Lockdown 🔓", description = "Type in ``server`` or ``guild`` to disable\na server-wide lockdown, or type ``channel`` to\ndisable a lockdown for this channel\n\nType ``cancel`` to keep the lockdown", color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        mesg = await ctx.send(embed = embed)
        def corgcheck(m):
            return (m.content.lower() == "server" or m.content.lower() == "guild" or m.content.lower() == "channel" or m.content.lower() == "cancel") and m.author == ctx.author
        msg = await self.bot.wait_for("message", check = corgcheck, timeout = 20.0)
        if msg.content == "server" or "guild":
            embed = discord.Embed(title = "Server/Guild Unlocked 🔓", description = "The ``everyone`` role now has ``Send Messages`` permissions as ``None`` for the server/guild", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            for channel in ctx.guild.channels:
                unlockperms = channel.overwrites_for(everyone)
                unlockperms.send_messages = None
                await channel.set_permissions(everyone, overwrite = unlockperms, reason = reason)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Unlock Log", description = "{} unlocked the server".format(ctx.author.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass
        elif msg.content == "channel":
            if (channel.overwrites_for(everyone)).send_messages is None or (channel.overwrites_for(everyone)).send_messages is True:
                embed = discord.Embed(title = "Error ❌", description = "Looks like this channel is already unlocked", color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                pass
            unlockperms = channel.overwrites_for(everyone)
            unlockperms.send_messages = None
            embed = discord.Embed(title = "Channel Unlocked 🔓", description = "The ``everyone`` role now has ``Send Messages`` permissions as ``None`` for the channel", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.channel.set_permissions(everyone, overwrite = unlockperms, reason = reason)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Unlock Log", description = "{} unlocked the channel {}".format(ctx.author.mention, ctx.channel.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass
        elif msg.content == "cancel":
            embed = discord.Embed(title = "Lockdown Continued 🔒", description = "", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await msg.add_reaction("\u2705")
            await mesg.edit(embed = embed)
        else:
            pass

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def logging(self, ctx):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        def logcheck(m):
            return m.author == ctx.author
        if str(ctx.guild.id) in loglist:
            logsChannel = discord.utils.get(self.bot.get_all_channels(), id = int(loglist[str(ctx.guild.id)]["log"]))
            embed = discord.Embed(title = "Logging Already Enabled ❕", description = "Looks like logging is already enabled in {}\n\nIf you wish to disable logging, type ``disable``\n\nIf you wish to change the logging channel, type ``change``\n\nType ``cancel`` to not do anything".format(logsChannel.mention), color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            msg3 = await ctx.send(embed = embed)
            msg = await self.bot.wait_for("message", check = logcheck)
            if msg.content == "disable":
                del loglist[str(ctx.guild.id)]
                embed = discord.Embed(title = "Logging Disabled 📝", description = "", color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await msg.add_reaction("\u2705")
                await msg3.edit(embed = embed)
                return
            elif msg.content == "change":
                del loglist[str(ctx.guild.id)]
                await msg.add_reaction("\u2705")
                pass
            elif msg.content == "cancel":
                embed = discord.Embed(title = "Logging Continued 📝", description = "", color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await msg.add_reaction("\u2705")
                await msg3.edit(embed = embed)
                return
        embed = discord.Embed(title = "Enabling Logging 📝", description = "To enable the logging module, please enter the channel name you want for logging.\n\nExample: ``bot-logs``\n\nType in ``cancel`` to disable logging", color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        msg1 = await ctx.send(embed = embed)
        msg = await self.bot.wait_for("message", check = logcheck)
        if msg.content == "cancel":
            embed = discord.Embed(title = "Logging Cancelled 📝", description = "", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await msg.add_reaction("\u2705")
            await msg1.edit(embed = embed)
        else:
            logsChannel = discord.utils.get(self.bot.get_all_channels(), name = msg.content)
            if logsChannel is None:
                embed = discord.Embed(title = "Error ❌", description = "Looks like the channel ``{}`` does not exist".format(msg.content), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                embed = discord.Embed(title = "Channel found ✅", description = "Logging is being enabled in the channel {}\n\nUse ``logging`` to disable this feature or change the logs channel".format(logsChannel.mention), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                loglist[str(ctx.guild.id)] = dict()
                loglist[str(ctx.guild.id)]["log"] = str(logsChannel.id)
                with open("Data/logging.json", "w") as f:
                    json.dump(loglist, f)
                await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warning(self, ctx):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        def authcheck(m):
            return m.author == ctx.author
        with open("Data/warn.json", "r") as f:
            warnlist = json.load(f)
        if str(ctx.guild.id) in warnlist:
            embed = discord.Embed(title = "Warning System ⚠", description = "Looks like the warning system has already been activated on this guild\n\nType in ``disable`` to disable the warning system or ``cancel`` to keep it", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            confirm = await ctx.send(embed = embed)
            msg = await self.bot.wait_for("message", check = authcheck)
            if msg.content.lower() == "disable":
                del warnlist[str(ctx.guild.id)]
                with open("Data/warn.json", "w") as f:
                    json.dump(warnlist, f)
                embed = discord.Embed(title = "Warning System Disabled ⚠", description = "The warning system has now been removed and all member warns have been deleted\n\nUse ``warning`` to enable the system again", color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await msg.add_reaction("\u2705")
                await confirm.edit(embed = embed)
                try:
                    logsChannel = loglist[str(ctx.guild.id)]['log']
                    logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                    embed2 = discord.Embed(title = "Warning System Log", description = "{} disabled the warning system".format(ctx.author.mention), color = 0x195ac4)
                    await logsChannel.send(embed = embed2)
                except:
                    pass
            else:
                embed = discord.Embed(title = "Warning System Continued ⚠", description = "The warning system is still active\n\nUse ``warning`` to disable the system", color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await msg.add_reaction("\u2705")
                await confirm.edit(embed = embed)
                pass
        else:
            embed = discord.Embed(title = "Initiating Warning System ⚠", description = "Type ``enable`` to enable a warning system on the guild, or ``cancel`` to abort", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            msg1 = await ctx.send(embed = embed)
            msg = await self.bot.wait_for("message", check = authcheck)
            if msg.content.lower() == "enable":
                embed = discord.Embed(title = "Warning System Initiated ⚠", description = "A warning system is now active on your server\n\nUse ``warn <user> <reason>`` to warn a user\n\nUse ``warns <user>`` to check a user's warns\n\nA user may use ``warns`` to only check their own warns\n\nA staff member with the ability to kick members can warn other users\n\nType ``warning`` to disable the system", color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                warnlist[str(ctx.guild.id)] = dict()
                with open("Data/warn.json", "w") as f:
                    json.dump(warnlist, f)
                await msg.add_reaction("\u2705")
                await msg1.edit(embed = embed)
                try:
                    logsChannel = loglist[str(ctx.guild.id)]['log']
                    logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                    embed2 = discord.Embed(title = "Warning System Log", description = "{} enabled the warning system".format(ctx.author.mention), color = 0x195ac4)
                    await logsChannel.send(embed = embed2)
                except:
                    pass
            else:
                await msg.add_reaction("\u2705")
                pass

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, user : discord.Member, *, reason):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        with open("Data/warn.json", "r") as f:
            warnlist = json.load(f)
        if str(ctx.guild.id) not in warnlist:
            embed = discord.Embed(title = "Whoops", description = "Looks like you haven't enabled the warning system on your guild.\n\nUse ``warning`` to enable the system", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif user.guild_permissions >= ctx.author.guild_permissions:
            embed = discord.Embed(title = "Whoops", description = "Looks like the target's permissions are equivalent or greater than yours - you cannot warn them", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        elif str(user.id) not in warnlist[str(ctx.guild.id)]:
            await ctx.message.delete()
            warnlist[str(ctx.guild.id)][str(user.id)] = list()
            (warnlist[str(ctx.guild.id)][str(user.id)]).append(reason)
            with open("Data/warn.json", "w")  as f:
                json.dump(warnlist, f)
            embed = discord.Embed(title = "Warned ✅", description = "{} has been warned\n\nUse ``warns`` to check your own warns\n\nStaff members with the ability to kick members may view a user's warns by typing ``warns <user mention>``".format(user.mention), color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Warning Log", description = "{} has warned {}".format(ctx.author.mention, user.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass
        else:
            await ctx.message.delete()
            (warnlist[str(ctx.guild.id)][str(user.id)]).append(reason)
            with open("Data/warn.json", "w")  as f:
                json.dump(warnlist, f)
            embed = discord.Embed(title = "Warned ✅", description = "{} has been warned\n\nUse ``warns`` to check your own warns\n\nStaff members with the ability to kick members may view a user's warns by typing ``warns <user mention>``".format(user.mention), color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            try:
                logsChannel = loglist[str(ctx.guild.id)]['log']
                logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                embed2 = discord.Embed(title = "Warning Log", description = "{} has warned {}".format(ctx.author.mention, user.mention), color = 0x195ac4)
                embed2.add_field(name = "Reason", value = reason)
                await logsChannel.send(embed = embed2)
            except:
                pass

    @commands.command()
    async def warns(self, ctx, *user : discord.Member):
        with open("Data/warn.json", "r") as f:
            warnlist = json.load(f)
        try:
            user = user[0]
        except Exception as e:
            user = None
        if user is None:
            if str(ctx.guild.id) not in warnlist:
                pass
            elif str(ctx.author.id) not in warnlist[str(ctx.guild.id)]:
                embed = discord.Embed(title = "No warns detected ❎", description = "Looks like you don't have any warns on **{}**".format(ctx.guild.name), color = 0x195ac4)
                await ctx.author.send(embed = embed)
                await ctx.message.add_reaction("\u2705")
            else:
                warnstring = ""
                index = 1
                for warn in warnlist[str(ctx.guild.id)][str(ctx.author.id)]:
                    warnstring += "{}.  ``{}``\n".format(str(index), warn)
                    index += 1
                embed = discord.Embed(title = "Warn list ❗", description = "You have **{}** warn(s) on **{}**:\n\n{}".format(index, ctx.guild.name, warnstring), color = 0x195ac4)
                await ctx.author.send(embed = embed)
        else:
            if ctx.author.guild_permissions.kick_members is True:
                if str(ctx.guild.id) not in warnlist:
                    return
                else:
                    pass
                if str(user.id) in warnlist[str(ctx.guild.id)]:
                    warnstring = ""
                    index = 1
                    for warn in warnlist[str(ctx.guild.id)][str(user.id)]:
                        warnstring += "**{}.**  ``{}``\n".format(str(index), warn)
                        index += 1
                    embed = discord.Embed(title = "Warn list ❗", description = "**{}** has **{}** warn(s) on **{}**:\n\n{}".format(user.mention, index, ctx.guild.name, warnstring), color = 0x195ac4)
                    await ctx.author.send(embed = embed)
                else:
                    embed = discord.Embed(title = "No warns detected ❎", description = "Looks like **{}** doesn't have any warns on **{}**".format(user.mention, ctx.guild.name), color = 0x195ac4)
                    await ctx.author.send(embed = embed)
                    await ctx.message.add_reaction("\u2705")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def deletewarns(self, ctx, username : discord.Member):
        with open("Data/logging.json", "r") as f:
            loglist = json.load(f)
        def authcheck(m):
            return m.author == ctx.author
        with open("Data/warn.json", "r") as f:
            warnlist = json.load(f)
        if str(ctx.guild.id) not in warnlist:
            pass
        elif str(username.id) not in warnlist[str(ctx.guild.id)]:
            embed = discord.Embed(title = "No warns detected ❎", description = "Looks like **{}** doesn't have any warns on **{}**".format(user.mention, ctx.guild.name), color = 0x195ac4)
            await ctx.author.send(embed = embed)
            await ctx.message.add_reaction("\u2705")
        else:
            embed = discord.Embed(title = "Deleting Warn(s) ❓", description = "Type in ``all`` to delete all the user's warns or ``recent``/``last`` to delete the most recent warn", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            confirm = await ctx.send(embed = embed)
            msg = await self.bot.wait_for("message", check = authcheck)
            if msg.content.lower() == "all":
                del warnlist[str(ctx.guild.id)][str(username.id)]
                embed = discord.Embed(title = "All Warnings Purged ✅", description = "All the warns for {} in this guild have been removed".format(username.mention), color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                with open("Data/warn.json", "w") as f:
                    json.dump(warnlist, f)
                await msg.add_reaction("\u2705")
                await confirm.edit(embed = embed)
                try:
                    logsChannel = loglist[str(ctx.guild.id)]['log']
                    logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                    embed2 = discord.Embed(title = "Warning Log", description = "{} has removed all of the warnings for {}".format(ctx.author.mention, username.mention), color = 0x195ac4)
                    await logsChannel.send(embed = embed2)
                except:
                    pass
            elif msg.content.lower() == "recent" or msg.content.lower() == "last":
                del warnlist[str(ctx.guild.id)][str(username.id)][-1]
                embed = discord.Embed(title = "Last Warning Purged ✅", description = "The most recent warning for {} in this guild has been removed".format(username.mention), color = 0x195ac4)
                embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                with open("Data/warn.json", "w") as f:
                    json.dump(warnlist, f)
                await msg.add_reaction("\u2705")
                await confirm.edit(embed = embed)
                try:
                    logsChannel = loglist[str(ctx.guild.id)]['log']
                    logsChannel = discord.utils.get(member.guild.text_channels, id = int(logsChannel))
                    embed2 = discord.Embed(title = "Warning Log", description = "{} has removed the most recent warning for {}".format(ctx.author.mention, username.mention), color = 0x195ac4)
                    await logsChannel.send(embed = embed2)
                except:
                    pass
            else:
                pass


def setup(bot):
    bot.add_cog(Mod(bot))
    print('"Mod" has been loaded successfully.')
