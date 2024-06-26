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
        guild = message.guild
        channels = guild.text_channels
        target = int(target_str)

        if (None == target):
            await message.channel.send('target not specified. Try again.')
            return

        if (message.author.id not in secret.credentials.privileged_users):
            await message.channel.send("no perms, byebye")
            return
       
        await message.channel.send(f"iterating over channels in {guild.name}...")
       
        output = """"""
        for channel in channels:
            output += (f"<#{channel.id}> : found channel {channel.name}, id {channel.id}\n")

            if len(output) >= 1500:
                await message.channel.send(output)
                output = """"""

        await message.channel.send(output)
        await message.channel.send("=======================================================")

        total_server_messages = 0
        target_total_messages = 0

        for channel in channels:
            channel_messages = 0
            target_messages = 0
            async for historical_message in channel.history(limit=None):
                channel_messages += 1
                if (target == historical_message.author.id):
                    target_messages += 1
                    await historical_message.delete()
                    time.sleep(1.2)

            target_total_messages += target_messages
            total_server_messages += channel_messages

            await message.channel.send(f"<#{channel.id}>: for user <@{target}>, {target_messages}/{channel_messages} have been deleted; current total: {target_total_messages}/{total_server_messages}")

        await message.channel.send(f"total messages: {target_total_messages}/{total_server_messages}")


async def setup(bot):
    await bot.add_cog(Redact(bot))
