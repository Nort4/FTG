from telethon import events
import os
import json
from urllib import request
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="weat (.*)"))
async def _(event):
	
    if event.fwd_from:
        return


    location = event.pattern_match.group(1)

    wind = 'M'
    metric = 'm'
    option = '0T'

    url = (f'http://wttr.in/{location}?F{wind}{metric}{option}')



    rqst = request.urlopen(url)
    if rqst.getcode() in [200]:
        charset = rqst.info().get_content_charset()
    	content = rqst.read().decode(charset)
    	await event.edit(content.split('Weather ')[2])
