# import os
# import json
# import random
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# from telegram.error import Forbidden

# # Bot tokeni
# TOKEN = "7552596511:AAFU_AjhWH-bA3Xontk-T8qQ8gmmXlSxLM0"

# # Adminlar ro'yxati
# boss = 1179267491
# Admins = {5935789154, 1179267491, 6987013817, boss}

# # Majburiy kanallar
# required_channels = ['@RALPHLAURENUzb', '@LuxStoreTow']
# kanal = "@kinotime1515"

# # JSON fayl
# VIDEO_DATA_FILE = 'video_data.json'
# if os.path.exists(VIDEO_DATA_FILE):
#     with open(VIDEO_DATA_FILE, 'r') as f:
#         video_data = json.load(f)
# else:
#     video_data = {}

# def save_video_data():
#     with open(VIDEO_DATA_FILE, 'w') as f:
#         json.dump(video_data, f)

# def is_admin(chat_id):
#     return chat_id in Admins

# def generate_unique_code():
#     while True:
#         random_code = str(random.randint(1000, 9999))
#         if random_code not in video_data:
#             return random_code

# async def check_subscription(user_id, context):
#     if is_admin(user_id):
#         return True
    
#     for channel in required_channels:
#         chat_member = await context.bot.get_chat_member(chat_id=channel, user_id=user_id)
#         if chat_member.status not in ["member", "administrator", "creator"]:
#             return False
#     return True

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Botga xush kelibsiz!")

# async def tag_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.message.chat_id
#     if not is_admin(chat_id):
#         return await update.message.reply_text("Siz admin emassiz!")
    
#     args = context.args
#     if len(args) < 2:
#         return await update.message.reply_text("/tag <videoRaqami> <description>")
    
#     video_code = args[0]
#     description = ' '.join(args[1:])
#     if video_code in video_data:
#         video_data[video_code]['description'] = description
#         save_video_data()
#         await update.message.reply_text(f"Video {video_code} uchun tavsif o'zgartirildi.")
#     else:
#         await update.message.reply_text("Bunday video mavjud emas!")

# async def tag_del(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.message.chat_id
#     if not is_admin(chat_id):
#         return await update.message.reply_text("Siz admin emassiz!")
    
#     args = context.args
#     if len(args) < 1:
#         return await update.message.reply_text("/tag_del <videoRaqami>")
    
#     video_code = args[0]
#     if video_code in video_data:
#         video_data[video_code]['description'] = ""
#         save_video_data()
#         await update.message.reply_text(f"Video {video_code} tavsifi o‘chirildi.")
#     else:
#         await update.message.reply_text("Bunday video mavjud emas!")

# async def delete_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.message.chat_id
#     if not is_admin(chat_id):
#         return await update.message.reply_text("Siz admin emassiz!")
    
#     args = context.args
#     if len(args) < 1:
#         return await update.message.reply_text("/delete_video <videoRaqami>")
    
#     video_code = args[0]
#     if video_code in video_data:
#         del video_data[video_code]
#         save_video_data()
#         await update.message.reply_text(f"Video {video_code} o‘chirildi.")
#     else:
#         await update.message.reply_text("Bunday video mavjud emas!")

# async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.message.chat_id
#     if not is_admin(chat_id):
#         return await update.message.reply_text("Siz admin emassiz!")
    
#     video = update.message.video
#     description = update.message.caption or "No description"
#     random_code = generate_unique_code()
    
#     sent_message = await context.bot.send_video(chat_id=kanal, video=video.file_id, caption=description)
#     file_id = sent_message.video.file_id
    
#     video_data[random_code] = {'file_id': file_id, 'description': description}
#     save_video_data()
    
#     await update.message.reply_text(f"Video qabul qilindi! Kod: {random_code}")

# async def handle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.message.chat_id
#     user_id = update.message.from_user.id
#     code = update.message.text.strip()
    
#     if not await check_subscription(user_id, context):
#         keyboard = [[InlineKeyboardButton("A‘zo bo‘lish", url="https://t.me/Panda571kulgiTime")],
#                     [InlineKeyboardButton("A‘zo bo‘lish", url="https://t.me/LuxStoreTow")]]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         return await update.message.reply_text("Videoni olish uchun quyidagi kanallarga a‘zo bo‘ling!", reply_markup=reply_markup)
    
#     if code in video_data:
#         video_info = video_data[code]
#         await context.bot.send_video(chat_id=chat_id, video=video_info['file_id'], caption=video_info['description'])
#     else:
#         await update.message.reply_text("Noto‘g‘ri kod!")

# def main():
#     application = Application.builder().token(TOKEN).build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("tag", tag_video))
#     application.add_handler(CommandHandler("tag_del", tag_del))
#     application.add_handler(CommandHandler("delete_video", delete_video))
#     application.add_handler(MessageHandler(filters.VIDEO, handle_video))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code))
#     application.run_polling()

# if __name__ == '__main__':
#     main()


while True:
    print("while works")
