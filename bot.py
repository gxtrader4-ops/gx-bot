import os
import telebot
from telebot import types

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8989938530:AAFhsY_5jC2_YF3d0QHki4uAI87gcRzUFvY"
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

def inject_elite_protection(html_content, target_user_id):
    # JavaScript অংশ আলাদা রেখে পাইথন সিনট্যাক্স এরর মুক্ত করা হয়েছে
    elite_script = """
    <!--==================================================
    🔥 UNBREAKABLE ELITE ANTI-DECODE BY NIROB GX 🔥
    --------------------------------------------------
    Status: MAXIMUM ANTI-DECODER SHIELD ACTIVE 🛑
    ==================================================-->
    <script>
    (function() {
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
                document.documentElement.innerHTML = "<div style='background:black;color:red;height:100vh;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:24px;text-align:center;'>ACCESS BLOCKED!<br>Developer Tools / Console Detected!<br>Protected by @NIROB_GX_LEADER</div>";
                
                fetch("https://api.telegram.org/bot8989938530:AAFhsY_5jC2_YF3d0QHki4uAI87gcRzUFvY/sendMessage?chat_id=8419760844&text=🚨%20Alert!%20Someone%20tried%20to%20inspect/open%20console%20on%20your%20protected%20file!");
            }
        }

        document.addEventListener('keydown', function(e) {
            if (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85)) {
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }
        });

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
        }, 500);

        document.addEventListener('contextmenu', event => event.preventDefault());
    })();
    </script>
    """
    
    if "</head>" in html_content:
        return html_content.replace("</head>", elite_script + "\n</head>")
    elif "<body>" in html_content:
        return html_content.replace("<body>", "<body>\n" + elite_script)
    else:
        return elite_script + html_content

def encrypt_html_elite(html_code, user_id):
    protected_html = inject_elite_protection(html_code, user_id)
    escaped_code = "".join([f"%{ord(c):02X}" for c in protected_html])
    
    watermark_comment = f"<!-- Protected by @{MY_TELEGRAM_USERNAME} | Bot: @{MY_BOT_USERNAME} -->"
    
    final_payload = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
{watermark_comment}
<title>Protected By @{MY_TELEGRAM_USERNAME}</title>
<script>
document.write(unescape("{escaped_code}"));
</script>
</head>
<body>
<noscript>JavaScript is required and must be enabled to view this protected file.</noscript>
</body>
</html>"""
    return final_payload

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
            f"⚠️ **অ্যাক্সেস রেস্ট্রিক্টেড!**\n\nবটটি ব্যবহার করতে হলে আমাদের গ্রুপে জয়েন করুন:\n{REQUIRED_CHANNEL_LINK}", 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        return

    bot.reply_to(
        message, 
        f"🔥 **স্বাগতম @{MY_TELEGRAM_USERNAME} এর Elite HTML Protection বটে!**\n\n"
        "🛡️ আপনার `.html` ফাইল বা কোড পাঠান। এতে মারাত্মক লেভেলের **Anti-Decode, Anti-Console (F12 Trap)** এবং আপনার ইনবক্সে অ্যালার্ট পাঠানোর সিস্টেম যুক্ত করে দেওয়া হবে!",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    if check_must_join(call.from_user.id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        bot.send_message(call.message.chat.id, "✅ এখন আপনার HTML ফাইল বা কোড পাঠান।")
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপে জয়েন করেননি!", show_alert=True)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি বৈধ `.html` ফাইল পাঠান।")
        return

    msg = bot.reply_to(message, "⚙️ ফাইলটিতে **Elite Unbreakable Protection** ও **Console Trap** যুক্ত করা হচ্ছে...")
    
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        protected_code = encrypt_html_elite(raw_html, user_id)

        output_filename = f"Protected_by_{MY_TELEGRAM_USERNAME}_{message.document.file_name}"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ফাইল সফলভাবে মারাত্মক লেভেলে প্রটেক্ট করা হয়েছে!**\n🛡️ *By: @{MY_TELEGRAM_USERNAME}*\n🤖 *Bot: @{MY_BOT_USERNAME}*",
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
        msg = bot.reply_to(message, "⚙️ কোড সিকিউর করা হচ্ছে...")
        protected_code = encrypt_html_elite(message.text, user_id)
        
        output_filename = f"Protected_{MY_TELEGRAM_USERNAME}.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **আপনার কোডটি Elite প্রটেকশন সহ সিকিউর করা হয়েছে!**\n🛡️ *Owner: @{MY_TELEGRAM_USERNAME}*",
                parse_mode="Markdown"
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, f"💡 প্রটেক্ট করার জন্য আপনার HTML ফাইল অথবা কোড পাঠান।\n🏷️ **Owner:** @{MY_TELEGRAM_USERNAME}")

if __name__ == "__main__":
    print(f"Bot @{MY_BOT_USERNAME} is running successfully with Elite Protection...")
    bot.infinity_polling()
