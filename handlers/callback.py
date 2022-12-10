import asyncio

from helpers.filters import command
from helpers.decorators import fallen
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_ID, START_IMG, OWNER_NAME, UPDATES_CHANNEL, ASSISTANT_NAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        f"""✨ **مرحبا عزيزي »「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
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



@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("طريقة الاستخدام")
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوة حساب المساعد
 4 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 
 💡 إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا منن خلال قروب الدعم الخاصة بي هنا ↤ @{GROUP_SUPPORT}

⚡ قناة البوت @{UPDATES_CHANNEL}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- رجـوع .", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر")
    await query.edit_message_text(
        f"""» **قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("- اوامـر الادمـنـيـه .", callback_data="cbadmin"),
                    InlineKeyboardButton("- اوامـر الـمـطـور .", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("- اوامـر الـتـشـغـيـل .", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("- رجـوع .", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» /end「لإنهاء الموسيقى / الفيديو في الكول」
» /song + 「الاسم تنزيل صوت من youtube」
» /skip「للتخطي إلى التالي」
» /ping 「إظهار حالة البوت بينغ」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- رجـوع .", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

» /pause 「ايقاف التشغيل موقتآ」
» /resume 「استئناف التشغيل」
» /stop「لإيقاف التشغيل」
» /userbotjoin「لاستدعاء الحساب المساعد」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- رجـوع .", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» /rmw「لحذف جميع الملفات 」
» /rmd「حذف جميع الملفات المحمله」
» /sysinfo「لمعرفه معلومات السيرفر」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- رجـوع .", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
