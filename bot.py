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

# এখানে parse_mode সরিয়ে নেওয়া হয়েছে যাতে কোনো মার্কডাউন এরর বা ক্রাশ না করে
bot = telebot.TeleBot(TOKEN)

banned_users = set()
total_protected_count = 0

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
        "⚠️ অ্যাক্সেস ব্লকড!\n\n"
        "এই বট ব্যবহার করতে হলে আপনাকে অবশ্যই আমাদের অফিশিয়াল সাপোর্ট গ্রুপে জয়েন থাকতে হবে!\n\n"
        "👉 নিচের বাটন থেকে সাপোর্ট গ্রুপে জয়েন করে 'Check Membership' বাটনে ক্লিক করুন।",
        reply_markup=markup
    )

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
===================================
-->
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROTECTED BY NIROB | @NIROB_GX_LEADER</title>
    <style>
        html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; background:#000; }}
        iframe {{ width:100%; height:100%; border:none; }}
    </style>
</head>
<body oncontextmenu="return false;" onkeydown="return false;">
<script>
    {dense_junk_stream}
    var _0xgx_nirob_payload = "{encoded_payload}";
    var isDestroyed = false;
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("নিরব আব্বা আমার ভুল হয়ে গেছে! আমাকে মাফ করে দেন...");
    
    function triggerVoiceWarning() {{
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var msgText = "ওই শয়তানের বাচ্চা! তোর এত্ত বড় সাহস তুই নিরব আব্বার কোডে হাত দেস? ফালতু কোড চুরি করার চিন্তা বাদ দে!";
            var speech = new SpeechSynthesisUtterance(msgText);
            speech.lang = 'bn-BD';
            window.speechSynthesis.speak(speech);
        }}
    }}
    
    function destroyAndRedirect() {{
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#000;color:#ff0055;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;"><h1>⚠️ ACCESS DENIED BY NIROB ABBA!</h1><a href="' + telegramTrapLink + '" style="background:#00ffcc;color:#000;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;">👉 নিরব আব্বার টেলিগ্রামে যান</a></div>';
        setTimeout(function() { window.location.href = telegramTrapLink; }, 1500);
    }}
    
    (function() {{
        window.addEventListener('keydown', function(e) {{
            if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey)) {{ destroyAndRedirect(); return false; }}
        }}, true);
        window.addEventListener('contextmenu', function(e) {{ destroyAndRedirect(); return false; }}, true);
    }})();
    
    (function(){{
        try {{
            var decoded = decodeURIComponent(escape(atob(_0xgx_nirob_payload)));
            var blob = new Blob([decoded], {{type: 'text/html'}});
            var blobUrl = URL.createObjectURL(blob);
            var iframe = document.createElement('iframe');
            iframe.src = blobUrl;
            document.body.appendChild(iframe);
        }} catch(e) {{}}
    }})();
</script>
</body>
</html>"""
    return secured_HTML

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
        bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত হয়েছেন। যোগাযোগ করুন: @NIROB_GX_LEADER")
        return

    if not check_user_membership(user_id):
        send_force_join_msg(message.chat.id)
        return

    if user_id in ADMIN_IDS:
        bot.send_message(message.chat.id, "👑 WELCOME ADMIN (নিরব ভাই)\nবট ফুল্লি লাইভ আছে!", reply_markup=admin_keyboard())
    else:
        bot.send_message(message.chat.id, "🔒 HTML OBFUSCATOR BOT\n\n📄 Send your .html file to start protection!", reply_markup=user_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    user_id = call.from_user.id
    if check_user_membership(user_id):
        bot.answer_callback_query(call.id, "✅ কনফার্ম হয়েছে!")
        bot.send_message(call.message.chat.id, "🎉 অভিনন্দন! এখন বট ব্যবহার করতে পারেন। /start দিন।", reply_markup=user_keyboard())
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(commands=['admin', 'unban'])
def handle_admin_commands(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text
    if text.startswith('/admin'):
        bot.reply_to(message, f"👑 ADMIN PANEL\n📊 Protected: {total_protected_count}\n🚫 Banned: {len(banned_users)}")
    elif text.startswith('/unban'):
        try:
            target_id = int(text.split()[1])
            if target_id in banned_users:
                banned_users.remove(target_id)
                bot.reply_to(message, f"✅ ইউজার {target_id} আনব্যান করা হয়েছে।")
            else:
                bot.reply_to(message, "⚠️ ইউজার ব্যান লিস্টে নেই।")
        except:
            bot.reply_to(message, "⚠️ সঠিক নিয়ম: /unban [ID]")

@bot.message_handler(content_types=['text', 'document'])
def handle_incoming(message):
    user_id = message.from_user.id
    text = message.text if message.text else ""

    if user_id in ADMIN_IDS and text.isdigit():
        target_id = int(text)
        banned_users.add(target_id)
        bot.reply_to(message, f"✅ ইউজার আইডি {target_id} ব্যান করা হয়েছে!")
        return

    if user_id in banned_users or not check_user_membership(user_id):
        if user_id in banned_users:
            bot.reply_to(message, "❌ আপনি ব্যানপ্রাপ্ত।")
        else:
            send_force_join_msg(message.chat.id)
        return

    if text in ['/start', '📊 Admin Stats', '🛠️ Admin Help']:
        if text == '🛠️ Admin Help':
            bot.reply_to(message, "🛠️ ইউজার ব্যান করতে শুধু তার আইডি (সংখ্যা) পাঠান। আনব্যান করতে /unban [ID] দিন।")
        return

    if text in ['🔒 Obfuscate', '🌐 HTML']:
        bot.send_message(message.chat.id, "📄 আপনার .html ফাইল বা কোডটি পাঠান!")
        return

    bot.reply_to(message, "⏳ Processing and applying Nirob's Dense Stream Security Engine...")
    
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

        global total_protected_count
        total_protected_count += 1

        for admin_id in ADMIN_IDS:
            bot.send_message(admin_id, f"📥 New file captured from ID: {user_id} | File: {file_name_original}")

        secured_code = obfuscate_html(html_data)
        output_file_name = "NIROB_PROTECTED_GX.html"
        
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(secured_code)
            
        with open(output_file_name, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption="✅ আল্ট্রা-ডেনস সিকিউরিটি সফল!\n\n👑 Protected by @NIROB_GX_LEADER"
            )
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot started...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
