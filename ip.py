from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd
from socket import *

@borg.on(admin_cmd(pattern="ip (.*)"))

async def _(event):

    if event.fwd_from:

        return


    input_str = event.pattern_match.group(1)
        
    addr = gethostbyname(input_str)
	await event.edit("IP Address of website is" + " " + addr)
