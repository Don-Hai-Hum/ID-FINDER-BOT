from pyrogram import Client, filters
from forcers import force_sub
api_id = 7651392
api_hash = "db62aa57ef8162bb4c95d0cf81e1c09b"
bot_token = "5707765751:AAHNPzjXHoT-cdVmsJqqUyXUsRTRHbFRlkI"

dkbotz = Client(
    "ID-FINDER-BOT",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

ft = "Hi {message.from_user.mention}\n\nDue To Overload Only Channel Subscribers Can Use Me\n\n Join : @DK_BOTZ"
channel = "DK_BOTZ"


@dkbotz.on_message(filters.private & filters.command("start"))
async def start_cmd(client, message):
    Fsub = await force_sub(client, message, ft, channel)
    if Fsub == True:
       return 
    await message.reply(f"Hi {message.from_user.first_name}, \n\nI AM ID FINDER BOT\n\nSend /help For Info")

@dkbotz.on_message(filters.private & filters.command("help"))
async def help_cmd(client, message):
    Fsub = await force_sub(client, message, ft, channel)
    if Fsub == True:
       return
    await message.reply(f"How To Use Me\n\n/id - To Get Your\n\n/info - Get Your Profile Information")



print("Bot Started")
dkbotz.run()
