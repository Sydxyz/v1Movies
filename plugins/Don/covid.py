import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("ðð²ð»ð¾ðð´", callback_data='close_data')]])

@Client.on_message(filters.command("ð¦ covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**ð²ð¾ðð¸ð³ ð·ð¿ ð¸ð½ðµð¾ðð¼ð°ðð¸ð¾ð½**--
áâº Country : `{country}`
áâº Actived : `{active}`
áâº Confirmed : `{confirmed}`
áâº Deaths : `{deaths}`
áâº ID : `{info_id}`
áâº Last Update : `{last_update}`
áâº Latitude : `{latitude}`
áâº Longitude : `{longitude}`
áâº Recovered : `{recovered}`

<b> ð²ðð´ð³ð¸ðð âºâº 
<a href=https://t.me/Mod_Moviezx><b>ð¼ð¾ð³ ð¼ð¾ðð¸ð´ð ððð</a>
<a href=https://t.me/Syd_Xyz>ð¾ðð½ð´ððð</a>
<a href=https://t.me/malayalam_requester_bot>ð¶ðð¾ðð¿â¤ï¸âð¥</a>
<a href=https://t.me/gettglinks/9>ð±ð¾ððð®</a>
<a href=https://t.me/parallel_Cinemas>ð³ð°ðð° ð±ð°ðð´ðð</a>
<a href=https://t.me/bot_cracker>ð¼ð°ð¸ð½ ð²ð·ð°ð½ð½ð´ð»ðð«</b>"""
        return covid_info
    except Exception as error:
        return error
