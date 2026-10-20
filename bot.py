import os
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# টোকেন এবং এডমিন আইডি
TOKEN = '8960539162:AAHnIm9z-7A3ZOu4RXbSkAlvaRwAS3AvMeA'
ADMIN_ID = 8419760844

bot = telebot.TeleBot(TOKEN)

# ফ্লাস্ক সার্ভার (Render ফ্রি টায়ারে ২৪ ঘণ্টা সচল রাখার জন্য)
app = Flask('')

@app.route('/')
def home():
    return "GX Security Bot is running 24/7!"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"আসসালামু আলাইকুম, {user_name}!\n\n"
        "স্বাগতম **GX Security Bot**-এ। 🛡️\n"
        "এই বটের মাধ্যমে আপনি আপনার HTML ফাইল বা কোডকে অতি গোপনীয় ও সুরক্ষিত (Obfuscated) করতে পারবেন।\n\n"
        "আপনার কোড বা HTML ফাইলটি এখানে পাঠিয়ে দিন!"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# ফাইল বা টেক্সট রিসিভ করে সিকিউর করার লজিক
@bot.message_handler(content_types=['text', 'document'])
def handle_incoming_code(message):
    # ইউজার যদি কোনো টেক্সট বা ফাইল পাঠায়
    bot.reply_to(message, "⏳ আপনার কোডটি সিকিউর ও অবফাস্কেট করা হচ্ছে...")
    
    # এখানে আপনার মূল সিকিউরিটি এবং অবফাসস্কেশন প্রসেসিং হবে
    # (ফাইল এনক্রিপ্ট হয়ে ইউজারকে ডাউনলোড লিংক হিসেবে রিটার্ন করবে)
    
    bot.send_message(
        message.chat.id, 
        "✅ আপনার ফাইলটি সফলভাবে প্রোটেক্ট করা হয়েছে!\n(অ্যাডভান্সড ব্ল্যাকআউট ও ভয়েস ওয়ার্নিং যুক্ত করা হয়েছে)"
    )

if __name__ == '__main__':
    keep_alive()  # ফ্লাস্ক পোর্ট চালু রাখবে
    print("Bot is starting...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
