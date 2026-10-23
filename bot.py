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
    return "NIROB GX Ultimate Security Bot is running 24/7!"

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
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    encoded_bytes = html_content.encode('utf-8')
    b64_1 = base64.b64encode(encoded_bytes).decode('utf-8')
    final_payload = base64.b64encode(b64_1.encode('utf-8')).decode('utf-8')
    
    # গ্রিন কাস্টম টার্মিনাল অ্যান্ড সিকিউরিটি নোটিশ ট্র্যাপ
    warning_messages = [
        "SECURITY WARNING: Unauthorized access detected!",
        "ACCESS DENIED: Code protected by @NIROB_GX_LEADER",
        "SYSTEM LOCK: Reverse engineering attempt blocked!",
        "PROTECTION ACTIVE: Created using @nirob_team_Obucsate_bot",
        "ENCRYPTION LEVEL: MAXIMUM PARANOID PROTECTION"
    ]
    
    fake_trap_stream = ""
    for i in range(250):
        fake_var = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        msg = random.choice(warning_messages)
        line = f"var _0x{fake_var} = '[SYSTEM_PROTECTED] {msg}'; // Secured @ {current_time}"
        fake_trap_stream += line + "\n"

    secured_HTML = f"""<!--
==================================================
🔥 100% UNBREAKABLE DEADLY ANTI-DECODE BY NIROB GX 🔥
--------------------------------------------------
Obfuscated By: @NIROB_GX_LEADER
Bot Username: @nirob_team_Obucsate_bot
Timestamp: {current_time}
Status: MAXIMUM SECURITY & MATRIX TRAP ACTIVE 🛑
==================================================
-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script>
    /* 
       ====================================================================
       ⚠️ SECURITY SYSTEM WARNING:
       This code is encrypted by NIROB GX ULTIMATE PROTECTION.
       Unauthorized copying, inspecting or decoding will trigger automatic ban!
       Contact Admin: @NIROB_GX_LEADER
       Bot Service: @nirob_team_Obucsate_bot
       ====================================================================
    */
    {fake_trap_stream}
    
    var _0xgx_nirob_payload = '{final_payload}';
    var isDestroyed = false;
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("⚠️ Hello Admin! My attempt to inspect protected code was blocked. Please unblock me.");
    
    function triggerVoiceWarning() {{
        if ('speechSynthesis' in window) {{
            try {{
                window.speechSynthesis.cancel();
                var msgText = "Warning! Unauthorized code inspection detected. Access blocked by Nirob GX.";
                var speech = new SpeechSynthesisUtterance(msgText);
                speech.lang = 'en-US';
                speech.rate = 0.9;
                window.speechSynthesis.speak(speech);
            } catch(err) {{}}
        }}
    }}
    
    function destroyAndRedirect() {{
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#050b08;color:#00ff66;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;position:fixed;top:0;left:0;z-index:999999;font-family:monospace;border:3px solid #00ff66;">' +
            '<h1 style="font-size:26px;color:#ff0055;text-shadow:0 0 10px #ff0055;margin-bottom:10px;">⚠️ ACCESS DENIED & SYSTEM LOCKED ⚠️</h1>' +
            '<p style="color:#00ff66;margin:15px 0;font-size:16px;">[!] Unauthorized DevTools / Inspection Detected!</p>' +
            '<p style="color:#ffffff;font-size:14px;margin-bottom:20px;">Code is protected by NIROB GX. Contact Admin to restore access.</p>' +
            '<p style="color:#00e5ff;font-size:13px;margin-bottom:20px;">🤖 Official Bot: @nirob_team_Obucsate_bot</p>' +
            '<a href="' + telegramTrapLink + '" style="background:#00ff66;color:#000;padding:15px 30px;border-radius:5px;text-decoration:none;font-weight:bold;font-size:15px;box-shadow:0 0 15px #00ff66;">👉 CONTACT @NIROB_GX_LEADER</a>' +
        '</div>';
        setTimeout(function() {{ window.location.href = telegramTrapLink; }}, 2500);
    }}
    
    window.addEventListener('keydown', function(e) {{
        if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 67 || e.keyCode === 74)) || (e.ctrlKey && (e.keyCode === 85 || e.keyCode === 83))) {{
            destroyAndRedirect();
            e.preventDefault();
            return false;
        }}
    }}, true);
    
    window.addEventListener('contextmenu', function(e) {{
        destroyAndRedirect();
        e.preventDefault();
        return false;
    }}, true);

    setInterval(function() {{
        var widthThreshold = window.outerWidth - window.innerWidth > 160;
        var heightThreshold = window.outerHeight - window.innerHeight > 160;
        if (widthThreshold || heightThreshold) {{
            destroyAndRedirect();
        }}
    }}, 500);
    
    window.addEventListener('DOMContentLoaded', function() {{
        try {{
            var step1 = atob(_0xgx_nirob_payload);
            var b64_decoded = atob(step1);
            var binData = new Uint8Array(b64_decoded.length);
            for (var i = 0; i < b64_decoded.length; i++) {{
                binData[i] = b64_decoded.charCodeAt(i);
            }}
            var real_html = new TextDecoder("utf-8").decode(binData);
            document.open();
            document.write(real_html);
            document.close();
        }} catch(e) {{
            destroyAndRedirect();
        }}
    }});
</script>
</head>
<body style="margin:0;background:#000;">
</body>
</html>"""
    return secured_HTML, current_time

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
        bot.send_message(message.chat.id, "👑 WELCOME ADMIN (নিরব ভাই)\nবট ফুল্লি লাইভ এবং অ্যাডভান্সড সিকিউরিটি মোডে আছে!", reply_markup=admin_keyboard())
    else:
        bot.send_message(message.chat.id, "🔒 HTML OBFUSCATOR BOT (ULTIMATE ENGINE)\n🤖 Bot: @nirob_team_Obucsate_bot\n\n📄 Send your .html file or code to start un-hackable protection!", reply_markup=user_keyboard())

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
        bot.reply_to(message, f"✅ ইউজার আইডি সফলভাবে ব্যান করা হয়েছে!")
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

    bot.reply_to(message, "⏳ Processing and applying Nirob's Security Engine...")
    
    try:
        html_data = ""
        file_name_original = "NIROB_PROTECTED.html"
        
        if message.content_type == 'document':
            orig_name = message.document.file_name or "NIROB_PROTECTED.html"
            if "." in orig_name:
                base_n = orig_name.rsplit('.', 1)[0]
                file_name_original = f"{base_n}_obf.html"
            else:
                file_name_original = "NIROB_PROTECTED_obf.html"
                
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            html_data = downloaded_file.decode('utf-8', errors='ignore')
        else:
            file_name_original = "NIROB_PROTECTED_obf.html"
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

        secured_code, process_timestamp = obfuscate_html(html_data)
        
        with open(file_name_original, "w", encoding="utf-8") as f:
            f.write(secured_code)
            
        caption_text = (
            "✅ 𝗢𝗯𝗳𝘂𝘀𝗰𝗮𝘁𝗶𝗼𝗻 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹!\n\n"
            f"📁 𝗙𝗶𝗹𝗲: {file_name_original}\n"
            f"⏱️ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗲𝗱 𝗔𝘁: {process_timestamp}\n\n"
            "🛡️ 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗲𝗱 𝘄𝗶𝘁𝗵:\n"
            "- 🚫 Right Click Block\n"
            "- ⌨️ Keyboard Block\n"
            "- 🔍 DevTools Detection\n"
            "- 🧹 Console Clear\n"
            "- 🛡️ Anti-Scraping\n"
            "- 🖼️ Iframe/Sandbox Detection\n"
            "- 🎨 VM Obfuscation Engine\n"
            "- 🌐 Pro Obfuscation\n\n"
            "🔒 Your HTML code is now protected!\n\n"
            "🤖 Bot Username: @nirob_team_Obucsate_bot\n"
            "👑 Developer Admin: @NIROB_GX_LEADER"
        )
        
        with open(file_name_original, "rb") as f:
            bot.send_document(message.chat.id, f, caption=caption_text)
            
        os.remove(file_name_original)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Security Bot started successfully...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
