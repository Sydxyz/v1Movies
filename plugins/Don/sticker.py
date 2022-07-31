#Made
#by
#Don_Sflix

from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`\n\n ➕➕➕🅲︎🆁︎🅴︎🅳︎🅸︎🆃︎🆂︎➖➖➖ \n [𝙼𝙾𝙳 𝙼𝙾𝚅𝙸𝙴𝚉𝚇 📺](https://t.me/Mod_Moviezx) \n [𝙱𝙾𝚃 𝙲𝚁𝙰𝙲𝙺𝙴𝚁🧨🧨](https://t.me/bot_cracker) \n [𝙶𝚁𝙾𝚄𝙿🥨🥨🥨](https://t.me/malayalam_requester_bot)", quote=True)
    else: 
       await message.reply("Oops !!That is Not a sticker file")
