from telethon import events
import telethon
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.mgc", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
    await event.edit(.eval client.get_me())
