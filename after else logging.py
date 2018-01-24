logsChannel = discord.utils.get(self.bot.get_all_channels(), name = msg.content)
            if logsChannel is None:
                embed = discord.Embed(title = "❌ Error ❌", description = "Looks like the channel ``{}`` does not exist".format(msg.content), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                embed = discord.Embed(title = "✅ Channel found ✅", description = "Logging is being enabled in the channel {}\n\nEnter ``1`` if you would like to log only PlutoBot commands\n\nEnter``2``if you would like to log PlutoBot commands and events such a message edits, deletions, joins, etc. as well".format(logsChannel.mention), color = 0x195ac4)
                embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                msg2 = await self.bot.wait_for("message", check = logcheck)
                if msg2.content == "1":
                    embed = discord.Embed(title = "📝 Logging Enabled 📝", description = "The usage of all commands that affect the server via PlutoBot will now be logged in {}\n\nType in >>logging to disable or change the logging channel".format(logsChannel.mention), color = 0x195ac4)
                    embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    loglist[ctx.guild.id]["log"] = logsChannel.id
                    loglist[ctx.guild.id]["level"] = "1"
                    with open("Data/logging.json", "w") as f:
                        json.dump(loglist, f)
                    ctx.send(embed = embed)
                elif msg2.content == "2":
                    embed = discord.Embed(title = "📝 Logging Enabled 📝", value = "The usage of all commands that affect the server via PlutoBot as well as events such as bans, leaves, joins, kicks, etc. will now be logged in {}\n\nType in >>logging to disable or change the logging channel".format(logsChannel.mention), color = 0x195ac4)
                    embed.set_footer(text = "Action performed by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
                    loglist[ctx.guild.id]["log"] = logsChannel.id
                    loglist[ctx.guild.id]["level"] = "2"
                    with open("Data/logging.json", "w") as f:
                        json.dump(loglist, f)
                    ctx.send(embed = embed)
                else:
                    pass
