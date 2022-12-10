import asyncio

from helpers.filters import command
from helpers.decorators import fallen
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_ID, START_IMG, OWNER_NAME, UPDATES_CHANNEL, ASSISTANT_NAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""✨ **مرحبا عزيزي » {message.from_user.mention()} !**\n
💭 **انا بوت استطيع تشغيل الموسيقي والفديو في محادثتك الصوتية**

💡 تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » - الاوامـر . !

""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- الاوامـر .", callback_data="cbcmds"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "- قـنـاة الـسـورس .", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "- جـروب الـدعـم .", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "- اضفني لمجموعتك .", url=f"https://t.me/{bu}?startgroup=true"
                    ),
                    
                    InlineKeyboardButton(
                        "- الـمـطـور .", url="https://t.me/VR_LA"
                    )]
            ]
       ),
    )

