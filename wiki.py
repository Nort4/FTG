from telethon import events
import os
from uniborg.util import admin_cmd
import wikipedia

wikipedia.set_lang("ru")


@borg.on(admin_cmd(pattern="wiki (.*)"))
async def _(event):
    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    
    wiki_search = wikipedia.summary(input_str)
    await message.edit(wiki_search)
