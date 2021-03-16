import asyncio as _asyncio
import os as _os
import threading as _threading
import time as _time

from discord.ext.commands import Bot as _Bot
from dotenv import load_dotenv as _load_dotenv

class TEMP:
    def done(self):
        return True

async def spammer(ctx, count: int, response: str):
    for _ in range(count):
        await ctx.send(response)
        await _asyncio.sleep(0.01)

TASK = TEMP()

_load_dotenv()
_TOKEN = _os.getenv('DISCORD_TOKEN')

_bot = _Bot(command_prefix='?')


"""
@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)"""

@_bot.event
async def on_ready():
    print("Online!")

"""@_bot.event
async def on_message(message):
    if message.author == _bot.user:
        return
    if message.author"""

@_bot.command(name='spam', help='Spam something!')
async def _spam(ctx, person: str, count: int = 5, *msg):
    global TASK
    #if count > 20: count=20
    response = (person + ' ' + ' '.join(msg)) if msg else person

    TASK = _asyncio.create_task(spammer(ctx, count, response))

    print("Thread Started")
    await TASK
    print("Thread Ended")
    

@_bot.command(name='stop', help='Stop spamming the current spam command')
async def _stop(ctx):
    global TASK

    if not TASK.done():
        TASK.cancel()
        print("Thread Stopped")
    else:
        print("Task already done")

_bot.run(_TOKEN)