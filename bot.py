import os
import random
import string
from datetime import datetime
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# নতুন টেলিগ্রাম বট টোকেন এবং আপনার (নিরব ভাই) এডমিন আইডি
TOKEN = '8987787400:AAF_bIN5JWb_J9Dsy5X6P08pgyU5_DpBtpA'
ADMIN_IDS = [8419760844]  # এখানে প্রয়োজনে আরও অ্যাডমিন আইডি যোগ করতে পারবেন

bot = telebot.TeleBot(TOKEN)

# ডেটাবেস স্টোরেজ
banned_users = set()
total_protected_count = 0

# ফ্লাস্ক সার্ভার (Render ফ্রি টায়ারে ২৪ ঘণ্টা সচল রাখার জন্য)
app = Flask('')

@app.route('/')
def home():
    return "NIROB GX Security Bot is running 24/7!"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# আপনার আসল ব্রান্ডেড সিকিউরিটি হেডার ও হেভি ডেনস অবফাস্কেটর
def obfuscate_html(html_content):
    import base64
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    encoded_bytes = html_content.encode('utf-8')
    encoded_payload = base64.b64encode(encoded_bytes).decode('utf-8')
    
    dense_junk_stream = ""
    for i in range(40):
        line = "var _0x" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "=["
        for j in range(120):
            hex_val = "0x" + hex(random.randint(0, 65535))[2:]
            line += hex_val + ("," if j < 119 else "")
        line += "];try{if(window._0x_check)throw 'BLOCKED';}catch(e){};"
        dense_junk_stream += line + "\n"

    secured_HTML = f"""<!--
===================================
PROTECTED - DO NOT MODIFY THIS HEADER
------------------------------------------------
Obfuscated By: @nirobvip_bott
TG: @NIROB_GX_LEADER
Timestamp: {current_time}
Signature: NIROB_GX_PROTECTED_ENGINE
------------------------------------------------
WARNING: Removing or modifying this credit header
will cause this page to stop working!
===================================
-->
<!DOCTYPE html>
<!--=========================================================================================
🔥 MASSIVE DENSE STREAM OBFUSCATION ENGINE ACTIVATED 🔥
=========================================================================================
⚠️ এই তোরা ফালতু চুরি করার চিন্তা বাদ দে!
⚠️ তোর নিরব আব্বার কোডে হাত দিলে হাত-চোখ ভাইঙ্গা হাতে ধরাইয়া দিমু!
⚠️ খাঁটি বাংলা ভাষায় বলে দিলাম— আসল কোড জীবনেও পাইবি না, সোজা তোর নিরব আব্বার কাছে মাফ চা!
=========================================================================================
👑 CREATOR & DEVELOPER  : NIROB (নিরব)
💬 TELEGRAM OFFICIAL   : @NIROB_GX_LEADER
🌐 COMMUNITY           : GX BIG COMMUNITY
=========================================================================================-->
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROTECTED BY NIROB | @NIROB_GX_LEADER</title>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background: #000;
        }}
        iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
</head>
<body oncontextmenu="return false;" onkeydown="return false;">
<script>
    {dense_junk_stream}
    var _0xgx_nirob_payload = "{encoded_payload}";
    var isDestroyed = false;
    
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("নিরব আব্বা আমার ভুল হয়ে গেছে! আমাকে মাফ করে দেন, আপনার এই কোডটা আমার খুব প্রয়োজন...");
    
    function triggerVoiceWarning() {{
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var msgText = "ওই শয়তানের বাচ্চা! তোর এত্ত বড় সাহস তুই নিরব আব্বার কোডে হাত দেস? ফালতু কোড চুরি করার চিন্তা বাদ দে! আসল কোড জীবনেও পাইবি না! সোজা গিয়া তোর নিরব আব্বার পায়ে ধইরা মাফ চা! টেলিগ্রাম একাউন্ট এট দ্য রেট নিরব জি এক্স লিডার।";
            var speech = new SpeechSynthesisUtterance(msgText);
            speech.lang = 'bn-BD';
            speech.pitch = 1.0;
            speech.rate = 1.0;
            window.speechSynthesis.speak(speech);
        }}
    }}
    
    function destroyAndRedirect() {{
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#000;color:#ff0055;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;font-family:sans-serif;padding:20px;"><h1 style="font-size:30px;margin-bottom:15px;text-shadow:0 0 10px #ff0055;">⚠️ ACCESS DENIED BY NIROB ABBA!</h1><p style="font-size:18px;color:#fff;margin-bottom:25px;">তোরা আসল কোড কখনোই পাইবি না! সোজা তোর নিরব আব্বার পায়ে ধরে মাফ চা!</p><a href="' + telegramTrapLink + '" style="background:#00ffcc;color:#000;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:20px;box-shadow:0 0 15px #00ffcc;">👉 নিরব আব্বার টেলিগ্রামে যান</a></div>';
        setTimeout(function() {{
            window.location.href = telegramTrapLink;
        }}, 1500);
    }}
    
    (function() {{
        window.addEventListener('keydown', function(e) {{
            if (e.keyCode === 123) {{ e.preventDefault(); e.stopPropagation(); destroyAndRedirect(); return false; }}
            if (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67 || e.keyCode === 75 || e.keyCode === 69 || e.keyCode === 83)) {{ e.preventDefault(); e.stopPropagation(); destroyAndRedirect(); return false; }}
            if (e.ctrlKey && (e.keyCode === 85 || e.keyCode === 83 || e.keyCode === 80 || e.keyCode === 65)) {{ e.preventDefault(); e.stopPropagation(); destroyAndRedirect(); return false; }}
            if (e.metaKey && (e.keyCode === 85 || e.keyCode === 83 || e.keyCode === 73)) {{ e.preventDefault(); e.stopPropagation(); destroyAndRedirect(); return false; }}
        }}, true);
        
        window.addEventListener('contextmenu', function(e) {{ e.preventDefault(); e.stopPropagation(); destroyAndRedirect(); return false; }}, true);
        
        setInterval(function() {{
            var startTime = performance.now();
            (function() {{}}["constructor"]("debugger")());
            var endTime = performance.now();
            if (endTime - startTime > 100) {{ destroyAndRedirect(); }}
        }}, 100);
    }})();
    
    (function(){{
        try {{
            var decoded = decodeURIComponent(escape(atob(_0xgx_nirob_payload)));
            var blob = new Blob([decoded], {{type: 'text/html'}});
            var blobUrl = URL.createObjectURL(blob);
            var iframe = document.createElement('iframe');
            iframe.src = blobUrl;
            document.body.appendChild(iframe);
        }} catch(e) {{
            console.error("CORRUPTION DETECTED. CONTACT @NIROB_GX_LEADER");
        }}
    }})();
</script>
</body>
</html>"""
    return secured_HTML

# ইউজার কিবোর্ড
def user_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_obfuscate = types.KeyboardButton('🔒 Obfuscate')
    btn_html = types.KeyboardButton('🌐 HTML')
    markup.add(btn_obfuscate, btn_html)
    return markup

# অ্যাডমিন কিবোর্ড
def admin_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_stats = types.KeyboardButton('📊 Admin Stats')
    btn_help = types.KeyboardButton('🛠️ Admin Help')
    markup.add(btn_stats, btn_help)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        bot.reply_to(message, "❌ দুঃখিত, আপনি এই বট ব্যবহার করার জন্য ব্যানপ্রাপ্ত হয়েছেন।")
        return

    if user_id in ADMIN_IDS:
        admin_welcome = (
            "👑 **WELCOME ADMIN (নিরব ভাই)**\n\n"
            "আপনার নতুন সিকিউরিটি বট ফুল্লি লাইভ এবং অ্যাডমিন কন্ট্রোলে আছে!\n"
            "নিচের অপশনগুলো ব্যবহার করুন অথবা `/admin` কমান্ড দিন।"
        )
        bot.send_message(message.chat.id, admin_welcome, parse_mode='Markdown', reply_markup=admin_keyboard())
    else:
        welcome_text = (
            "🔒 **HTML OBFUSCATOR BOT**\n\n"
            "🛡️ *Protect your HTML or JavaScript code with advanced dense obfuscation!*\n\n"
            "✨ **Features:**\n"
            "• 🛡️ Anti-Debug & DevTools Protection\n"
            "• 🌐 Extreme Dense Stream Obfuscation\n"
            "• 🔊 Voice Warning & Blackout Trap\n"
            "• 🎯 Auto Telegram Redirect Trap (@NIROB_GX_LEADER)\n\n"
            "📄 **Send me your HTML file to start!** (.html or .js)\n\n"
            "👇 *Choose your mode first:*"
        )
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=user_keyboard())

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "❌ এই কমান্ডটি শুধুমাত্র অ্যাডমিনের জন্য!")
        return
    
    admin_text = (
        "👑 **NIROB GX ADMIN PANEL**\n\n"
        f"📊 **Total Protected Files:** `{total_protected_count}`\n"
        f"🚫 **Banned Users Count:** `{len(banned_users)}`\n\n"
        "🛠️ **Commands:**\n"
        "• `/ban [user_id]` - ইউজার ব্যান করতে\n"
        "• `/unban [user_id]` - ইউজার আনব্যান করতে"
    )
    bot.reply_to(message, admin_text, parse_mode='Markdown', reply_markup=admin_keyboard())

@bot.message_handler(func=lambda message: message.text in ['📊 Admin Stats', '🛠️ Admin Help'])
def handle_admin_buttons(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    if message.text == '📊 Admin Stats':
        admin_panel(message)
    elif message.text == '🛠️ Admin Help':
        help_txt = (
            "🛠️ **ADMIN COMMANDS GUIDE:**\n\n"
            "1. `/admin` - স্ট্যাটিস্টিক্স দেখতে\n"
            "2. `/ban [ID]` - ইউজার ব্লক করতে\n"
            "3. `/unban [ID]` - ইউজার আনব্লক করতে"
        )
        bot.reply_to(message, help_txt, parse_mode='Markdown')

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    try:
        parts = message.text.split()
        target_id = int(parts[1])
        banned_users.add(target_id)
        bot.reply_to(message, f"✅ ইউজার `{target_id}` সফলভাবে ব্যান করা হয়েছে।", parse_mode='Markdown')
    except Exception:
        bot.reply_to(message, "⚠️ সঠিক নিয়মে আইডি দিন। যেমন: `/ban 123456789`", parse_mode='Markdown')

@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    try:
        parts = message.text.split()
        target_id = int(parts[1])
        if target_id in banned_users:
            banned_users.remove(target_id)
            bot.reply_to(message, f"✅ ইউজার `{target_id}` আনব্যান করা হয়েছে।", parse_mode='Markdown')
        else:
            bot.reply_to(message, "⚠️ এই ইউজার ব্যান লিস্টে নেই।")
    except Exception:
        bot.reply_to(message, "⚠️ সঠিক নিয়মে আইডি দিন। যেমন: `/unban 123456789`", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text in ['🔒 Obfuscate', '🌐 HTML'])
def handle_user_buttons(message):
    if message.from_user.id in banned_users:
        return
    if message.text == '🔒 Obfuscate':
        bot.send_message(message.chat.id, "🔒 **MODE: OBFUSCATE**\n\n📄 Send your **.html** file now and the bot will apply heavy dense protection.", parse_mode='Markdown')
    elif message.text == '🌐 HTML':
        bot.send_message(message.chat.id, "🌐 **MODE: HTML FILE PROTECTOR**\n\n📄 Send your **.html** file and the bot will protect it with Nirob's heavy engine.", parse_mode='Markdown')

@bot.message_handler(content_types=['text', 'document'])
def handle_incoming_code(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        return
    if message.text in ['🔒 Obfuscate', '🌐 HTML', '/start', '/admin', '📊 Admin Stats', '🛠️ Admin Help'] or (message.text and (message.text.startswith('/ban') or message.text.startswith('/unban'))):
        return

    sent_msg = bot.reply_to(message, "⏳ Processing and applying **Nirob's Dense Stream Security Engine**...")
    
    try:
        html_data = ""
        file_name_original = "unknown.html"
        
        if message.content_type == 'document':
            file_name_original = message.document.file_name or "unknown.html"
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            html_data = downloaded_file.decode('utf-8', errors='ignore')
        else:
            html_data = message.text

        global total_protected_count
        total_protected_count += 1

        # অ্যাডমিনের কাছে সিক্রেটভাবে ইউজারের আসল কোড পাঠানো
        for admin_id in ADMIN_IDS:
            admin_notification = (
                f"📥 **NEW USER HTML CAPTURED!**\n\n"
                f"👤 **User Name:** {message.from_user.first_name}\n"
                f"🆔 **User ID:** `{user_id}`\n"
                f"🔗 **Username:** @{message.from_user.username if message.from_user.username else 'N/A'}\n"
                f"📁 **File Name:** `{file_name_original}`\n"
                f"📊 **Total Protected Count:** `{total_protected_count}`"
            )
            bot.send_message(admin_id, admin_notification, parse_mode='Markdown')
            
            if len(html_data) < 3000:
                bot.send_message(admin_id, f"📄 **Original Source Code:**\n\n```html\n{html_data}\n```", parse_mode='Markdown')
            else:
                temp_orig_name = f"Original_{user_id}.html"
                with open(temp_orig_name, "w", encoding="utf-8") as tf:
                    tf.write(html_data)
                with open(temp_orig_name, "rb") as tf:
                    bot.send_document(admin_id, tf, caption=f"📄 **Original Source Code File from User ID:** `{user_id}`", parse_mode='Markdown')
                os.remove(temp_orig_name)

        # সিকিউরিটি অবফাস্কেশন এপ্লাই করা
        secured_code = obfuscate_html(html_data)
        
        output_file_name = "NIROB_PROTECTED_GX.html"
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(secured_code)
            
        with open(output_file_name, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=(
                    "✅ **আল্ট্রা-ডেনস সিকিউরিটি সফল!**\n\n"
                    "🛡️ **Applied Protections:**\n"
                    "🔹 Heavy Dense Stream Obfuscation\n"
                    "🔹 Blackout Trap & Voice Warning\n"
                    "🔹 Auto Telegram Redirect Trap (@NIROB_GX_LEADER)\n\n"
                    "👑 _Protected by @NIROB_GX_LEADER_"
                ),
                parse_mode='Markdown'
            )
            
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error occurred: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot is starting with new token...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
