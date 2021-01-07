import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import json

class Tags:

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def tags(self, ctx):
        if ctx.invoked_subcommand is None:
            with open("Data/tags.json", "r") as f:
                taglist = json.load(f)
            if (str(ctx.guild.id) not in taglist) or (str(ctx.author.id) not in taglist[str(ctx.guild.id)]):
                embed = discord.Embed(title = "No Tags Found", description = "Looks like there are no tags created by you\nUse ``tags create`` to create a new tag", color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                tagstring = ""
                index = 1
                for tagname in taglist[str(ctx.guild.id)][str(ctx.author.id)]:
                    tagstring += "{}.  ``{}``\n".format(index, tagname)
                    index += 1
                embed = discord.Embed(title = "Your Tags", description = "{}".format(tagstring), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            pass


    @tags.command(aliases = ["make", "new"])
    async def create(self, ctx):
        def authcheck(m):
            return m.author == ctx.author
        with open("Data/tags.json", "r") as f:
            taglist = json.load(f)
        if str(ctx.guild.id) not in taglist:
            taglist[str(ctx.guild.id)] = dict()
            pass
        else:
            pass
        embed = discord.Embed(title = "Creating a New Tag", description = "What would you like the name of the tag to be?", color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        tagname = await self.bot.wait_for("message", check = authcheck)
        for username in taglist[str(ctx.guild.id)]:
            for tag in username:
                if tagname.content == tag:
                    embed = discord.Embed(title = "Tag Already Exists ❌", description = "Looks like <@{}> already has a tag called **{}**".format(username, tagname.content), color = 0x195ac4)
                    embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                    return
                else:
                    pass
        embed = discord.Embed(title = "Creating a New Tag", description = "What would you like the content of the tag to be?\n\n*URLs will work but file uploads will not*", color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        tagcontent = await self.bot.wait_for("message", check = authcheck)
        if str(ctx.author.id) not in taglist[str(ctx.guild.id)]:
            taglist[str(ctx.guild.id)][str(ctx.author.id)] = dict()
            pass
        else:
            pass
        taglist[str(ctx.guild.id)][str(ctx.author.id)][tagname.content] = tagcontent.content
        with open("Data/tags.json", "w") as f:
            json.dump(taglist, f)
        embed = discord.Embed(title = "Tag Created 📑", description = "Your tag **{0}** has been created\nUse ``tag {0}`` to view it".format(tagname.content), color = 0x195ac4)
        embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @tags.command(name = "all")
    async def _all(self, ctx):
        with open("Data/tags.json", "r") as f:
            taglist = json.load(f)
        tagstring = ""
        index = 1
        for alltagauthors, alltagnames in (taglist[str(ctx.guild.id)]).items():
            for tagname in alltagnames:
                tagstring += "{}.  ``{}``".format(index, tagname)
                index += 1
        embed = discord.Embed(title = "All Tags", description = "{}".format(tagstring), color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @tags.command()
    async def delete(self, ctx):
        def authcheck(m):
            return m.author == ctx.author
        with open("Data/tags.json", "r") as f:
            taglist = json.load(f)
        if ctx.author.guild_permissions.manage_messages is True:
            embed = discord.Embed(title = "Deleting Tag", description = "```asciidoc\n= Staff member detected =\n[You can delete other users' tags as well]\n```\nType in the tag name you'd like to delete\nType in ``all`` to delete all your tags\nType ``cancel`` to abort", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = "Deleting Tag", description = "Type in your tag name to delete it\nType in ``all`` to delete all your tags\nType ``cancel`` to abort", color = 0x195ac4)
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        confirm = await self.bot.wait_for("message", check = authcheck)
        if confirm.content.lower() == "all":
            embed = discord.Embed(title = "Tags Deleted ♻", description = "All of your tags have been deleted", color = 0x195ac4)
            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            del taglist[str(ctx.guild.id)][str(ctx.author.id)]
            with open("Data/tags.json", "w") as f:
                json.dump(taglist, f)
            await ctx.send(embed = embed)
        else:
            if ctx.author.guild_permissions.manage_messages is True:
                for user in taglist[str(ctx.guild.id)]:
                    for label in taglist[str(ctx.guild.id)][user]:
                        if confirm.content == label:
                            embed = discord.Embed(title = "Tag Deleted ♻", description = "The tag **{}** by <@{}> has been deleted".format(confirm.content, user), color = 0x195ac4)
                            embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                            del taglist[str(ctx.guild.id)][user][label]
                            with open("Data/tags.json", "w") as f:
                                json.dump(taglist, f)
                            await ctx.send(embed = embed)
                            return
                        else:
                            pass
                embed = discord.Embed(title = "Tag Not Found ❌", description = "You do not have any tag named as **{}**".format(confirm.content), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                if confirm.content in taglist[str(ctx.guild.id)][str(ctx.author.id)]:
                    embed = discord.Embed(title = "Tag Deleted ♻", description = "Your tag **{}** has been deleted".format(taglist[str(ctx.guild.id)][str(ctx.author.id)][confirm.content]), color = 0x195ac4)
                    embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    del taglist[str(ctx.guild.id)][str(ctx.author.id)][confirm.content]
                    with open("Data/tags.json", "w") as f:
                        json.dump(taglist, f)
                    await ctx.send(embed = embed)
                else:
                    embed = discord.Embed(title = "Tag Not Found ❌", description = "You do not have any tag named as **{}**".format(confirm.content), color = 0x195ac4)
                    embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)

    @commands.command()
    async def tag(self, ctx, *, name):
        with open("Data/tags.json", "r") as f:
            taglist = json.load(f)
        for author in taglist[str(ctx.guild.id)]:
            for tag, content in taglist[str(ctx.guild.id)][author].items():
                if tag == name:
                    await ctx.send(content)
                    return
                else:
                    pass
            break
        embed = discord.Embed(title = "Tag Not Found ❌", description = "You do not have any tag named as **{}**".format(name), color = 0x195ac4)
        embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Tags(bot))
    print('"Tags" has been loaded successfully.')
