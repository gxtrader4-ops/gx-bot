```python
import os
import re
import html
import tempfile
import logging
from pathlib import Path

import telebot
from telebot import types

# =====================================================
# CONFIGURATION
# =====================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()

ADMIN_ID = 8419760844
REQUIRED_CHANNEL_ID = -1003810620422
REQUIRED_CHANNEL_LINK = "https://t.me/SUPPOR8TNIROB"

MY_TELEGRAM_USERNAME = "NIROB_GX_LEADER"
MY_BOT_USERNAME = "nirob_team_Obucsate_bot"

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {".html", ".htm"}

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN সেট করা নেই। Environment variable-এ সেট করুন।"
    )

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# =====================================================
# MEMBERSHIP CHECK
# =====================================================

def check_must_join(user_id):
    try:
        member = bot.get_chat_member(
            REQUIRED_CHANNEL_ID,
            user_id
        )
        return member.status in (
            "creator",
            "administrator",
            "member"
        )
    except Exception:
        logging.exception("Membership verification failed")
        return False


def get_main_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )

    markup.add(
        types.KeyboardButton("🛡️ HTML Security"),
        types.KeyboardButton("📌 Help & Guide"),
        types.KeyboardButton("📢 Official Channel/Group")
    )

    if user_id == ADMIN_ID:
        markup.add(
            types.KeyboardButton("⚙️ Admin Panel")
        )

    return markup


def send_join_prompt(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(
            "Join Channel 📢",
            url=REQUIRED_CHANNEL_LINK
        ),
        types.InlineKeyboardButton(
            "Check Join ✅",
            callback_data="check_join"
        )
    )

    bot.reply_to(
        message,
        "⚠️ বট ব্যবহার করতে প্রথমে নির্ধারিত চ্যানেলে Join করুন।",
        reply_markup=markup
    )


def user_is_allowed(message):
    if check_must_join(message.from_user.id):
        return True

    send_join_prompt(message)
    return False


# =====================================================
# HTML PROCESSING
# =====================================================

def validate_html_filename(filename):
    if not filename or len(filename) > 180:
        return False

    # Path traversal / unusual filename rejection
    if Path(filename).name != filename:
        return False

    if "\x00" in filename:
        return False

    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def validate_html_content(content):
    if not content or not content.strip():
        raise ValueError("HTML ফাইলটি খালি।")

    if len(content.encode("utf-8")) > MAX_FILE_SIZE:
        raise ValueError("HTML ফাইলের সাইজ 5 MB-এর বেশি।")

    if not re.search(r"<\s*(html|body|head|div|!doctype)\b",
                     content, re.IGNORECASE):
        raise ValueError("সঠিক HTML ডকুমেন্ট পাওয়া যায়নি।")

    return content


def protect_html(content):
    """
    নিরাপদ HTML processing.

    এখানে ইচ্ছাকৃতভাবে debugger loop, DevTools detection,
    browser lockout বা গোপনে তথ্য পাঠানোর JavaScript নেই।

    ব্রাউজারে পাঠানো HTML/CSS/JS সম্পূর্ণ গোপন রাখা যায় না।
    এই ফাংশন মূল HTML অক্ষত রাখে এবং basic validation করে।
    """

    content = validate_html_content(content)

    # Add a harmless copyright comment if not already present.
    marker = "<!-- Protected by NIROB_GX_LEADER -->"

    if marker not in content:
        if re.search(r"<\s*html\b", content, re.IGNORECASE):
            match = re.search(
                r"<\s*html\b[^>]*>",
                content,
                re.IGNORECASE
            )

            if match:
                position = match.end()
                content = (
                    content[:position]
                    + "\n"
                    + marker
                    + "\n"
                    + content[position:]
                )
        else:
            content = marker + "\n" + content

    return content


def safe_output_filename(original_name):
    suffix = Path(original_name).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        suffix = ".html"

    return "Protected_" + "website" + suffix


# =====================================================
# START COMMAND
# =====================================================

@bot.message_handler(commands=["start"])
def send_welcome(message):
    if not user_is_allowed(message):
        return

    bot.reply_to(
        message,
        "স্বাগতম! 🛡️ NIROB HTML Security Bot\n\n"
        "আপনার .html অথবা .htm ফাইল পাঠান।\n"
        "বট ফাইলটি যাচাই করে প্রসেস করা কপি ফেরত দেবে।\n\n"
        "মনে রাখবেন: ব্রাউজারে চলা কোড শতভাগ কপি-প্রুফ নয়।",
        reply_markup=get_main_keyboard(message.from_user.id)
    )


# =====================================================
# JOIN VERIFICATION CALLBACK
# =====================================================

@bot.callback_query_handler(
    func=lambda call: call.data == "check_join"
)
def callback_check_join(call):
    if check_must_join(call.from_user.id):
        bot.answer_callback_query(
            call.id,
            "সফলভাবে যাচাই হয়েছে!"
        )

        bot.send_message(
            call.message.chat.id,
            "✅ এখন বট ব্যবহার করতে পারবেন।",
            reply_markup=get_main_keyboard(call.from_user.id)
        )
    else:
        bot.answer_callback_query(
            call.id,
            "প্রথমে চ্যানেলে Join করুন।",
            show_alert=True
        )


# =====================================================
# MENU HANDLER
# =====================================================

@bot.message_handler(
    func=lambda msg: msg.text in [
        "🛡️ HTML Security",
        "📌 Help & Guide",
        "📢 Official Channel/Group",
        "⚙️ Admin Panel"
    ]
)
def handle_menu_clicks(message):
    if not user_is_allowed(message):
        return

    user_id = message.from_user.id

    if message.text == "🛡️ HTML Security":
        bot.reply_to(
            message,
            "📂 আপনার .html বা .htm ফাইল Document হিসেবে পাঠান।"
        )

    elif message.text == "📌 Help & Guide":
        bot.reply_to(
            message,
            "📖 ব্যবহারবিধি:\n"
            "1. প্রথমে চ্যানেলে Join করুন।\n"
            "2. HTML ফাইল আপলোড করুন।\n"
            "3. প্রসেস করা ফাইল গ্রহণ করুন।\n\n"
            "এই বট HTML validation করে; "
            "ব্রাউজারের সোর্স কোড সম্পূর্ণ গোপন করতে পারে না।"
        )

    elif message.text == "📢 Official Channel/Group":
        bot.reply_to(
            message,
            "📢 Official Channel:\n" + REQUIRED_CHANNEL_LINK
        )

    elif message.text == "⚙️ Admin Panel":
        if user_id != ADMIN_ID:
            bot.reply_to(message, "⛔ অনুমতি নেই।")
            return

        bot.reply_to(
            message,
            "⚙️ Admin Panel\n\n"
            "Bot status: Running\n"
            "Maximum HTML size: 5 MB\n"
            "Allowed extensions: .html, .htm\n"
            "Admin access: Enabled"
        )


# =====================================================
# DOCUMENT HANDLER
# =====================================================

@bot.message_handler(content_types=["document"])
def handle_document(message):
    if not user_is_allowed(message):
        return

    document = message.document
    filename = document.file_name or ""

    if not validate_html_filename(filename):
        bot.reply_to(
            message,
            "❌ শুধু .html অথবা .htm ফাইল আপলোড করুন।"
        )
        return

    if document.file_size and document.file_size > MAX_FILE_SIZE:
        bot.reply_to(
            message,
            "❌ ফাইলের সর্বোচ্চ সাইজ 5 MB।"
        )
        return

    status_message = bot.reply_to(
        message,
        "⏳ HTML ফাইল যাচাই ও প্রসেস করা হচ্ছে..."
    )

    try:
        file_info = bot.get_file(document.file_id)
        downloaded = bot.download_file(file_info.file_path)

        if len(downloaded) > MAX_FILE_SIZE:
            raise ValueError("ফাইলের সাইজ 5 MB-এর বেশি।")

        # Decode HTML. Keep normal UTF-8 content intact.
        raw_html = downloaded.decode("utf-8-sig", errors="strict")
        protected_code = protect_html(raw_html)

        output_name = safe_output_filename(filename)

        # Temporary file is removed automatically.
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / output_name
            output_path.write_text(
                protected_code,
                encoding="utf-8"
            )

            with output_path.open("rb") as output_file:
                bot.send_document(
                    message.chat.id,
                    output_file,
                    caption=(
                        "✅ HTML ফাইল প্রসেস সম্পন্ন।\n"
                        "🛡️ Owner: @NIROB_GX_LEADER\n\n"
                        "নোট: এটি সম্পূর্ণ anti-copy protection নয়।"
                    ),
                    reply_markup=get_main_keyboard(
                        message.from_user.id
                    )
                )

        bot.delete_message(
            message.chat.id,
            status_message.message_id
        )

        # Do not automatically send users' original files
        # to an admin without their explicit consent.

    except UnicodeDecodeError:
        bot.edit_message_text(
            "❌ ফাইলটি UTF-8 টেক্সট হিসেবে পড়া যায়নি।",
            message.chat.id,
            status_message.message_id
        )

    except Exception as exc:
        logging.exception("HTML processing failed")

        safe_error = html.escape(str(exc)[:250])

        try:
            bot.edit_message_text(
                "❌ ফাইল প্রসেস করা যায়নি।\n" + safe_error,
                message.chat.id,
                status_message.message_id
            )
        except Exception:
            bot.send_message(
                message.chat.id,
                "❌ ফাইল প্রসেস করা যায়নি।"
            )


# =====================================================
# HTML TEXT HANDLER
# =====================================================

@bot.message_handler(
    content_types=["text"],
    func=lambda message: not (
        message.text or ""
    ).startswith("/")
)
def handle_text(message):
    if not user_is_allowed(message):
        return

    text_content = message.text or ""

    if not re.search(
        r"<\s*(html|body|head|div|!doctype)\b",
        text_content,
        re.IGNORECASE
    ):
        bot.reply_to(
            message,
            "💡 একটি HTML কোড পাঠান অথবা .html ফাইল আপলোড করুন।",
            reply_markup=get_main_keyboard(message.from_user.id)
        )
        return

    if len(text_content.encode("utf-8")) > MAX_FILE_SIZE:
        bot.reply_to(message, "❌ HTML কোডটি অনেক বড়।")
        return

    try:
        protected_code = protect_html(text_content)

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "Protected_Code.html"
            output_path.write_text(
                protected_code,
                encoding="utf-8"
            )

            with output_path.open("rb") as output_file:
                bot.send_document(
                    message.chat.id,
                    output_file,
                    caption=(
                        "✅ HTML কোড প্রসেস সম্পন্ন।\n"
                        "🛡️ By @NIROB_GX_LEADER"
                    ),
                    reply_markup=get_main_keyboard(
                        message.from_user.id
                    )
                )

    except Exception:
        logging.exception("HTML text processing failed")
        bot.reply_to(
            message,
            "❌ HTML কোড প্রসেস করার সময় সমস্যা হয়েছে।"
        )


# =====================================================
# RUN BOT
# =====================================================

if __name__ == "__main__":
    logging.info("NIROB HTML Security Bot is starting...")

    try:
        bot.infinity_polling(
            skip_pending=True,
            allowed_updates=["message", "callback_query"]
        )
    except Exception:
        logging.exception("Bot stopped unexpectedly")
        raise
```
