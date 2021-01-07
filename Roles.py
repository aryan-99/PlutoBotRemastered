import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import json

col = 0x195ac4

class Roles:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def sroles(self, ctx):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        def authcheck(m):
            return m.author == author
        with open("Data/selfroles.json", "r") as f:
            guildList = json.load(f)
        if guild in guildList:
            srolelist = guildList[guild]
            embed = discord.Embed(title = "Disabling Self Roles 👥", description = "Are you sure you want to disable self roles?\nYour self role list will be deleted from the database\nType ``yes`` to disable or ``cancel`` to abort", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            confirmMsg = await self.bot.wait_for("message", check = authcheck)
            confirm = (confirmMsg.content).lower()
            if confirm == "yes" or confirm == "disable":
                del guildList[guild]
                embed = discord.Embed(title = "Self roles disabled ✅", description = "The self roles feature has been disabled on this server\nPlease use ``sroles`` to toggle it again", color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                with open("Data/selfroles.json", "w") as f:
                    json.dump(guildList, f)
                await ctx.send(embed = embed)
            else:
                await confirmMsg.add_reaction("✅")
        elif guild not in guildList:
            embed = discord.Embed(title = "Enabling Self Roles 👥", description = "Are you sure you want to enable self roles?\nThis feature allows users to give themselves roles you specify\nType ``yes`` to enable or ``cancel`` to abort", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            confirmMsg = await self.bot.wait_for("message", check = authcheck)
            confirm = (confirmMsg.content).lower()
            if confirm == "yes" or confirm == "enable":
                guildList[guild] = list()
                embed = discord.Embed(title = "Self roles enabled ✅", description = "The self roles feature has been enabled on this server\nYou can use ``addsrole <role>`` to add a role to a list of roles users can assign themselves\nPlease use ``sroles`` to disable this feature", color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                with open("Data/selfroles.json", "w") as f:
                    json.dump(guildList, f)
                await ctx.send(embed = embed)
            else:
                await confirmMsg.add_reaction("✅")
        else:
            embed = discord.Embed(title = "Error ❌", description = "Looks like there's a database error - contact the creator for further help <@345318328195350528>", color = col)
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addsrole(self, ctx, *, query):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/selfroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled self roles on this server\nUse ``sroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == query.lower(), ctx.guild.roles)
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(query), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            guildList[guild].append(role.id)
            with open("Data/selfroles.json", "w") as f:
                json.dump(guildList, f)
            embed = discord.Embed(title = "Self role added ✅", description = "``{}`` has been added as a self assignable role\nMembers can use ``addme <role>`` to assign themselves this role\nUse ``removesrole`` to remove it from this list".format(role.name), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def removesrole(self, ctx, *, query):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/selfroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled self roles on this server\nUse ``sroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == query.lower(), ctx.guild.roles)
        srolelist = guildList[guild]
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(query), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            roleID = role.id
            if roleID in srolelist:
                srolelist.remove(roleID)
                with open("Data/selfroles.json", "w") as f:
                    json.dump(guildList, f)
                embed = discord.Embed(title = "Self role removed ✅", description = "``{}`` has been removed from the self assignable roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` exists, but isn't on the self assignable roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)

    @commands.command()
    async def addme(self, ctx, *, role):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/selfroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled self roles on this server\nUse ``sroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == role.lower(), ctx.guild.roles)
        srolelist = guildList[guild]
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(role), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            existRole = discord.utils.find(lambda r: r.id == role.id, author.roles)
            roleID = role.id
            if existRole is None:
                pass
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like you already have the role ``{}``".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
                return
            if roleID in srolelist:
                await author.add_roles(role, reason = "Self role")
                embed = discord.Embed(title = "Role assigned ✅", description = "You have assigned yourself the role ``{}``\nUse ``removeme <role>`` to remove a self assignable role\nUse ``roles`` to view a list of self assignable roles".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` exists, but isn't on the self assignable roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)

    @commands.command()
    async def removeme(self, ctx, *, role):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/selfroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled self roles on this server\nUse ``sroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == role.lower(), ctx.guild.roles)
        srolelist = guildList[guild]
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(role), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            existRole = discord.utils.find(lambda r: r.id == role.id, author.roles)
            roleID = role.id
            if existRole is not None:
                pass
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like you don't have the role ``{}``".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
                return
            if roleID in srolelist:
                await author.remove_roles(role, reason = "Self role")
                embed = discord.Embed(title = "Role assigned ✅", description = "You have assigned yourself the role ``{}``\nUse ``removeme <role>`` to remove a self assignable role\nUse ``roles`` to view a list of self assignable roles".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` exists, but isn't on the self assignable roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def aroles(self, ctx):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        def authcheck(m):
            return m.author == author
        with open("Data/autoroles.json", "r") as f:
            guildList = json.load(f)
        if guild in guildList:
            arolelist = guildList[guild]
            embed = discord.Embed(title = "Disabling Auto Roles 👥", description = "Are you sure you want to disable auto roles?\nYour auto roles list will be deleted from the database\nType ``yes`` to disable or ``cancel`` to abort", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            confirmMsg = await self.bot.wait_for("message", check = authcheck)
            confirm = (confirmMsg.content).lower()
            if confirm == "yes" or confirm == "disable":
                del guildList[guild]
                embed = discord.Embed(title = "Auto roles disabled ✅", description = "The auto roles feature has been disabled on this server\nPlease use ``aroles`` to toggle it again", color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                with open("Data/autoroles.json", "w") as f:
                    json.dump(guildList, f)
                await ctx.send(embed = embed)
            else:
                await confirmMsg.add_reaction("✅")
        elif guild not in guildList:
            embed = discord.Embed(title = "Enabling Auto Roles 👥", description = "Are you sure you want to enable auto roles?\nThis feature will cause the bot to give members the roles you specify when they join your server\nType ``yes`` to enable or ``cancel`` to abort", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            confirmMsg = await self.bot.wait_for("message", check = authcheck)
            confirm = (confirmMsg.content).lower()
            if confirm == "yes" or confirm == "enable":
                guildList[guild] = list()
                embed = discord.Embed(title = "Auto roles enabled ✅", description = "The auto roles feature has been enabled on this server\nYou can use ``addarole <role>`` to add a role to a list of roles users will be assigned when they join\nPlease use ``aroles`` to disable this feature", color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                with open("Data/autoroles.json", "w") as f:
                    json.dump(guildList, f)
                await ctx.send(embed = embed)
            else:
                await confirmMsg.add_reaction("✅")
        else:
            embed = discord.Embed(title = "Error ❌", description = "Looks like there's a database error - contact the creator for further help <@345318328195350528>", color = col)
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addarole(self, ctx, *, query):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/autoroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled auto roles on this server\nUse ``aroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == query.lower(), ctx.guild.roles)
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(query), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            guildList[guild].append(role.id)
            with open("Data/autoroles.json", "w") as f:
                json.dump(guildList, f)
            embed = discord.Embed(title = "Auto role added ✅", description = "``{}`` has been added as an auto role\nMembers will now be given this role as soon as they join this server\nUse ``removearole`` to remove it from this list".format(role.name), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def removearole(self, ctx, *, query):
        guild = str(ctx.guild.id)
        author = ctx.author
        avatar = author.avatar_url
        footer = author.name
        with open("Data/autoroles.json", "r") as f:
            guildList = json.load(f)
        if guild not in guildList:
            embed = discord.Embed(title = "Error ❌", description = "Looks like you haven't enabled auto roles on this server\nUse ``aroles`` to enable this feature", color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
            return
        role = discord.utils.find(lambda r: r.name.lower() == query.lower(), ctx.guild.roles)
        arolelist = guildList[guild]
        if role is None:
            embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` isn't a role on this server".format(query), color = col)
            embed.set_footer(icon_url = avatar, text = footer)
            await ctx.send(embed = embed)
        else:
            roleID = role.id
            if roleID in arolelist:
                arolelist.remove(roleID)
                with open("Data/autoroles.json", "w") as f:
                    json.dump(guildList, f)
                embed = discord.Embed(title = "Auto role removed ✅", description = "``{}`` has been removed from the auto roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = "Error ❌", description = "Looks like ``{}`` exists, but isn't on the auto roles list".format(role.name), color = col)
                embed.set_footer(icon_url = avatar, text = footer)
                await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(Roles(bot))
    print('"Roles" has been loaded successfully.')
