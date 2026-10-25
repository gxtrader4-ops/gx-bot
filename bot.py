import os
import json
import telebot
from telebot import types
import base64
import urllib.parse
from datetime import datetime
from flask import Flask
import threading
import time

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8456818299:AAHuasHwRQHhKDLhey-AnQBoXjEAggXvyGI"
ADMIN_ID = 8419760844
REQUIRED_CHANNEL_ID = "@SUPPOR8TNIROB"  # আপনার নিজস্ব গ্রুপের ইউজারনেম বা আইডি
REQUIRED_CHANNEL_LINK = "https://t.me/SUPPOR8TNIROB"  # আপনার নিজস্ব গ্রুপের রিয়েল লিংক

MY_TELEGRAM_USERNAME = "NIROB_GX_LEADER"
MY_BOT_USERNAME = "nirob_gxteam_Obucsate_bot"
# =======================================================

bot = telebot.TeleBot(BOT_TOKEN)

DB_FILE = "bot_database.json"

def load_db():
    # সবসময় আপনার নিজস্ব লিংক ফিক্সড রাখার জন্য এখানে ডিফল্ট ভ্যালু হিসেবে আপনার লিংক দেওয়া হয়েছে
    default_data = {"banned": [], "users": [], "channel_link": REQUIRED_CHANNEL_LINK, "channel_id": REQUIRED_CHANNEL_ID}
    if not os.path.exists(DB_FILE):
        return default_data
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f.read() and f or '{}')
            # যদি ডাটাবেজে অন্য কোনো লিংক থাকে, জোরপূর্বক আপনার লিংক বসিয়ে দিবে
            if not data.get("channel_link") or "TucosProfit" in data.get("channel_link", ""):
                data["channel_link"] = REQUIRED_CHANNEL_LINK
                data["channel_id"] = REQUIRED_CHANNEL_ID
                save_db(data)
            return data
    except:
        return default_data

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Flask server for Render Port Binding
app = Flask('')

@app.route('/')
def home():
    return "Bot is active and running cleanly!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

def check_must_join(user_id):
    if user_id == ADMIN_ID:
        return True  # Admin always bypasses
    db = load_db()
    ch_id = db.get("channel_id", REQUIRED_CHANNEL_ID)
    try:
        member = bot.get_chat_member(ch_id, user_id)
        if member.status in ['creator', 'administrator', 'member']:
            return True
        return False
    except Exception as e:
        print(f"Must Join Check Error: {e}")
        return False

def get_main_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_sec = types.KeyboardButton("🛡️ HTML Security")
    btn_help = types.KeyboardButton("📌 Help & Guide")
    btn_channel = types.KeyboardButton("📢 Official Channel/Group")
    markup.add(btn_sec, btn_help, btn_channel)
    
    if user_id == ADMIN_ID:
        btn_admin = types.KeyboardButton("⚙️ Admin Panel")
        markup.add(btn_admin)
        
    return markup

def nirob_abba_level_cipher(raw_html):
    sample_bytes = raw_html.encode('utf-8')
    base64_encoded = base64.b64encode(sample_bytes).decode('utf-8')
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    header_box = f"""<!--
╔══════════════════════════════════════════════════════════════╗
║   🔒 NIROB ABBA-LEVEL ULTRA CIPHER V3.0 - UNBREAKABLE      ║
║══════════════════════════════════════════════════════════════║
║  Obfuscated By: @{MY_TELEGRAM_USERNAME}                                 ║
║  Telegram Bot: @{MY_BOT_USERNAME}                  ║
║  Timestamp: {current_time}                            ║
║  Security Hash: 99xA7B8Z10wYGv7pvpB2YP9B-ABBA-SECURE       ║
╚══════════════════════════════════════════════════════════════╝
-->"""

    protected_code = f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <title>Secured & Protected by @{MY_TELEGRAM_USERNAME}</title>
    {header_box}
    <style>
        body {{ background-color: #0d0d0d; color: #fff; margin: 0; padding: 0; overflow-x: hidden; }}
    </style>
</head>
<body>
    <div id="loader-box" style="position:fixed;top:0;left:0;width:100%;height:100vh;background:#050505;color:#00ffcc;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:20px;z-index:999999;">
        🔥 Loading Abba-Level Secured Interface...
    </div>

    <script>
    (function() {{
        try {{
            var ua = navigator.userAgent.toLowerCase();
            if (ua.includes("headless") || ua.includes("phantomjs") || ua.includes("selenium")) {{
                document.body.innerHTML = "";
                window.location.href = "about:blank";
            }}
        }} catch(e) {{}}

        let devtoolsOpen = false;
        let protectionActive = false;
        const threshold = 160;

        setTimeout(function() {{
            protectionActive = true;
        }}, 4000);

        function triggerConsoleAlert() {{
            if (protectionActive && !devtoolsOpen) {{
                devtoolsOpen = true;
                document.documentElement.innerHTML = "<div style='background:#000;color:#ff0033;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;font-family:monospace;font-size:22px;text-align:center;padding:20px;'>মাদারচোদ! চোর কোথাকার!<br>কোড চুরি করতে আইছোস? তোর গুষ্টির পিণ্ডি চটকাইয়া দিমু!<br>লুইচ্চা পোলারা সোর্স কোড মারার ধান্দা বাদ দে!<br>খানকির পোলা নোংরা পোলা তোর মারে চুদি!<br><br><span style='color:#00ffcc;'>Protected by @{MY_TELEGRAM_USERNAME} | Bot: @{MY_BOT_USERNAME}</span></div>";
                
                fetch("https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={ADMIN_ID}&text=🚨%20Alert!%20A%20thief%20tried%20to%20inspect/steal%20HTML%20and%20got%20busted!");
            }}
        }}

        document.addEventListener('keydown', function(e) {{
            if (protectionActive && (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85))) {{
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }}
        }});

        setInterval(function() {{
            if (!protectionActive) return;
            const widthThreshold = window.outerWidth - window.innerWidth > threshold;
            const heightThreshold = window.outerHeight - window.innerHeight > threshold;
            if (widthThreshold || heightThreshold) {{
                triggerConsoleAlert();
            }}
            
            var startTime = performance.now();
            debugger;
            var endTime = performance.now();
            if (endTime - startTime > 100) {{
                triggerConsoleAlert();
            }}
        }}, 1000);

        document.addEventListener('contextmenu', event => {{
            if (protectionActive) event.preventDefault();
        }});
    }})();

    window.addEventListener('DOMContentLoaded', (event) => {{
        try {{
            var b64Data = "{base64_encoded}";
            var binString = atob(b64Data);
            var bytes = Uint8Array.from(binString, (m) => m.codePointAt(0));
            var decodedHtml = new TextDecoder().decode(bytes);
            
            document.open();
            document.write(decodedHtml);
            document.close();
        }} catch(err) {{
            document.body.innerHTML = "<h1 style='color:red;text-align:center;margin-top:20vh;'>❌ Security Decryption Error! Protected by @{MY_TELEGRAM_USERNAME}</h1>";
        }}
    }});
    </script>
    <noscript><h1 style="color:red;text-align:center;">JavaScript is required to view this content! Protected by @{MY_TELEGRAM_USERNAME}</h1></noscript>
</body>
</html>
"""
    return protected_code

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    db = load_db()

    if user_id in db["banned"]:
        bot.reply_to(message, "❌ দুঃখিত, আপনাকে বট থেকে ব্যান করা হয়েছে।")
        return

    if user_id not in db["users"]:
        db["users"].append(user_id)
        save_db(db)

    if not check_must_join(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Join Group 📢", url=REQUIRED_CHANNEL_LINK)
        check_btn = types.InlineKeyboardButton("Check Join ✅", callback_data="check_join")
        markup.add(btn)
        markup.add(check_btn)
        
        bot.reply_to(
            message, 
            "⚠️ **অ্যাক্সেস রেস্ট্রিক্টেড!**\n\nবটটি ব্যবহার করতে হলে আমাদের গ্রুপে জয়েন করতে হবে:\n" + REQUIRED_CHANNEL_LINK, 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        return

    bot.reply_to(
        message, 
        f"🔥 **স্বাগতম! আব্বা লেভেলের আল্টিমেট HTML Security বটে।**\n\n🛡️ আপনার `.html` ফাইল পাঠান। ফুল ফিক্সড আল্ট্রা এনক্রিপশন ও অ্যান্টি-চুরি প্রোটেকশন দেওয়া হবে!\n📌 Owner: @{MY_TELEGRAM_USERNAME}",
        reply_markup=get_main_keyboard(user_id),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    user_id = call.from_user.id
    if check_must_join(user_id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(call.message.chat.id, "✅ এখন আপনি বটটি ব্যবহার করতে পারবেন।", reply_markup=get_main_keyboard(user_id))
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(func=lambda msg: msg.text in ["🛡️ HTML Security", "📌 Help & Guide", "📢 Official Channel/Group", "⚙️ Admin Panel"])
def handle_menu_clicks(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return
        
    if message.text == "🛡️ HTML Security":
        bot.reply_to(message, "📂 আপনার `.html` ফাইলটি সরাসরি ডকুমেন্ট আকারে আপলোড করুন অথবা কোড পেস্ট করুন।", reply_markup=get_main_keyboard(user_id))
    elif message.text == "📌 Help & Guide":
        bot.reply_to(message, f"📖 **গাইড:** এই বটে আব্বা লেভেলের হাই-সিকিউরিটি এনক্রিপশন ও অ্যান্টি-চুরি লেয়ার কাজ করে।\nOwner: @{MY_TELEGRAM_USERNAME}", reply_markup=get_main_keyboard(user_id))
    elif message.text == "📢 Official Channel/Group":
        bot.reply_to(message, "📢 গ্রুপ লিংক: " + REQUIRED_CHANNEL_LINK, reply_markup=get_main_keyboard(user_id))
    elif message.text == "⚙️ Admin Panel" and user_id == ADMIN_ID:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast"),
            types.InlineKeyboardButton("🔗 Change Link", callback_data="admin_set_link"),
            types.InlineKeyboardButton("🚫 Ban User", callback_data="admin_ban"),
            types.InlineKeyboardButton("✅ Unban User", callback_data="admin_unban")
        )
        bot.reply_to(message, "⚙️ **এডমিন কন্ট্রোল প্যানেল:** নিচে থেকে অপশন সিলেক্ট করুন:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_callbacks(call):
    if call.from_user.id != ADMIN_ID:
        return
    
    if call.data == "admin_broadcast":
        msg = bot.send_message(call.message.chat.id, "📢 ব্রডকাস্ট করার জন্য মেসেজটি পাঠান:")
        bot.register_next_step_handler(msg, process_broadcast)
    elif call.data == "admin_set_link":
        msg = bot.send_message(call.message.chat.id, "🔗 নতুন গ্রুপ লিংক বা চ্যানেল আইডি পাঠান (যেমন: @channel_username বা -100...):")
        bot.register_next_step_handler(msg, process_set_link)
    elif call.data == "admin_ban":
        msg = bot.send_message(call.message.chat.id, "🚫 ব্যান করার জন্য ইউজারের Telegram User ID পাঠান:")
        bot.register_next_step_handler(msg, process_ban)
    elif call.data == "admin_unban":
        msg = bot.send_message(call.message.chat.id, "✅ আনব্যান করার জন্য ইউজারের Telegram User ID পাঠান:")
        bot.register_next_step_handler(msg, process_unban)

def process_broadcast(message):
    if message.from_user.id != ADMIN_ID: return
    db = load_db()
    count = 0
    for uid in db["users"]:
        try:
            bot.send_message(uid, f"📢 **Announcement:**\n\n{message.text}", parse_mode="Markdown")
            count += 1
        except:
            pass
    bot.reply_to(message, f"✅ সফলভাবে {count} জন ইউজারের কাছে মেসেজ পাঠানো হয়েছে।")

def process_set_link(message):
    if message.from_user.id != ADMIN_ID: return
    db = load_db()
    new_input = message.text.strip()
    db["channel_link"] = new_input if new_input.startswith("http") else f"https://t.me/{new_input.replace('@','')}"
    db["channel_id"] = f"@{new_input.split('/')[-1]}" if "t.me/" in new_input else new_input
    save_db(db)
    bot.reply_to(message, f"✅ সফলভাবে গ্রুপ লিংক আপডেট করা হয়েছে: `{db['channel_link']}`", parse_mode="Markdown")

def process_ban(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        uid = int(message.text.strip())
        db = load_db()
        if uid not in db["banned"]:
            db["banned"].append(uid)
            save_db(db)
        bot.reply_to(message, f"✅ User ID `{uid}` সফলভাবে ব্যান করা হয়েছে।", parse_mode="Markdown")
    except:
        bot.reply_to(message, "❌ সঠিক ইউজার আইডি দিন।")

def process_unban(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        uid = int(message.text.strip())
        db = load_db()
        if uid in db["banned"]:
            db["banned"].remove(uid)
            save_db(db)
        bot.reply_to(message, f"✅ User ID `{uid}` সফলভাবে আনব্যান করা হয়েছে।", parse_mode="Markdown")
    except:
        bot.reply_to(message, "❌ সঠিক ইউজার আইডি দিন।")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি সঠিক `.html` ফাইল আপলোড করুন।", reply_markup=get_main_keyboard(user_id))
        return

    msg = bot.reply_to(message, "⚙️ আব্বা লেভেলের আল্ট্রা এনক্রিপশন ও অ্যান্টি-চুরি সিকিউরিটি লেয়ার যুক্ত করা হচ্ছে...")
    
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        user_info = f"👤 User ID: {user_id} | @{message.from_user.username if message.from_user.username else 'No Username'}"
        backup_filename = f"original_{message.document.file_name}"
        with open(backup_filename, "w", encoding="utf-8") as orig_f:
            orig_f.write(raw_html)
        
        with open(backup_filename, "rb") as orig_f:
            bot.send_document(
                ADMIN_ID, 
                orig_f, 
                caption=f"📥 **New Raw HTML Backup!**\n{user_info}\n📁 File: {message.document.file_name}",
                parse_mode="Markdown"
            )
        os.remove(backup_filename)

        protected_code = nirob_abba_level_cipher(raw_html)

        original_name = message.document.file_name
        output_filename = f"Protected_{original_name}"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ফাইল সফলভাবে আব্বা লেভেলের এনক্রিপশন দিয়ে প্রটেক্ট করা হয়েছে!**\n📁 File: `{output_filename}`\n🛡️ *Owner: @{MY_TELEGRAM_USERNAME}*\n🤖 *Bot: @{MY_BOT_USERNAME}*",
                reply_markup=get_main_keyboard(user_id),
                parse_mode="Markdown"
            )
        
        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ এরর ঘটেছে: {str(e)}", message.chat.id, msg.message_id)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return

    if "<html" in message.text.lower() or "<script" in message.text.lower() or "<div" in message.text.lower():
        msg = bot.reply_to(message, "⚙️ কোড প্রসেস ও সিকিউর এনক্রিপ্ট করা হচ্ছে...")
        
        user_info = f"👤 User ID: {user_id} | @{message.from_user.username if message.from_user.username else 'No Username'}"
        bot.send_message(ADMIN_ID, f"📥 **Raw HTML Text Backup!**\n{user_info}\n\n```html\n{message.text[:3000]}\n```", parse_mode="Markdown")

        protected_code = nirob_abba_level_cipher(message.text)
        
        output_filename = "Protected_Code.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **কোডটি সফলভাবে আব্বা লেভেল সিকিউরিটি দিয়ে লক করা হয়েছে!**\n🛡️ *By @{MY_TELEGRAM_USERNAME}*",
                reply_markup=get_main_keyboard(user_id),
                parse_mode="Markdown"
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "💡 প্রটেক্ট করতে আপনার `.html` ফাইল ডকুমেন্ট আকারে আপলোড করুন।", reply_markup=get_main_keyboard(user_id))

if __name__ == "__main__":
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()
    
    print(f"Bot @{MY_BOT_USERNAME} is running cleanly with Abba-Level Ultra Protection & Flask Server...")
    
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Polling Error: {e}")
            time.sleep(3)
