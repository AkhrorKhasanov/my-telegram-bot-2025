# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
CHAT_ID = 6697732961
updates = bot.get_updates()
message = bot.send_message(chat_id=CHAT_ID, text="Axror_bot")
photo='C:/Users/Defender/Desktop/aho.jpg'
photo = bot.send_photo(chat_id=CHAT_ID, photo=photo)
print(bot.send_document(chat_id=CHAT_ID, document='e:/Cdan/deutsch.docx'))
print(bot.send_audio(chat_id=CHAT_ID, audio='C:/Users/Defender/Desktop/1.ogg'))
print(bot.send_video(chat_id=CHAT_ID, video='C:/Users/Defender/Desktop/men.mp4'))


