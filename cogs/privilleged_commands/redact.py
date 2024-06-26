import secret

import datetime
import time

import asyncio
import discord
from discord.ext import commands


class Redact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["purge"])
    async def redact(self, message, target_str):
        
        target = int(target_str)

        if (None == target):
            await message.channel.send('target not specified. Try again.')
            return

        if (message.author.id not in secret.credentials.privileged_users):
            await message.channel.send("no perms, byebye")
            return
        
        await message.channel.send(f"Deleting messages for {target}...")
        
        #end_date = datetime.datetime(2021, 5, 1)
        async for historical_message in message.channel.history(limit=None):
            print(f"{historical_message.content}")
            if (target == historical_message.author.id):
                print(f"now deleting the next message, from {historical_message.created_at}")
                await historical_message.delete(delay=1.2)
                asyncio.sleep(5)

async def setup(bot):
    await bot.add_cog(Redact(bot))
