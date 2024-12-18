#!/usr/bin/env python3
"""
    Copyright (c) 2024 suwa, chocorho
"""

import datetime
import discord
from discord.ext import commands

import secret


"""
    A discord bot to be used by Moderators to manage messages in large numbers.
"""


class CleanSlateBot:
    def __init__(self):
        @bot.event
        async def on_ready():
            print(f'We have logged in as {bot.user}')
    
            await self.load_cogs()

        @bot.event
        async def on_disconnect():
            print("Bot has disconnected.")

    async def load_cogs(self):
       await bot.load_extension("cogs.user_commands.reply")
       await bot.load_extension("cogs.privilleged_commands.redact")

    def run(self):
        bot.run(secret.credentials.bottoken)
        

if __name__ == '__main__':
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)
    CleanSlateBot().run()

