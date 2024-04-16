import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/b4f3ac2bb756cfc907c49.jpg"
file2 = "https://te.legra.ph/file/3b8db7fd7e30603ff8525.jpg"
file3 = "https://te.legra.ph/file/4e3e3f5a5c65a55b3a52a.jpg"
file4 = "https://te.legra.ph/file/0dea7a3a14891ddfdde1c.jpg"
file5 = "https://te.legra.ph/file/523f4c00f8d5ea0b27b14.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Click Here", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"♡ Hey {betsy}, I'm Obanai\n♡ I'm Created By [LEVI](tg://user?id=1737646273)\n♡ Click The Button Below To Get Your Info",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        NEKO = "YOUR DETAILS BY NEKO \n\n"
        NEKO += f"FIRST NAME : {PRO.first_name} \n"
        NEKO += f"LAST NAME : {PRO.last_name}\n"
        NEKO += f"YOU BOT : {PRO.bot} \n"
        NEKO += f"RESTRICTED : {PRO.restricted} \n"
        NEKO += f"USER ID : {boy}\n"
        NEKO += f"USERNAME : {PRO.username}\n"
        await event.answer(NEKO, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "myinfo"
__command_list__ = ["myinfo"]
