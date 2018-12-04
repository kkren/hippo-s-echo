import telebot

API_TOKEN = '<api_token>'
USER_ID = '301949682'
TARGET_ID = '<target_id>'
bot = telebot.TeleBot('API_TOKEN')


@bot.message_handler(commands=['ping'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Pong, the ID is " + str(message.chat.id))


@bot.message_handler(content_types=["text", "sticker", "document", "photo", "audio", "video"])
def repeat_all_messages(message):
    if (message.from_user.id == USER_ID):
        bot.forward_message(TARGET_ID, message.chat.id, message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
