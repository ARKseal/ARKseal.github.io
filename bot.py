import asyncio as _asyncio
import os as _os
import threading as _threading
import time as _time

from discord.ext.commands import Bot as _Bot
from dotenv import load_dotenv as _load_dotenv

async def _spammer(ctx, count: int, response: str):
    for _ in range(count):
        await ctx.send(response)
        await _asyncio.sleep(1)

TASK = None
#test
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
async def _spam(ctx, count: int, *people_and_message):
    global TASK
    if count > 40: count=40
    people = []
    msg = []
    for a in people_and_message:
        if a.startswith('<') and a.endswith('>'):
            people.append(a)
        else:
            msg.append(a)
    if not msg: msg = ["No", "Message", "was", "given"]
    response = ((' '.join(people) + ' - ') if people else '') + ' '.join(msg)

    TASK = _asyncio.create_task(_spammer(ctx, count, response))

    print("Thread Started")
    await TASK
    print("Thread Ended")
    

@_bot.command(name='stop', help='Stop spamming the current spam command')
async def _stop(ctx):
    global TASK

    if (not TASK) or TASK.done():
        print("Task already done")
    else:
        TASK.cancel()
        print("Thread Stopped")

_bot.run(_TOKEN)