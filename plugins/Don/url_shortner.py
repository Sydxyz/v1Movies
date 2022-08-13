import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler
from pyshorteners import Shortener

BITLY_API = os.environ.get("BITLY_API", "2e461627f4a2b17c1ac0f58c0ef2fe165c903cd2")
CUTTLY_API = os.environ.get("CUTTLY_API", "6485ffdd417b749dd0e543034")
SHORTCM_API = os.environ.get("SHORTCM_API", "773742c6fa2ba266fb5fc8ec04e2294352efe662")
GPLINKS_API = os.environ.get("GPLINKS_API", "36d6dd04a79634bb5a4ae150903c78b9c9121ce6")

reply_markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("𝘊𝘭𝘰𝘴𝘦", callback_data='close_data')
        ]]
    )

@Client.on_message(filters.command(["short"]) & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="`I Like Your Smartness 🥳 But Don't Be Over Smart 🤨`",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        disable_web_page_preview=True
    )

@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0),
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Short Links",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
            reply_to_message_id=message.message_id
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )

async def short(link):
    shorten_urls = "**--I'VE TOLD YOU--**"
    
    # Send the text
    try:
        shorten_urls += ""
        return shorten_urls
    except Exception as error:
        return error
