import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from AlexaMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "- اهلين ياحلو تحكم من الازرار اسفل"




REPLY_MESSAGE_BUTTONS = [

         [

             ("‹ السورس ›"),                   

             ("")




          ],

          [

             ("‹ اوامر التشغيل ›"),

             ("‹ اوامر التفعيل ›")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^الاعدادات$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب الاعدادات**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("طريقة ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
