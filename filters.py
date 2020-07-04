from telethon import events
from PIL import Image, ImageFilter
import io
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.bl", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    
    im = io.BytesIO()
    await client.download_file(reply, im)
    im = Image.open(im)
    f = ImageFilter.BLUR
    img = im.filter(f)
    out = io.BytesIO()
    out.name = str(f)+".png"
    img.save(out)
    out.seek(0)
    await client.send_file(message.to_id, out, caption=str(f))
