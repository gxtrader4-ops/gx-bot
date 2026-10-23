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
    return "NIROB GX Ultimate Anti-Decode Bot is running 24/7!"

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
        "👉 নিচের বাটন থেকে সাপোর্ট গ্রুপে জয়েন করে **'Check Membership'** বাটনে ক্লিক করুন。",
        reply_markup=markup
    )

def obfuscate_html(html_content):
    import base64
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    encoded_bytes = html_content.encode('utf-8')
    b64_1 = base64.b64encode(encoded_bytes).decode('utf-8')
    reversed_payload = b64_1[::-1]
    final_payload = base64.b64encode(reversed_payload.encode('utf-8')).decode('utf-8')
    
    fake_trap_stream = ""
    slangs_list = [
        "maderchod", "suorer_bacca", "chudir_bhai", "haramzada", "kutnar_bacca", 
        "tor_mar_saoya", "baaler_code", "churir_potti", "tor_bap_ke_ja", "tor_gusti_ki_puti"
    ]
    
    for i in range(200):
        fake_var = ''.join(random.choices(string.ascii_lowercase, k=8))
        slang_word = random.choice(slangs_list)
        line = "var _0x" + fake_var + "_[0x" + hex(random.randint(1000, 9999))[2:] + "] = '😡🖕 তোর মার সাউয়ার মধ্যে কোড চুরি করতে আইছোস রে " + slang_word + "?! ফাজলামি পাও পাইছো হারামজাদা! 🤬🔥';"
        fake_trap_stream += line + "\n"

    secured_HTML = """<!--
==================================================
🔥 100% UNBREAKABLE ANTI-DECODE BY NIROB GX 🔥
--------------------------------------------------
Obfuscated By: @NIROB_GX_LEADER
Bot Username: @nirob_team_Obucsate_bot
Timestamp: """ + current_time + """
Status: ANTI-DECODER TRAP & FAKE PAYLOAD ACTIVE 🛑
==================================================
-->
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>🛑 ANTI-THEFT PROTECTED BY NIROB GX | @nirob_team_Obucsate_bot 🤬</title>
    <style>
        html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; background:#000; font-family: sans-serif; user-select: none; -webkit-user-select: none; }
    </style>
</head>
<body oncontextmenu="return false;" onselectstart="return false;" ondragstart="return false;">
<script>
    /* 
       ====================================================================
       ⚠️ WARNING TO DECODER BOTS & HACKERS:
       তোর মাদারচোদ চৌদ্দ গুষ্টি উদ্ধার করে দিমু যদি এই কোড ডিকোড করার চেষ্টা করস! 
       এখানে কোনো আসল কোড নাই, শুধু গালি আর ফেক ট্র্যাপ আছে! কুত্তার বাচ্চা চোর! 🖕🤬
       ====================================================================
    */
    """ + fake_trap_stream + """
    
    var _0xgx_nirob_trap_l2 = '""" + final_payload + """';
    var isDestroyed = false;
    var telegramTrapLink = "https://t.me/NIROB_GX_LEADER?text=" + encodeURIComponent("🤬 ওরে নিরব আব্বা! আপনার সিকিউরিটি ভাঙতে গিয়া আমার চৌদ্দ গুষ্টি উদ্ধার হয়ে গেছে! কোড চুরি করার গুষ্টি মারি, আমারে মাফ করে দেন আব্বা! 🙏😭🔥");
    
    function triggerVoiceWarning() {
        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
                var msgText = "ওই মাদারচোদ শুয়োরের বাচ্চা! তোর এত বড় সাহস তুই নিরব আব্বার কোডে হাত দিস? ফালতু কোড চুরি করার চিন্তা বাদ দে! তোর মার সাউয়ার মধ্যে কোড ভরে দিমু হারামজাদা! কুত্তার বাচ্চা চোর!";
                var speech = new SpeechSynthesisUtterance(msgText);
                speech.lang = 'bn-BD';
                speech.rate = 0.9;
                window.speechSynthesis.speak(speech);
            } catch(err) {}
        }
    }
    
    function destroyAndRedirect() {
        if (isDestroyed) return;
        isDestroyed = true;
        triggerVoiceWarning();
        document.body.innerHTML = '<div style="background:#000;color:#ff0055;height:100vh;width:100vw;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;position:fixed;top:0;left:0;z-index:999999;">' +
            '<h1 style="font-size:28px;margin-bottom:10px;">⚠️ তোর মার সাউয়ার মধ্যে কোড ভরে দিমু শুয়োরের বাচ্চা! 😡🔥🖕</h1>' +
            '<p style="color:#fff;margin:15px 0;font-size:18px;">মাদারচোদ কোড চুরি করতে আইছো? ডিকোড মারার শখ মিটে গেছে? তাড়াতাড়ি নিরব আব্বাকে <b>@NIROB_GX_LEADER</b> এ গিয়ে বাপ ডাকো এবং মাফ চাও! না হলে তোর সব কোড চিরতরে ভ্যানিশ হয়ে যাবো! 👺💥</p>' +
            '<p style="color:#00ffcc;font-size:14px;margin-bottom:20px;">🤖 Ultimate Anti-Decode Bot: @nirob_team_Obucsate_bot</p>' +
            '<a href="' + telegramTrapLink + '" style="background:#ff0055;color:#fff;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:16px;box-shadow:0 0 20px #ff0055;">👉 নিরব আব্বারের টেলিগ্রামে দৌড়াও (মাফ চাও) 🏃‍♂️💨</a>' +
        '</div>';
        setTimeout(function() { window.location.href = telegramTrapLink; }, 2500);
    }
    
    window.addEventListener('keydown', function(e) {
        if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 67 || e.keyCode === 74)) || (e.ctrlKey && e.keyCode === 85)) {
            destroyAndRedirect();
            e.preventDefault();
            return false;
        }
    }, true);
    
    window.addEventListener('contextmenu', function(e) {
        destroyAndRedirect();
        e.preventDefault();
        return false;
    }, true);

    setInterval(function() {
        var widthThreshold = window.outerWidth - window.innerWidth > 160;
        var heightThreshold = window.outerHeight - window.innerHeight > 160;
        if (widthThreshold || heightThreshold) {
            destroyAndRedirect();
        }
    }, 400);
    
    (function(){
        try {
            var step1 = atob(_0xgx_nirob_trap_l2);
            var step2 = step1.split('').reverse().join('');
            var decoded_final = decodeURIComponent(escape(atob(step2)));
            document.open();
            document.write(decoded_final);
            document.close();
        } catch(e) {
            destroyAndRedirect();
        }
    })();
</script>
</body>
</html>"""
    return secured_HTML

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
