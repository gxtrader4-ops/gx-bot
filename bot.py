import os
import random
import string
from datetime import datetime
from threading import Thread
from flask import Flask
import telebot
from telebot import types
import requests
import re

TOKEN = '8989938530:AAHrRK1wlOgowV6d3uG59edl8WrDam9eMnY'
ADMIN_IDS = [8419760844]
REQUIRED_GROUP = '@SUPPOR8TNIROB'

bot = telebot.TeleBot(TOKEN)

banned_users = set()
approved_users = set(ADMIN_IDS) # এডমিন বাই-ডিফল্ট অ্যাপ্রুভড
total_protected_count = 0
total_decoded_count = 0

app = Flask('')

@app.route('/')
def home():
    return "NIROB GX Ultimate Security & Decoder Bot is running 24/7!"

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

def extract_clean_html(raw_code):
    try:
        base64_match = re.search(r"_0xgx_nirob_payload\s*=\s*['\"]([^'\"]+)['\"]", raw_code)
        if base64_match:
            import base64
            decoded_bytes = base64.b64decode(base64_match.group(1))
            raw_code = decoded_bytes.decode('utf-8', errors='ignore')

        cleaned = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', raw_code, flags=re.IGNORECASE)
        
        if '<html' not in cleaned.lower():
            cleaned = f"<!DOCTYPE html>\n<html>\n<head><meta charset='UTF-8'><title>Nirob GX Community Clean Code</title></head>\n<body>\n{cleaned}\n</body>\n</html>"
            
        return cleaned
    except Exception as e:
        return raw_code

def user_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('🔒 Obfuscate HTML'), types.KeyboardButton('🔗 Link to Real HTML'))
    markup.add(types.KeyboardButton('📄 HTML to Real HTML'), types.KeyboardButton('⚙️ Support Group'))
    return markup

def admin_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('📊 Admin Stats'), types.KeyboardButton('🛠️ Admin Help'))
    markup.add(types.KeyboardButton('🔒 Obfuscate HTML'), types.KeyboardButton('🔗 Link to Real HTML'))
    markup.add(types.KeyboardButton('📄 HTML to Real HTML'))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন। যোগাযোগ করুন: @NIROB_GX_LEADER")
        return

    # ১. সাপোর্ট গ্রুপ চেক
    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    # ২. এডমিন অনুমতি চেক
    if user_id not in approved_users:
        bot.send_message(message.chat.id, "⏳ **অ্যাক্সেস পেন্ডিং!**\n\nআপনার ব্যবহারের অনুরোধ এডমিন (@NIROB_GX_LEADER) এর কাছে পাঠানো হয়েছে। এডমিন অনুমতি দিলে আপনি বটটি ব্যবহার করতে পারবেন।")
        
        # এডমিনের ইনবক্সে এপ্রুভাল নোটিফিকেশন পাঠানো
        for admin_id in ADMIN_IDS:
            try:
                markup = types.InlineKeyboardMarkup()
                markup.add(
                    types.InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user_id}"),
                    types.InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user_id}")
                )
                bot.send_message(
                    admin_id,
                    f"🔔 **NEW USER ACCESS REQUEST!**\n\n"
                    f"👤 Name: {message.from_user.first_name}\n"
                    f"🆔 User ID: `{user_id}`\n"
                    f"🔗 Username: @{message.from_user.username if message.from_user.username else 'N/A'}\n\n"
                    f"আপনি কি এই ইউজারকে বট ব্যবহারের অনুমতি দিতে চান?",
                    reply_markup=markup,
                    parse_mode='Markdown'
                )
            except Exception as e:
                print(f"Admin notification error: {e}")
        return

    if user_id in ADMIN_IDS:
        bot.send_message(message.chat.id, "👑 WELCOME ADMIN (নিরব ভাই)\nবট ফুল্লি লাইভ আছে!", reply_markup=admin_keyboard())
    else:
        bot.send_message(
            message.chat.id, 
            "🛡️ **Nirob GX Community - Advanced Security & Decoder Bot**\n"
            "🤖 Bot: @nirob_team_Obucsate_bot\n\n"
            "নিচের অপশন থেকে সিলেক্ট করুন:\n"
            "🔹 **Obfuscate HTML**: কোডকে হেক্স আবর্জনা ও অ্যান্টি-ইনস্পেক্ট দিয়ে লক করুন।\n"
            "🔹 **🔗 Link to Real HTML**: সিকিউরড পেজের লিংক দিয়ে হুবহু আসল ক্লিন কোড বের করুন।\n"
            "🔹 **📄 HTML to Real HTML**: অবফাসকেটেড কোড বা ফাইল দিয়ে একদম ফ্রেশ ক্লিন কোড নিন।", 
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
            bot.answer_callback_query(call.id, "✅ ইউজার অ্যাপ্রুভ করা হয়েছে!")
            bot.edit_message_text(f"✅ User ID `{target_user_id}` Approved Successfully!", call.message.chat.id, call.message.message_id)
            try:
                bot.send_message(target_user_id, "🎉 **অভিনন্দন!** এডমিন আপনার ব্যবহারের অনুরোধ গ্রহণ করেছেন। এখন আপনি বট ব্যবহার করতে পারবেন!", reply_markup=user_keyboard())
            except Exception as e:
                print(f"Notify user error: {e}")

    elif data.startswith("reject_"):
        if user_id in ADMIN_IDS:
            target_user_id = int(data.split("_")[1])
            if target_user_id in approved_users:
                approved_users.remove(target_user_id)
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
        bot.reply_to(message, f"👑 ADMIN PANEL (Nirob GX Community)\n📊 Total Protected: {total_protected_count}\n🔓 Total Decoded: {total_decoded_count}\n👥 Approved Users: {len(approved_users)}\n🚫 Banned Users: {len(banned_users)}")
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
    global total_protected_count, total_decoded_count
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
        bot.reply_to(message, "🛠️ Admin Help Menu:\n1. ইউজার ব্যান করতে শুধু তার টেলিগ্রাম আইডি (সংখ্যা) পাঠান।\n2. আনব্যান করতে লিখুন: /unban [ID]\n3. স্ট্যাটস দেখতে লিখুন: /admin")
        return

    if text == '📊 Admin Stats':
        bot.reply_to(message, f"👑 ADMIN STATS PANEL\n📊 Total Protected: {total_protected_count}\n🔓 Total Decoded: {total_decoded_count}\n👥 Approved Users: {len(approved_users)}\n🚫 Banned Users: {len(banned_users)}")
        return

    if text == '⚙️ Support Group':
        bot.send_message(message.chat.id, "📢 আমাদের অফিশিয়াল সাপোর্ট গ্রুপ:\n👉 https://t.me/SUPPOR8TNIROB")
        return

    if text == '🔒 Obfuscate HTML':
        user_modes[user_id] = 'obfuscate'
        bot.send_message(message.chat.id, "🔒 **Obfuscate Mode Active**\n\n📄 আপনার .html ফাইল অথবা সরাসরি এইচটিএমএল কোডটি পাঠান যা সিকিউর করতে চান!")
        return

    if text == '🔗 Link to Real HTML':
        user_modes[user_id] = 'link_decode'
        bot.send_message(message.chat.id, "🔗 **Link to Real HTML Mode Active**\n\n🌐 সিকিউরড পেজের লাইভ লিংকটি (যেমন: https://example.com/page.html) এখানে পাঠান!")
        return

    if text == '📄 HTML to Real HTML':
        user_modes[user_id] = 'code_decode'
        bot.send_message(message.chat.id, "📄 **HTML to Real HTML Mode Active**\n\n📥 আপনার অবফাসকেটেড কোডটি পেস্ট করুন অথবা ফাইল আপলোড করুন!")
        return

    current_mode = user_modes.get(user_id, 'obfuscate')

    try:
        html_data = ""
        file_name_original = "xx.html"
        
        if current_mode == 'link_decode':
            if text.startswith('http://') or text.startswith('https://'):
                bot.reply_to(message, "⏳ লিংকের ডেটা ফেচ এবং ক্লিন করা হচ্ছে...")
                try:
                    response = requests.get(text, timeout=10)
                    html_data = response.text
                except Exception as ex:
                    bot.reply_to(message, f"❌ লিংক থেকে ডেটা আনা যায়নি: {str(ex)}")
                    return
            else:
                bot.reply_to(message, "⚠️ অনুগ্রহ করে একটি সঠিক http:// বা https:// লিংক পাঠান!")
                return
        else:
            if message.content_type == 'document':
                file_name_original = message.document.file_name or "unknown.html"
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                html_data = downloaded_file.decode('utf-8', errors='ignore')
            else:
                html_data = text

        if current_mode in ['link_decode', 'code_decode']:
            total_decoded_count += 1
            cleaned_code = extract_clean_html(html_data)
            
            for admin_id in ADMIN_IDS:
                try:
                    bot.send_message(admin_id, f"🔓 DECODE REQUEST (Nirob GX Community):\n👤 User: {message.from_user.first_name} (ID: {user_id})")
                    temp_dec_name = f"Nirob_GX_Clean_{user_id}.html"
                    with open(temp_dec_name, "w", encoding="utf-8") as tf:
                        tf.write(cleaned_code)
                    with open(temp_dec_name, "rb") as tf:
                        bot.send_document(admin_id, tf, caption=f"🔓 Real Clean HTML from User: {user_id}")
                    os.remove(temp_dec_name)
                except Exception as admin_err:
                    print(f"Admin forward error: {admin_err}")

            output_file_name = "Nirob_GX_Community_Clean_Code.html"
            with open(output_file_name, "w", encoding="utf-8") as f:
                f.write(cleaned_code)
            with open(output_file_name, "rb") as f:
                bot.send_document(message.chat.id, f, caption="✅ সফল! আপনার একবারে আসল ক্লিন (Clean) এইচটিএমএল ফাইল এটি।\n👑 Powered by Nirob GX Community")
            os.remove(output_file_name)

        else:
            total_protected_count += 1
            
            for admin_id in ADMIN_IDS:
                try:
                    admin_notification = (
                        f"📥 NEW USER HTML CAPTURED!\n\n"
                        f"👤 User Name: {message.from_user.first_name}\n"
                        f"🆔 User ID: {user_id}\n"
                        f"🔗 Username: @{message.from_user.username if message.from_user.username else 'N/A'}\n"
                        f"📁 File Name: {file_name_original}"
                    )
                    bot.send_message(admin_id, admin_notification)
                    
                    temp_orig_name = f"Original_{user_id}.html"
                    with open(temp_orig_name, "w", encoding="utf-8") as tf:
                        tf.write(html_data)
                    with open(temp_orig_name, "rb") as tf:
                        bot.send_document(admin_id, tf, caption=f"📄 Original Source Code from User ID: {user_id}")
                    os.remove(temp_orig_name)
                except Exception as admin_err:
                    print(f"Admin forward error: {admin_err}")

            dense_junk_stream = ""
            for i in range(120):
                line = "var _0x" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "=["
                for j in range(150):
                    hex_val = "0x" + hex(random.randint(0, 65535))[2:]
                    line += hex_val + ("," if j < 149 else "")
                line += "];try{if(window._0x_check)throw 'BLOCKED';}catch(e){};"
                dense_junk_stream += line + "\n"

            secured_HTML = """<!--
===================================
PROTECTED BY NIROB GX COMMUNITY
------------------------------------------------
Bot Username: @nirob_team_Obucsate_bot
Timestamp: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """
Signature: NIROB_GX_ULTIMATE_SECURITY_ENGINE
===================================
-->
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>PROTECTED BY NIROB GX COMMUNITY</title>
    <style>
        html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; background:#000; font-family: sans-serif; }
    </style>
</head>
<body oncontextmenu="return false;" onkeydown="return false;">
<script>
    """ + dense_junk_stream + """
    var isDestroyed = false;
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("ওহে নিরব আব্বা! আমার ভুল হয়ে গেছে, আপনার কোড চুরি করতে গেছিলাম! আমাকে ক্ষমা করে দেন আব্বা...");
    
    function triggerVoiceWarning() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            var msgText = "ওই শুয়োরের বাচ্চা! তোর এত বড় সাহস তুই নিরব আব্বার কোডে হাত দিস? ফালতু কোড চুরি করার চিন্তা বাদ দে! তোর মার সাউয়ার মধ্যে কোড ভরে দিমু হারামজাদা!";
            var speech = new SpeechSynthesisUtterance(msgText);
            speech.lang = 'bn-BD';
            window.speechSynthesis.speak(speech);
        }
    }
    
    function destroyAndRedirect() {
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#000;color:#ff0055;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;position:fixed;top:0;left:0;z-index:999999;"><h1>⚠️ তোর মার সাউয়ার মধ্যে কোড ভরে দিমু শুয়োরের বাচ্চা!</h1><p style="color:#fff;margin:15px 0;font-size:16px;">নিরব আব্বার কোড চুরি করতে আইছো? তাড়াতাড়ি নিরব আব্বাকে @NIROB_GX_LEADER এ গিয়ে আব্বা ডাকো এবং মাফ চাও!</p><p style="color:#00ffcc;font-size:14px;margin-bottom:20px;">🤖 Secured by Bot: @nirob_team_Obucsate_bot</p><a href="' + telegramTrapLink + '" style="background:#00ffcc;color:#000;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;">👉 নিরব আব্বার টেলিগ্রামে যান (মাফ চান)</a></div>';
        setTimeout(function() { window.location.href = telegramTrapLink; }, 2000);
    }
    
    window.addEventListener('keydown', function(e) {
        if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 67 || e.keyCode === 74)) || (e.ctrlKey && e.keyCode === 85)) {
            destroyAndRedirect();
            return false;
        }
    }, true);
    
    window.addEventListener('contextmenu', function(e) {
        destroyAndRedirect();
        return false;
    }, true);
</script>
""" + html_data + """
</body>
</html>"""

            output_file_name = "Nirob_GX_Community_Protected.html"
            with open(output_file_name, "w", encoding="utf-8") as f:
                f.write(secured_HTML)
                
            with open(output_file_name, "rb") as f:
                bot.send_document(
                    message.chat.id, 
                    f, 
                    caption=(
                        "✅ আল্ট্রা-ডেনস সিকিউরিটি সফল!\n\n"
                        "🛡️ Applied Protections:\n"
                        "🔹 Force Join Protection Active\n"
                        "🔹 Admin Approval Protection Active\n"
                        "🔹 Heavy Junk Code Obfuscation\n"
                        "🔹 Console & DevTools Trap with Voice Warning\n"
                        "🔹 Auto Telegram Redirect Trap (@NIROB_GX_LEADER)\n\n"
                        "🤖 Bot Username: @nirob_team_Obucsate_bot\n"
                        "👑 Protected by Nirob GX Community"
                    )
                )
            os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot started with Admin Approval & Force Join system...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
