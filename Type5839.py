from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.type", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

orig_text = msg.text.split(".t", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.005) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.005)
 
        except FloodWait as e:
            sleep(e.x)

app.run()
