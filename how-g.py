from telethon import events
import asyncio
import os
import sys
import random


@borg.on(events.NewMessage(pattern=r"\.howg", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
    
    rnd = random.randrange(1, 100)
    rndt = str(rnd)
    
    await event.edit("🏳️‍🌈 Ты гей на " + rndt + " %")
