from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import json
#--
#Importing the bot developers list from config
with open('Data/config.json') as file:
    config = json.load(file)

botDevelopers = config["botDevelopers"]

def __init__(self, bot):
		self.bot = bot

class eval:
	def __init__(self, bot):
		self.bot = bot
		self._last_result = None
		self.sessions = set()

	#Creating a function to extract the code in the required format
	def cleanup_code(self, content):
		if content.startswith('```') and content.endswith('```'):
			return '\n'.join(content.split('\n')[1:-1])

		return content.strip('` \n')

	#Creating a function that returns the syntax errors if any are presented
	def get_syntax_error(self, e):
		if e.text is None:
			return '```py\n{}: {}\n```'.format(e.__class__.__name___, e)
		return '```py\n{}{"^":>{}}\n{}: {}```'.format(e.text, e.offset, e.__class__.__name__, e)

	#Debugging the code
	@commands.command(pass_context=True, hidden=True, aliases =['eval'])
	async def debug(self, ctx, *, body: str):
		if ctx.author.id in botDevelopers:
			env = {
				'bot': self.bot,
				'ctx': ctx,
				'channel': ctx.channel,
				'author': ctx.author,
				'guild': ctx.guild,
				'message': ctx.message,
				'_': self._last_result
			}

			env.update(globals())

			body = self.cleanup_code(body)
			stdout = io.StringIO()

			to_compile = 'async def func():\n{}'.format(textwrap.indent(body, "	"))

			try:
				exec(to_compile, env)
			except Exception as e:
				return await ctx.send('```py\n{}: {}\n```'.format(e.__class__.__name__, e))

			func = env['func']
			try:
				with redirect_stdout(stdout):
					ret = await func()
			except Exception as e:
				value = stdout.getvalue()
				await ctx.send('```py\n{}{}\n```'.format(value, traceback.format_exc()))
			else:
				value = stdout.getvalue()
				try:
					await ctx.message.add_reaction('\u2705')
				except:
					pass

				if ret is None:
					if value:
						await ctx.send('```py\n{}\n```'.format(value))
				else:
					self._last_result = ret
					await ctx.send('```py\n{}{}\n```'.format(value, ret))

#Adding this cog to the bot
def setup(bot):
	bot.add_cog(eval(bot))
	print('"Eval" has been loaded successfully.')
