from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME, BOT_USERNAME, ASSISTANT_NAME, OWNER, GROUP_SUPPORT, UPDATES_CHANNEL, PROJECT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELBV5g_zDtu5CEiT6hNd5ZcL7QCzGznAACDQIAAqWPKVTYFqnjbykUNiAE")
    await message.reply_text(
        f"""**👋🏻 Halo {message.from_user.first_name}, saya adalah {BOT_NAME}, bot yang dapat memutar musik di voice chat group kamu.

✨ Welcome back to {bn}, Saya adalah bot musik yang dirancang agar dapat memutar musik di voice chat group anda dengan cara yang mudah dan praktis.

👩‍💻 Bot ini dikelola oleh {OWNER}.

💁🏻‍♀️ Anda ingin memutar musik di vcg?, silahkan tambahkan saya dan [assistant bot](https://t.me/{ASSISTANT_NAME}) ke grup anda dan jadikan admin.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ TAMBAHKAN KE GRUP ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🎶 GROUP 🎶", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        " CHANNEL ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 DONATION", url="https://t.me/Itsmeaceng"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ music player is online.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 CHANNEL 🌸", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        )
   )


