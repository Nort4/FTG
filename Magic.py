from telethon import events
import telethon
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.mgc", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
    send_info = client.get_me()
    await event.edit(send_info)
