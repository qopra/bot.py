from telegram.ext import Updater, CommandHandler

# وظيفة لرد البوت على أمر /start
def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت تلجرام.")

# الوظيفة الرئيسية لتشغيل البوت
def main():
    token = '8179120297:AAHAeCINYGOLrn6wLa0FYtV5WUR04Vja5xE'  # استبدل بـ Token الذي حصلت عليه من BotFather

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # إضافة معالج للأمر /start
    dispatcher.add_handler(CommandHandler('start', start))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
