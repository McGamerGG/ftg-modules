from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.pol1", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       

    await event.edit("🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵")
    await asyncio.sleep(0.5)
    await event.edit("🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴")
    await asyncio.sleep(0.5)
    await event.edit("🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵")
    await asyncio.sleep(0.5)
    await event.edit("`**🚨🚨Никому ни с места! Прибыла полиция🚨🚨...Вы арестованы, за свою красоту.`**")
