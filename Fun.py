import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import urbandict

class Fun:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx, *, text):
        author = ctx.author
        colorList = [0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xf1c40f, 0xe67e22, 0xe74c3c, 0x992d22, 0x7289da, 0x99aab5]
        def authcheck(m):
            return m.author == author
        embed = discord.Embed(title = "", description = text, color = random.choice(colorList))
        embed.set_footer(icon_url = author.avatar_url, text = author.name)
        await ctx.channel.purge(limit = 1, check = authcheck)
        await ctx.send(embed = embed)

    @commands.command()
    async def choose(self, ctx, *choices):
        choice = random.choice(choices)
        await ctx.send("I think you should go with ``{}`` {}".format(choice.strip(','), ctx.author.mention))

    @commands.command()
    async def whisper(self, ctx, *, text):
        def authcheck(m):
            return m.author == ctx.author
        await ctx.channel.purge(limit = 1, check = authcheck)
        await ctx.send(text)

    @commands.command()
    async def urban(self, ctx, *, query):
        avatar = ctx.author.avatar_url
        try:
            result = urbandict.define(query)
        except Exception as e:
            embed = discord.Embed(title = "Urban Dictionary 📖", description = "You searched for ``{}`` but I couldn't find anything 😕".format(query), color = 0x195ac4)
            embed.set_footer(icon_url = avatar, text = "Requested by {}".format(ctx.author.name))
            await ctx.send(embed = embed)
            return
        definiton = result[0]["def"]
        example = result[0]["example"]
        embed = discord.Embed(title = "Urban Dictionary 📖", description = "You searched for ``{}`` and here's what we got:\n\n**Definition**\n{}\n\n**Example**\n{}".format(query, definiton, example), color = 0x195ac4)
        embed.set_footer(icon_url = avatar, text = "Requested by {}".format(ctx.author.name))
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))
    print('"Fun" has been loaded successfully.')
