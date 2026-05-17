import telebot
import requests
import threading
import time
import re
import json
from urllib.parse import quote

# Function to read token from file
def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Initialize bot with token
BOT_TOKEN = read_token_from_file('token.txt')
bot = telebot.TeleBot(BOT_TOKEN)

REQUIRED_CHANNEL = '@mrinxdildos'
BOT_LIST = "https://t.me/MRiNxDiLDOS/3 "
OWNER_URL = "https://t.me/M_o_y_zzz "
OWNER_IDS = {2007860433}
CHANNEL_URL = "https://t.me/mrinxdildos "

# Define the required channel
required_channel = '@MRiNxDiLDOS'

# Delete existing webhook before polling
bot.remove_webhook()

# Function to delete message after delay
def delete_after_delay(chat_id, message_id):
    time.sleep(9)
    try:
        bot.delete_message(chat_id, message_id)
    except Exception:
        pass

def check_user_membership(message):
    try:
        user_status = bot.get_chat_member(REQUIRED_CHANNEL, message.from_user.id).status
        if user_status not in ["member", "administrator", "creator"]:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗧 𝗝𝗢𝗜 𝗛𝗘𝗘 𝗢 𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL)
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗢𝗧𝗦 | ➖]", url=BOT_LIST)
            )

            user_id = message.from_user.id

            try:
                photos = bot.get_user_profile_photos(user_id)
                has_photo = photos.total_count > 0
            except Exception:
                has_photo = False

            caption = f"🚨𝗛 👋 *{message.from_user.first_name}* \n\n‼ 🔒𝗠𝗥𝗶 𝘅 𝗶𝗟𝗢𝗦™ 𝗜𝗡𝗦𝗔𝗚𝗥𝗔𝗠 𝗗𝗢𝗡𝗢𝗔𝗗𝗘𝗥 𝗢𝗧 𝗔𝗖𝗖𝗦𝗦 𝗘𝗡𝗜𝗘𝗗 ! 🔒 \n\n🔒 *𝗼𝗶𝗻 𝗼𝗿 𝗼𝗳𝗳𝗶𝗶𝗮𝗹 𝗰𝗵𝗮𝗻𝗻𝗹 𝗼 𝘂𝗲 𝗵𝗶𝘀 𝗯𝗼𝘁 !* 🔒"

            if has_photo:
                try:
                    photo_file_id = photos.photos[0][0].file_id

                    bot.send_photo(
                        message.chat.id,
                        photo_file_id,
                        caption=caption,
                        parse_mode="Markdown",
                        reply_markup=markup
                    )

                except Exception:
                    bot.send_message(
                        message.chat.id,
                        caption,
                        parse_mode="Markdown",
                        reply_markup=markup
                    )

            else:
                bot.send_message(
                    message.chat.id,
                    caption,
                    parse_mode="Markdown",
                    reply_markup=markup
                )

            return False

        return True

    except Exception as e:

        markup = telebot.types.InlineKeyboardMarkup()

        markup.add(
            telebot.types.InlineKeyboardButton(
                "[➖ 𝟭𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥 𝗧 𝗨𝗘 𝗠𝗘 ➖]",
                url=CHANNEL_URL
            )
        )

        bot.send_message(
            message.chat.id,
            f"Error checking membership: {str(e)}",
            reply_markup=markup
        )

        return False

# === START COMMAND ===
@bot.message_handler(commands=['start'])
def send_welcome(message):

    if not check_user_membership(message):
        return

    user_id = message.from_user.id

    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton(
        text="[➖ 𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗘 ➖]",
        url=OWNER_URL
    )

    button2 = telebot.types.InlineKeyboardButton(
        text="[➖ 𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘 ➖]",
        url=CHANNEL_URL
    )

    button3 = telebot.types.InlineKeyboardButton(
        text="[➖ | 𝗠 𝘅 ™ 𝗔𝗟 𝗢𝗦 | ➖]",
        url=BOT_LIST
    )

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    welcome_text = (
        "𝗪𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗥𝗶 𝘅 𝗗𝗶𝗟𝗗𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗗𝗘 𝗕𝗢𝗧\n\n"
        " 📎 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀 !\n\n"
    )

    try:
        photos = bot.get_user_profile_photos(user_id)
        has_photo = photos.total_count > 0
    except Exception:
        has_photo = False

    if has_photo:
        try:
            photo_file_id = photos.photos[0][0].file_id

            bot.send_photo(
                message.chat.id,
                photo_file_id,
                caption=welcome_text,
                parse_mode="Markdown",
                reply_markup=markup
            )

        except Exception:

            bot.send_message(
                message.chat.id,
                welcome_text,
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=markup
            )

    else:
        bot.send_message(
            message.chat.id,
            welcome_text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=markup
        )

    # Notify owners
    user_name = (
        message.from_user.username and
        f"@{message.from_user.username}"
    ) or message.from_user.first_name or str(message.from_user.id)

    notify_text = (
        f"👤 𝗘𝗪 𝗨𝗦𝗥 𝗛𝗔𝗦 𝗦𝗧𝗥𝗧𝗘𝗗 𝗨𝗥 𝗕𝗢𝗧\n\n"
        f"𝗨𝗘𝗥𝗔𝗠𝗘: {user_name}\n"
        f"𝗨𝗘 𝗜𝗗: {message.from_user.id}"
    )

    for owner_id in OWNER_IDS:
        if owner_id != message.from_user.id:
            try:
                bot.send_message(owner_id, notify_text)
            except Exception as e:
                print(f"Failed to notify owner {owner_id}: {e}")

def is_instagram_url(url):
    instagram_url_pattern = r"^(https?://)?(www\.)?instagram\.com/.*$"
    return re.match(instagram_url_pattern, url) is not None

# =========================
# FASTVIDEOSAVE FALLBACK
# =========================
def extract_video_from_fastvideosave(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://fastvideosave.net/"
        }

        session = requests.Session()

        target_url = f"https://fastvideosave.net/?url={quote(url)}"

        response = session.get(
            target_url,
            headers=headers,
            timeout=30
        )

        print(f"[FALLBACK] Status Code: {response.status_code}")

        if response.status_code != 200:
            return None

        html = response.text

        with open(
            "fastvideosave_debug.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)

        print("[FALLBACK] Saved HTML")

        patterns = [

            r'href="(https://[^"]+\.mp4[^"]*)".*?Download Video',

            r'href="(https://[^"]+\.mp4[^"]*)"',

            r'(https://cdn[^"\']+\.mp4[^"\']*)',

            r'(https://[^"\']*instagram[^"\']*\.mp4[^"\']*)',
        ]

        for pattern in patterns:

            matches = re.findall(
                pattern,
                html,
                re.IGNORECASE | re.DOTALL
            )

            if matches:

                for video_url in matches:

                    video_url = (
                        video_url
                        .replace("&amp;", "&")
                        .replace("\\/", "/")
                        .strip()
                    )

                    if ".mp4" in video_url:

                        print(
                            f"[FALLBACK] Found Video: "
                            f"{video_url[:100]}"
                        )

                        return video_url

        hrefs = re.findall(r'href="([^"]+)"', html)

        for href in hrefs:

            href = (
                href
                .replace("&amp;", "&")
                .replace("\\/", "/")
                .strip()
            )

            if ".mp4" in href:
                print(f"[FALLBACK] Found MP4 href")
                return href

        print("[FALLBACK] No video URL found")
        return None

    except Exception as e:

        print(f"[FALLBACK] Exception: {str(e)}")

        import traceback
        traceback.print_exc()

        return None

# =========================
# MAIN HANDLER
# =========================
@bot.message_handler(
    func=lambda message:
    re.match(
        r"^(https?://)?(www\.)?instagram\.com/.*$",
        message.text
    )
)
def download_reel_with_caption(message):

    if not check_user_membership(message):
        return

    url = message.text.strip()

    processing_msg = bot.reply_to(
        message,
        "⏳ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻𝗸......"
    )

    video_url = None

    combined_caption = (
        "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 "
        "𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 "
        "𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 "
        "@instra_dwn_bymrin_bot ❤️\n\n"
    )

    use_fallback = False

    # =========================
    # PRIMARY API
    # =========================
    try:

        print(f"[PRIMARY] Requesting: {url}")

        api_v2_url = (
            "https://api.yabes-desu.workers.dev/"
            f"download/instagram/v2?url={url}"
        )

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response_v2 = requests.get(
            api_v2_url,
            headers=headers,
            timeout=20
        )

        print(f"[PRIMARY] Status: {response_v2.status_code}")

        if response_v2.status_code == 200:

            try:

                data_v2 = response_v2.json()

                print(
                    f"[PRIMARY] Response keys: "
                    f"{list(data_v2.keys())}"
                )

                # Structure 1
                if (
                    isinstance(data_v2, dict)
                    and 'data' in data_v2
                    and isinstance(data_v2['data'], dict)
                    and 'url' in data_v2['data']
                ):

                    if isinstance(data_v2['data']['url'], list):
                        video_url = data_v2['data']['url'][0]
                    else:
                        video_url = data_v2['data']['url']

                    caption_text = (
                        data_v2['data'].get('caption')
                        or "No caption available."
                    )

                # Structure 2
                elif (
                    isinstance(data_v2, dict)
                    and data_v2.get("success") == True
                    and isinstance(data_v2.get("message"), dict)
                ):

                    msg_data = data_v2["message"]

                    if "url" in msg_data:

                        if isinstance(msg_data["url"], list):
                            video_url = msg_data["url"][0]
                        else:
                            video_url = msg_data["url"]

                    elif "video_url" in msg_data:
                        video_url = msg_data["video_url"]

                    caption_text = (
                        msg_data.get("caption")
                        or msg_data.get("title")
                        or "No caption available."
                    )

                # Structure 3
                elif (
                    isinstance(data_v2, dict)
                    and "url" in data_v2
                ):

                    video_url = data_v2["url"]

                    caption_text = (
                        data_v2.get("caption")
                        or "No caption available."
                    )

                if video_url:

                    max_caption_length = 500

                    if len(caption_text) > max_caption_length:
                        caption_text = (
                            caption_text[:max_caption_length]
                            + "..."
                        )

                    footer = (
                        "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 "
                        "𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 "
                        "𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 "
                        "@instra_dwn_bymrin_bot ❤️\n\n"
                    )

                    combined_caption = (
                        f"{caption_text}{footer}"
                    )

                else:

                    print(
                        "[PRIMARY] No video URL found"
                    )

                    use_fallback = True

            except Exception as e:

                print(
                    f"[PRIMARY] JSON error: {str(e)}"
                )

                use_fallback = True

        else:

            use_fallback = True

    except Exception as e:

        print(f"[PRIMARY] Exception: {str(e)}")

        use_fallback = True

    # =========================
    # FALLBACK
    # =========================
    if use_fallback or not video_url:

        print("[FALLBACK] Trying fallback...")

        fallback_url = extract_video_from_fastvideosave(url)

        if fallback_url:

            video_url = fallback_url

            combined_caption = (
                "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 "
                "𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 "
                "𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 "
                "@instra_dwn_bymrin_bot ❤️\n\n"
            )

            print("[FALLBACK] Success")

        else:

            print("[FALLBACK] Failed")

    # =========================
    # FINAL CHECK
    # =========================
    if not video_url:

        try:
            bot.delete_message(
                processing_msg.chat.id,
                processing_msg.message_id
            )
        except Exception:
            pass

        bot.reply_to(
            message,
            "‼ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. "
            "𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 𝗹𝗮𝘁𝗲𝗿.‼"
        )

        return

    try:
        bot.delete_message(
            processing_msg.chat.id,
            processing_msg.message_id
        )
    except Exception:
        pass

    progress_msg = bot.reply_to(
        message,
        "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗻𝗱 ! 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ⤵"
    )

    threading.Thread(
        target=delete_after_delay,
        args=(
            progress_msg.chat.id,
            progress_msg.message_id
        )
    ).start()

    try:

        video_headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.instagram.com/"
        }

        video_response = requests.get(
            video_url,
            headers=video_headers,
            stream=True,
            timeout=60
        )

        if video_response.status_code == 200:

            bot.send_video(
                message.chat.id,
                video_response.raw,
                caption=combined_caption,
                supports_streaming=True
            )

        else:

            raise Exception(
                f"Video download failed: "
                f"{video_response.status_code}"
            )

    except Exception as e:

        print(f"[SEND] Error: {str(e)}")

        bot.reply_to(
            message,
            f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 "
            f"𝘃𝗶𝗱𝗲𝗼.\n\nError: {str(e)}"
        )

        return

    bot.send_message(
        message.chat.id,
        "𝗜 𝗮𝗺 𝗿𝗲𝗮𝗱𝘆 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 "
        "𝗻𝗲𝘅𝘁 𝘃𝗶𝗱𝗲𝗼.... "
        "𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 "
        "𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 "
        "𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 "
        "𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀 \n\n"
        "[ 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
    )

# Ignore non-Instagram messages
@bot.message_handler(
    func=lambda message:
    not re.match(
        r"^(https?://)?(www\.)?instagram\.com/.*$",
        message.text
    )
)
def ignore_message(message):
    pass

print("🤖 Bot started successfully...")

bot.polling()
