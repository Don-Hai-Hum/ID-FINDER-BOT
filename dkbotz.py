from pyrogram import Client, filters

api_id = 7651392
api_hash = "db62aa57ef8162bb4c95d0cf81e1c09b"
bot_token = "5707765751:AAHNPzjXHoT-cdVmsJqqUyXUsRTRHbFRlkI"

dkbotz = Client(
    "ID-FINDER-BOT",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@dkbotz.on_message(filters.private & filters.command("start"))
async def start_cmd(client, message):
    await message.reply(f"Hi {message.from_user.first_name}, \n\nI AM ID FINDER BOT\nSend /help For Info")

@dkbotz.on_message(filters.private & filters.command("help"))
async def help_cmd(client, message):
    await message.reply(f"How To Use Me\n\n/id - To Get Your\n\n/info - Get Your Profile Information")




dkbotz.run()
