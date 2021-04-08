import asyncio as _asyncio
import os as _os
import threading as _threading
import time as _time

from discord.ext.commands import Bot as _Bot
from dotenv import load_dotenv as _load_dotenv

from Task_List import *

async def _spammer(ctx, count: int, response: str):
    for _ in range(count):
        await ctx.send(response)
        await _asyncio.sleep(1)

TASK = Tasklist()
_code_website = "https://github.com/ARKseal/ARKseal.github.io"

_load_dotenv()
_TOKEN = _os.getenv('DISCORD_TOKEN')

_bot = _Bot(command_prefix='?')

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
    if not msg: msg = ["I", "think", "you", "need", "to", "get", "on"]
    response = ((' '.join(people) + ' - ') if people else '') + ' '.join(msg)

    TASK.add(ctx.guild, _asyncio.create_task(_spammer(ctx, count, response)))

    print("Thread Started")
    await TASK
    print("Thread Ended")


@_bot.command(name='stop', help='Stop spamming the current spam command')
async def _stop(ctx):
    global TASK
    TASK.stop(ctx.guild)

@_bot.command(name='code', help='Get the link to my code')
async def _code(ctx):
    await ctx.send('See my code at {} under Get_On_Bot!'.format(_code_website))

_bot.run(_TOKEN)