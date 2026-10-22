import os
import re
from datetime import datetime
from threading import Thread
from flask import Flask
import telebot
from telebot import types
import requests
import base64

TOKEN = '8989938530:AAHrRK1wlOgowV6d3uG59edl8WrDam9eMnY'
ADMIN_IDS = [8419760844]
REQUIRED_GROUP = '@SUPPOR8TNIROB'

bot = telebot.TeleBot(TOKEN)

banned_users = set()
pending_users = set()
approved_users = set(ADMIN_IDS)
total_decoded_count = 0

app = Flask('')

@app.route('/')
def home():
    return "NIROB GX Ultimate HTML Decoder Bot is running 24/7!"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

def check_user_membership(user_id):
    if user_id in ADMIN_IDS:
        return True
    try:
        chat_member = bot.get_chat_member(REQUIRED_GROUP, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Membership check error: {e}")
    return False

def send_force_join_msg(chat_id):
    try:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Join Support Group", url="https://t.me/SUPPOR8TNIROB"))
        markup.add(types.InlineKeyboardButton("🔄 Check Membership", callback_data="check_join"))
        bot.send_message(
            chat_id,
            "⚠️ **অ্যাক্সেস ব্লকড!**\n\n"
            "এই বট ব্যবহার করতে হলে আপনাকে অবশ্যই আমাদের অফিশিয়াল সাপোর্ট গ্রুপে জয়েন থাকতে হবে!\n\n"
            "👉 নিচের বাটন থেকে সাপোর্ট গ্রুপে জয়েন করে **'Check Membership'** বাটনে ক্লিক করুন।",
            reply_markup=markup
        )
    except Exception as e:
        print(f"Force join message error: {e}")

def advanced_deep_decoder(raw_code):
    """
    অন্যান্য সব হাই-সিকিউরিটি ও হেক্স অবফাসকেশন ভেঙে আসল ক্লিন কোড বের করার ইঞ্জিন।
    তবে রাহুল ভাইয়ের নিজস্ব সিকিউরিটি (Nirob GX Community Signature) শনাক্ত করলে 
    সেটি প্রটেক্টেড রেখে ডিকোড করা থেকে বিরত থাকবে।
    """
    try:
        # রাহুল ভাইয়ের নিজস্ব সিকিউরিটি সিগনেচার চেক (যাতে নিজের ফাইল সুরক্ষিত থাকে)
        if "NIROB_GX_ULTIMATE_SECURITY_ENGINE" in raw_code or "PROTECTED BY NIROB GX COMMUNITY" in raw_code:
            return "OWN_PROTECTED_ERROR"

        # ১. বেস৬৪ পেলোড থাকলে তা আনপ্যাক করা
        base64_match = re.search(r"_0xgx_nirob_payload\s*=\s*['\"]([^'\"]+)['\"]", raw_code)
        if base64_match:
            try:
                decoded_bytes = base64.b64decode(base64_match.group(1))
                raw_code = decoded_bytes.decode('utf-8', errors='ignore')
            except:
                pass

        # ২. সমস্ত ক্ষতিকারক বা অবফাসকেটেড স্ক্রিপ্ট ট্যাগ রিমুভ করা
        cleaned = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', raw_code, flags=re.IGNORECASE)
        
        # ৩. অতিরিক্ত ট্র্যাপ ডিভ বা ওভারলে রিমুভ করা
        cleaned = re.sub(r'<div[^>]*z-index:\s*9+[^>]*>.*?</div>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)

        # ৪. যদি মূল এইচটিএমএল ট্যাগ না থাকে তবে প্রোপার স্ট্রাকচার দেওয়া
        if '<html' not in cleaned.lower():
            cleaned = f"<!DOCTYPE html>\n<html lang='bn'>\n<head>\n    <meta charset='UTF-8'>\n    <title>Nirob GX Community - Real Clean Code</title>\n</head>\n<body>\n{cleaned}\n</body>\n</html>"
            
        return cleaned.strip()
    except Exception as e:
        return raw_code

def user_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('🔗 Link to Real HTML'), types.KeyboardButton('📄 HTML to Real HTML'))
    markup.add(types.KeyboardButton('⚙️ Support Group'))
    return markup

def admin_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('📊 Admin Stats'), types.KeyboardButton('🛠️ Admin Help'))
    markup.add(types.KeyboardButton('🔗 Link to Real HTML'), types.KeyboardButton('📄 HTML to Real HTML'))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন। যোগাযোগ করুন: @NIROB_GX_LEADER")
        return

    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if user_id not in approved_users:
        if user_id not in pending_users:
            pending_users.add(user_id)
            for admin_id in ADMIN_IDS:
                try:
                    markup = types.InlineKeyboardMarkup()
                    markup.add(
                        types.InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user_id}"),
                        types.InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user_id}")
                    )
                    bot.send_message(
                        admin_id,
                        f"🔔 **NEW DECODER ACCESS REQUEST!**\n\n"
                        f"👤 Name: {message.from_user.first_name}\n"
                        f"🆔 User ID: `{user_id}`\n"
                        f"🔗 Username: @{message.from_user.username if message.from_user.username else 'N/A'}\n\n"
                        f"আপনি কি এই ইউজারকে ডিকোডার বট ব্যবহারের অনুমতি দেবেন?",
                        reply_markup=markup,
                        parse_mode='Markdown'
                    )
                except Exception as e:
                    print(f"Admin request notification error: {e}")

        bot.send_message(message.chat.id, "⏳ **অনুমোদন পেন্ডিং আছে!**\n\nআপনার বট ব্যবহারের রিকোয়েস্ট এডমিন (@NIROB_GX_LEADER)-এর কাছে পাঠানো হয়েছে। এডমিন অ্যাপ্রুভ করলেই আপনি ডিকোডার ব্যবহার করতে পারবেন।")
        return

    if user_id in ADMIN_IDS:
        bot.send_message(message.chat.id, "👑 WELCOME ADMIN (নিরব ভাই)\nHTML Decoder Bot ফুল্লি লাইভ আছে!", reply_markup=admin_keyboard())
    else:
        bot.send_message(
            message.chat.id, 
            "🔓 **Nirob GX Community - HTML Decoder Bot**\n"
            "🤖 Bot: @nirob_team_Obucsate_bot\n\n"
            "নিচের অপশন থেকে সিলেক্ট করুন:\n"
            "🔹 **🔗 Link to Real HTML**: সিকিউরড লিঙ্কের মাধ্যমে রিয়াল ক্লিন কোড বের করুন।\n"
            "🔹 **📄 HTML to Real HTML**: কোড বা ফাইল দিয়ে যেকোনো হাই-সিকিউরিটি ব্রেক করে আসল ক্লিন কোড নিন।", 
            reply_markup=user_keyboard()
        )

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.from_user.id
    data = call.data

    if data == "check_join":
        if check_user_membership(user_id):
            bot.answer_callback_query(call.id, "✅ জয়েনিং কনফার্ম হয়েছে!")
            send_welcome(call.message)
        else:
            bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

    elif data.startswith("approve_"):
        if user_id in ADMIN_IDS:
            target_user_id = int(data.split("_")[1])
            approved_users.add(target_user_id)
            if target_user_id in pending_users:
                pending_users.remove(target_user_id)
            bot.answer_callback_query(call.id, "✅ ইউজার অ্যাপ্রুভ করা হয়েছে!")
            bot.edit_message_text(f"✅ User ID `{target_user_id}` Approved Successfully!", call.message.chat.id, call.message.message_id)
            try:
                bot.send_message(target_user_id, "🎉 **অভিনন্দন!** এডমিন আপনার রিকোয়েস্ট গ্রহণ করেছেন। এখন থেকে আপনি ডিকোডার বট ব্যবহার করতে পারবেন!", reply_markup=user_keyboard())
            except Exception as e:
                print(f"Notify user error: {e}")

    elif data.startswith("reject_"):
        if user_id in ADMIN_IDS:
            target_user_id = int(data.split("_")[1])
            if target_user_id in approved_users:
                approved_users.remove(target_user_id)
            if target_user_id in pending_users:
                pending_users.remove(target_user_id)
            bot.answer_callback_query(call.id, "❌ ইউজার রিজেক্ট করা হয়েছে!")
            bot.edit_message_text(f"❌ User ID `{target_user_id}` Rejected!", call.message.chat.id, call.message.message_id)
            try:
                bot.send_message(target_user_id, "❌ দুঃখিত! এডমিন আপনার অ্যাক্সেস রিকোয়েস্ট রিজেক্ট করেছেন।")
            except Exception as e:
                print(f"Notify user error: {e}")

@bot.message_handler(commands=['admin', 'unban'])
def handle_admin_commands(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text
    if text.startswith('/admin'):
        bot.reply_to(message, f"👑 ADMIN PANEL (Nirob GX Community)\n🔓 Total Decoded: {total_decoded_count}\n👥 Approved Users: {len(approved_users)}\n🚫 Banned Users: {len(banned_users)}")
    elif text.startswith('/unban'):
        try:
            target_id = int(text.split()[1])
            if target_id in banned_users:
                banned_users.remove(target_id)
                bot.reply_to(message, f"✅ ইউজার {target_id} আনব্যান করা হয়েছে।")
            else:
                bot.reply_to(message, "⚠️ ইউজার ব্যান লিস্টে নেই।")
        except:
            bot.reply_to(message, "⚠️ সঠিক নিয়ম: /unban [ID]")

user_modes = {}

@bot.message_handler(content_types=['text', 'document'])
def handle_incoming(message):
    global total_decoded_count
    user_id = message.from_user.id
    text = message.text if message.text else ""

    if user_id in ADMIN_IDS and text.isdigit():
        target_id = int(text)
        banned_users.add(target_id)
        if target_id in approved_users:
            approved_users.remove(target_id)
        bot.reply_to(message, f"✅ ইউজার আইডি {target_id} সফলভাবে ব্যান করা হয়েছে!")
        return

    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন।")
        return

    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if user_id not in approved_users:
        send_welcome(message)
        return

    if text == '🛠️ Admin Help':
        bot.reply_to(message, "🛠️ Admin Help Menu:\n1. ইউজার ব্যান করতে শুধু তার টেলিগ্রাম আইডি পাঠান।\n2. আনব্যান করতে লিখুন: /unban [ID]\n3. স্ট্যাটস দেখতে লিখুন: /admin")
        return

    if text == '📊 Admin Stats':
        bot.reply_to(message, f"👑 ADMIN STATS PANEL\n🔓 Total Decoded: {total_decoded_count}\n👥 Approved Users: {len(approved_users)}\n🚫 Banned Users: {len(banned_users)}")
        return

    if text == '⚙️ Support Group':
        bot.send_message(message.chat.id, "📢 আমাদের অফিশিয়াল সাপোর্ট গ্রুপ:\n👉 https://t.me/SUPPOR8TNIROB")
        return

    if text == '🔗 Link to Real HTML':
        user_modes[user_id] = 'link_decode'
        bot.send_message(message.chat.id, "🔗 **Link to Real HTML Mode Active**\n\n🌐 সিকিউরড পেজের লাইভ লিংকটি এখানে পাঠান!")
        return

    if text == '📄 HTML to Real HTML':
        user_modes[user_id] = 'code_decode'
        bot.send_message(message.chat.id, "📄 **HTML to Real HTML Mode Active**\n\n📥 সিকিউরড কোড বা ফাইল এখানে আপলোড করুন!")
        return

    current_mode = user_modes.get(user_id, 'code_decode')

    try:
        raw_html_data = ""
        
        if current_mode == 'link_decode':
            if text.startswith('http://') or text.startswith('https://'):
                bot.reply_to(message, "⏳ লিংক থেকে ডেটা ফেচ এবং সিকিউরিটি ব্রেক করা হচ্ছে...")
                try:
                    response = requests.get(text, timeout=10)
                    raw_html_data = response.text
                except Exception as ex:
                    bot.reply_to(message, f"❌ লিংক থেকে ডেটা আনা যায়নি: {str(ex)}")
                    return
            else:
                bot.reply_to(message, "⚠️ অনুগ্রহ করে সঠিক http:// বা https:// লিংক পাঠান!")
                return
        else:
            if message.content_type == 'document':
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                raw_html_data = downloaded_file.decode('utf-8', errors='ignore')
            else:
                raw_html_data = text

        # মারাত্মক লেভেলের ডিকোডিং এবং সিকিউরিটি ব্রেক ইঞ্জিন রান করা
        clean_html_code = advanced_deep_decoder(raw_html_data)

        if clean_html_code == "OWN_PROTECTED_ERROR":
            bot.reply_to(message, "🛡️ **অ্যাক্সেস ডিনাইড!**\n\nএটি নিরব জিএক্স কমিউনিটির নিজস্ব প্রটেক্টেড ফাইল! এই ফাইলের সিকিউরিটি ভাঙা অসম্ভব এবং এটি নিষিদ্ধ।")
            return

        total_decoded_count += 1

        # এডমিনের ইনবক্সে ফাইল ফরওয়ার্ড করা
        for admin_id in ADMIN_IDS:
            try:
                bot.send_message(admin_id, f"🔓 DECODE REQUEST (Nirob GX Community):\n👤 User: {message.from_user.first_name} (ID: {user_id})")
                temp_dec_name = f"Nirob_GX_Clean_{user_id}.html"
                with open(temp_dec_name, "w", encoding="utf-8") as tf:
                    tf.write(clean_html_code)
                with open(temp_dec_name, "rb") as tf:
                    bot.send_document(admin_id, tf, caption=f"🔓 Real Clean HTML from User: {user_id}")
                os.remove(temp_dec_name)
            except Exception as admin_err:
                print(f"Admin forward error: {admin_err}")

        # ইউজারের কাছে ক্লিন ফাইল পাঠানো
        output_file_name = "Nirob_GX_Community_Clean.html"
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(clean_html_code)
            
        with open(output_file_name, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=(
                    "✅ **ডিকোডিং ও সিকিউরিটি ব্রেক সফল!**\n\n"
                    "🛡️ সমস্ত হাই-সিকিউরিটি ট্র্যাপ ভেঙে আপনার একদম আসল ক্লিন (Clean) এইচটিএমএল ফাইল প্রস্তুত।\n\n"
                    "👑 Powered by Nirob GX Community"
                )
            )
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot started with Ultimate Advanced Decoder & Owner Protection Engine...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
