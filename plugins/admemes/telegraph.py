import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from info import TMP_DOWNLOAD_DIRECTORY
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from plugins.helper_functions.get_file_id import get_file_id


@Client.on_message(
    filters.command("telegraph") &
    f_onw_fliter
)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.🥶")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!🤯")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.message_id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply(
            f"Link :- <code>https://telegra.ph{response[0]}</code>    <b> 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› 
<a href=https://t.me/Mod_Moviezx><b>𝙼𝙾𝙳 𝙼𝙾𝚅𝙸𝙴𝚉 𝚇🎐🎐</a>
<a href=https://t.me/Syd_Xyz>𝙾𝚆𝙽𝙴𝚁😇😇</a>
<a href=https://t.me/malayalam_requester_bot>𝙶𝚁𝙾𝚄𝙿❤️‍🔥</a>
<a href=https://t.me/gettglinks/9>𝙱𝙾𝚃𝚂🎮</a>
<a href=https://t.me/parallel_Cinemas>𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴😉😁</a>
<a href=https://t.me/bot_cracker>𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻😇💫</a> </b> ",
            disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )
