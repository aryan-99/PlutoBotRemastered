import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import giphypop

g = giphypop.Giphy()

class Giphy:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, *, query):
        img = g.random_gif(tag = query)
        embed = discord.Embed(title = "Giphy", description = "You searched for ``{}`` and here is what I found:".format(query), color = 0x195ac4)
        embed.set_image(url = img.media_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = "Requested by {}".format(ctx.author.name))
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Giphy(bot))
    print('"Giphy" has been loaded successfully.')
