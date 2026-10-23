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

def inject_safe_protection(html_content):
    """
    নিরাপদ এবং শক্তিশালী প্রটেকশন লেয়ার:
    - আসল এইচটিএমএল, সিএসএস, বা জাভাস্ক্রিপ্ট ভাঙবে না।
    - কনসোল/ইন্সপেক্ট (F12) ব্লক করবে এবং কোড উধাও করে ইনবক্সে অ্যালার্ট পাঠাবে।
    - ফাইলের অরিজিনাল টাইটেল বা ডিজাইন পরিবর্তন করবে না।
    """
    safe_script = """
    <script>
    (function() {
        // ফেইক বা হেডলেস ব্রাউজার ডিটেকশন
        try {
            var ua = navigator.userAgent.toLowerCase();
            if (ua.includes("headless") || ua.includes("phantomjs") || ua.includes("selenium")) {
                document.body.innerHTML = "";
                window.location.href = "about:blank";
            }
        } catch(e) {}

        let devtoolsOpen = false;
        const threshold = 160;

        function triggerConsoleAlert() {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                document.documentElement.innerHTML = "<div style='background:#000;color:#ff3333;height:100vh;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:22px;text-align:center;padding:20px;'>ACCESS BLOCKED!<br>Developer Console Detected.<br>Protected Content Terminated.</div>";
                
                // ইনবক্সে অ্যালার্ট পাঠানোর রিকোয়েস্ট
                fetch("https://api.telegram.org/bot8987787400:AAHyqVQf45234LpFEnmgfJ-AahfG_We4-8A/sendMessage?chat_id=8419760844&text=🚨%20Alert!%20Someone%20tried%20to%20inspect%20or%20open%20console%20on%20the%20protected%20file!");
            }
        }

        // শর্টকাট কি (F12, Ctrl+Shift+I ইত্যাদি) ব্লক করা
        document.addEventListener('keydown', function(e) {
            if (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85)) {
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }
        });

        // ডিবাগিং ও উইন্ডো সাইজ ট্র্যাপ
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
        }, 600);

        // রাইট ক্লিক ডিজাবল
        document.addEventListener('contextmenu', event => event.preventDefault());
    })();
    </script>
    """
    
    if "</head>" in html_content:
        return html_content.replace("</head>", safe_script + "\n</head>")
    elif "<body>" in html_content:
        return html_content.replace("<body>", "<body>\n" + safe_script)
    else:
        return safe_script + html_content

def protect_html_file(html_code):
    # কোডের গঠন ও স্টাইল অক্ষুণ্ণ রেখে এনক্রিপ্ট করার প্রক্রিয়া
    protected_html = inject_safe_protection(html_code)
    escaped_code = "".join([f"%{ord(c):02X}" for c in protected_html])
    
    # অরিজিনাল ফাইল স্ট্রাকচার এবং টাইটেল ঠিক রেখে পেআলোড তৈরি
    final_payload = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
document.write(unescape("{escaped_code}"));
</script>
</head>
<body>
<noscript>JavaScript is required to run this application.</noscript>
</body>
</html>"""
    return final_payload

# মেনু বাটন তৈরি করার ফাংশন
def get_main_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_sec = types.KeyboardButton("🛡️ HTML Security")
    btn_help = types.KeyboardButton("📌 Help & Guide")
    btn_channel = types.KeyboardButton("📢 Official Channel/Group")
    markup.add(btn_sec, btn_help, btn_channel)
    
    # এডমিনের জন্য এক্সট্রা বাটন
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
            f"⚠️ **অ্যাক্সেস রেস্ট্রিক্টেড!**\n\nবটটি ব্যবহার করতে হলে আমাদের অফিশিয়াল গ্রুপে জয়েন করতে হবে:\n{REQUIRED_CHANNEL_LINK}", 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        return

    bot.reply_to(
        message, 
        f"🔥 **স্বাগতম! এইচটিএমএল সিকিউরিটি ও প্রোটেকশন বটে।**\n\n"
        "🛡️ নিচের বাটন ব্যবহার করে অথবা সরাসরি আপনার `.html` ফাইল/কোড পাঠিয়ে আপনার প্রজেক্ট প্রটেক্ট করে নিন। কোনো ডিজাইন বা কোড নষ্ট হবে না!",
        reply_markup=get_main_keyboard(user_id),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    if check_must_join(call.from_user.id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        bot.send_message(call.message.chat.id, "✅ এখন আপনি বটটি ফুললি ব্যবহার করতে পারবেন।", reply_markup=get_main_keyboard(call.from_user.id))
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(func=lambda msg: msg.text in ["🛡️ HTML Security", "📌 Help & Guide", "📢 Official Channel/Group", "⚙️ Admin Panel"])
def handle_menu_clicks(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return
        
    if message.text == "🛡️ HTML Security":
        bot.reply_to(message, "📂 আপনার প্রটেক্ট করার জন্য কাঙ্ক্ষিত `.html` ফাইলটি সরাসরি ডকুমেন্ট আকারে আপলোড করুন অথবা কোড পেস্ট করুন।")
    elif message.text == "📌 Help & Guide":
        bot.reply_to(message, "📖 **গাইড:** এই বট আপনার এইচটিএমএল ফাইলের ডিজাইন ও স্টাইল ঠিক রেখে ক্ষতিকর ডিকোডার ও কনসোল ইন্সপেক্ট ব্লক করে। ফাইল আপলোড করলেই প্রটেক্টেড ফাইল পেয়ে যাবেন।")
    elif message.text == "📢 Official Channel/Group":
        bot.reply_to(message, f"📢 আমাদের অফিশিয়াল গ্রুপে যুক্ত থাকুন: {REQUIRED_CHANNEL_LINK}")
    elif message.text == "⚙️ Admin Panel" and user_id == ADMIN_ID:
        bot.reply_to(message, "⚙️ **এডমিন প্যানেল:** বট সম্পূর্ণ সচল আছে। নতুন টোকেন আপডেট করা হয়েছে।")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি সঠিক `.html` ফাইল আপলোড করুন।")
        return

    msg = bot.reply_to(message, "⚙️ ফাইলটির ডিজাইন ও অরিজিনাল স্ট্রাকচার অক্ষুণ্ণ রেখে সিকিউরিটি এবং প্রটেকশন লেয়ার যুক্ত করা হচ্ছে...")
    
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        protected_code = protect_html_file(raw_html)

        output_filename = f"Protected_{message.document.file_name}"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption="✅ **ফাইল সফলভাবে প্রটেক্ট করা হয়েছে!**\n🛡️ *স্টাইল, ডিজাইন এবং অরিজিনাল ফাইল ঠিক রাখা হয়েছে।*",
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
        msg = bot.reply_to(message, "⚙️ কোড প্রসেস ও সিকিউর করা হচ্ছে...")
        protected_code = protect_html_file(message.text)
        
        output_filename = "Protected_Code.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption="✅ **আপনার কোডটি সফলভাবে সিকিউর করা হয়েছে!**",
                reply_markup=get_main_keyboard(user_id),
                parse_mode="Markdown"
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "💡 প্রটেক্ট করতে আপনার `.html` ফাইল আপলোড করুন অথবা নিচের বাটনগুলো ব্যবহার করুন।", reply_markup=get_main_keyboard(user_id))

if __name__ == "__main__":
    print("Bot is running with updated token and clean protection logic...")
    bot.infinity_polling()
