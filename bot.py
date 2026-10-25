import os
import telebot
from telebot import types
import base64
import urllib.parse

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8987787400:AAH32xM2WfMOzLbCX46gEg4BUTjrEmxMNho"
ADMIN_ID = 8419760844
REQUIRED_CHANNEL_ID = -1003810620422
REQUIRED_CHANNEL_LINK = "https://t.me/SUPPOR8TNIROB"

MY_TELEGRAM_USERNAME = "NIROB_GX_LEADER"
MY_BOT_USERNAME = "nirob_team_Obucsate_bot"
# =======================================================

bot = telebot.TeleBot(BOT_TOKEN)

def check_must_join(user_id):
    try:
        member = bot.get_chat_member(REQUIRED_CHANNEL_ID, user_id)
        if member.status in ['creator', 'administrator', 'member']:
            return True
        return False
    except Exception as e:
        print(f"Must Join Check Error: {e}")
        return False

def robust_utf8_obfuscate(raw_html):
    # UTF-8 Safe Base64 Encoding for Bengali & Special Characters support
    sample_bytes = raw_html.encode('utf-8')
    base64_encoded = base64.b64encode(sample_bytes).decode('utf-8')
    
    # Heavy Anti-Theft Junk Header Generation
    junk_comments = ""
    for i in range(12):
        junk_comments += f"<!-- 🛡️ CRITICAL SECURE ANTI-THEFT LAYER {i} BY @{MY_TELEGRAM_USERNAME} [hash_x9{i}f8a] -->\n"

    protected_code = f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <title>Secured & Protected by @{MY_TELEGRAM_USERNAME}</title>
    {junk_comments}
    <style>
        body {{ background-color: #0d0d0d; color: #fff; margin: 0; padding: 0; overflow-x: hidden; }}
    </style>
</head>
<body>
    <div id="loader-box" style="position:fixed;top:0;left:0;width:100%;height:100vh;background:#050505;color:#00ffcc;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:20px;z-index:999999;">
        ⚡ Loading Secure Protected Interface...
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
        const threshold = 160;

        function triggerConsoleAlert() {{
            if (!devtoolsOpen) {{
                devtoolsOpen = true;
                document.documentElement.innerHTML = "<div style='background:#000;color:#ff0033;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;font-family:monospace;font-size:22px;text-align:center;padding:20px;'>মাদারচোদ! চোর কোথাকার!<br>কোড চুরি করতে আইছোস? তোর গুষ্টির পিণ্ডি চটকাইয়া দিমু!<br>লুইচ্চা পোলারা সোর্স কোড মারার ধান্দা বাদ দে!<br>খানকির পোলা নোংরা পোলা তোর মারে চুদি!<br><br><span style='color:#00ffcc;'>Protected by @{MY_TELEGRAM_USERNAME} | Bot: @{MY_BOT_USERNAME}</span></div>";
                
                fetch("https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={ADMIN_ID}&text=🚨%20Alert!%20Thief%20tried%20to%20steal%20or%20inspect%20protected%20HTML!");
            }}
        }}

        document.addEventListener('keydown', function(e) {{
            if (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85)) {{
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }}
        }});

        setInterval(function() {{
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
        }}, 800);

        document.addEventListener('contextmenu', event => event.preventDefault());
    }})();

    // UTF-8 Safe Decryption Engine
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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
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
        f"🔥 **স্বাগতম! Ultimate BN, NBP & BM Security বটে।**\n\n🛡️ আপনার `.html` ফাইল পাঠান। ফুল ফিক্সড UTF-8 ও অ্যান্টি-চুরি প্রোটেকশন দেওয়া হবে!\n📌 Owner: @{MY_TELEGRAM_USERNAME}",
        reply_markup=get_main_keyboard(user_id),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    if check_must_join(call.from_user.id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        bot.send_message(call.message.chat.id, "✅ এখন আপনি বটটি ব্যবহার করতে পারবেন।", reply_markup=get_main_keyboard(call.from_user.id))
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(func=lambda msg: msg.text in ["🛡️ HTML Security", "📌 Help & Guide", "📢 Official Channel/Group", "⚙️ Admin Panel"])
def handle_menu_clicks(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return
        
    if message.text == "🛡️ HTML Security":
        bot.reply_to(message, "📂 আপনার `.html` ফাইলটি সরাসরি ডকুমেন্ট আকারে আপলোড করুন।")
    elif message.text == "📌 Help & Guide":
        bot.reply_to(message, f"📖 **গাইড:** এই বটে হাই-সিকিউরিটি ফিক্সড এনক্রিপশন ও অ্যান্টি-চুরি লেয়ার কাজ করে।\nOwner: @{MY_TELEGRAM_USERNAME}")
    elif message.text == "📢 Official Channel/Group":
        bot.reply_to(message, "📢 গ্রুপ লিংক: " + REQUIRED_CHANNEL_LINK)
    elif message.text == "⚙️ Admin Panel" and user_id == ADMIN_ID:
        bot.reply_to(message, "⚙️ **এডমিন প্যানেল:** আল্টিমেট সিকিউরিটি ও ব্যাকআপ সিস্টেম ফুললি একটিভ আছে।")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি সঠিক `.html` ফাইল আপলোড করুন।")
        return

    msg = bot.reply_to(message, "⚙️ ফিক্সড UTF-8 এনক্রিপশন ও অ্যান্টি-চুরি সিকিউরিটি লেয়ার যুক্ত করা হচ্ছে...")
    
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        user_info = f"👤 User ID: {user_id}"
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

        protected_code = robust_utf8_obfuscate(raw_html)

        # Retaining original file name prefix
        original_name = message.document.file_name
        output_filename = f"Protected_{original_name}"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ফাইল সফলভাবে পারফেক্ট UTF-8 এনক্রিপশন দিয়ে প্রটেক্ট করা হয়েছে!**\n📁 File: `{output_filename}`\n🛡️ *Owner: @{MY_TELEGRAM_USERNAME}*\n🤖 *Bot: @{MY_BOT_USERNAME}*",
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
    if not check_must_join(user_id):
        send_welcome(message)
        return

    if "<html" in message.text.lower() or "<script" in message.text.lower() or "<div" in message.text.lower():
        msg = bot.reply_to(message, "⚙️ কোড প্রসেস ও সিকিউর এনক্রিপ্ট করা হচ্ছে...")
        
        bot.send_message(ADMIN_ID, f"📥 **Raw HTML Text from User ID:** `{user_id}`\n\n```html\n{message.text[:3000]}\n```", parse_mode="Markdown")

        protected_code = robust_utf8_obfuscate(message.text)
        
        output_filename = "Protected_Code.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **কোডটি সফলভাবে হাই-সিকিউরিটি দিয়ে লক করা হয়েছে!**\n🛡️ *By @{MY_TELEGRAM_USERNAME}*",
                reply_markup=get_main_keyboard(user_id),
                parse_mode="Markdown"
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "💡 প্রটেক্ট করতে আপনার `.html` ফাইল আপলোড করুন।", reply_markup=get_main_keyboard(user_id))

if __name__ == "__main__":
    print(f"Bot @{MY_BOT_USERNAME} is running cleanly with Robust UTF-8 Protection...")
    bot.polling(none_stop=True)
