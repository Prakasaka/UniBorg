from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd("pingme"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Ping is High AF 😭")
    end = datetime.now()
    ms = (end - start).microseconds/1000
    await event.edit("Ping is High AF 😭\n{}".format(ms))
