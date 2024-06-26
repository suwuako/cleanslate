import discord
from discord.ext import commands


class Reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["hello"])
    async def ping(self, message):
      await message.channel.send('Pong!')


async def setup(bot):
    await bot.add_cog(Reply(bot))