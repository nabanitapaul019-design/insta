import telebot
import requests
import threading
import time
import re

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
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL, style="danger")
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦 | ➖]", url=BOT_LIST, style="primary")
            )
            user_id = message.from_user.id
            try:
                photos = bot.get_user_profile_photos(user_id)
                has_photo = photos.total_count > 0
            except Exception:
                has_photo = False
            caption = f"🚨𝗛𝗜 👋 *{message.from_user.first_name}* \n\n‼ 🔒𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 ! 🔒 \n\n🔒 *𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 !* 🔒"
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
            telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL, style="primary")
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
    button1 = telebot.types.InlineKeyboardButton(text="[➖ 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥 ➖]", url=OWNER_URL, style="primary")
    button2 = telebot.types.InlineKeyboardButton(text="[➖ 𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ➖]", url=CHANNEL_URL, style="danger")
    button3 = telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦  | ➖]", url=BOT_LIST, style="success")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    welcome_text = (
        "𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗘𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧\n\n"
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
                message.chat.id, photo_file_id,
                caption=welcome_text,
                parse_mode="Markdown",
                reply_markup=markup
            )
        except Exception:
            bot.send_message(
                message.chat.id, welcome_text,
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=markup
            )
    else:
        bot.send_message(
            message.chat.id, welcome_text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=markup
        )

    # Notify owner(s) about new user
    user_name = (message.from_user.username and f"@{message.from_user.username}") or message.from_user.first_name or str(message.from_user.id)
    notify_text = f"👤 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗛𝗔𝗦 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗢𝗨𝗥 𝗕𝗢𝗧\n\n 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: {user_name}\n 𝗨𝗦𝗘𝗥 𝗜𝗗: {message.from_user.id}"

    for owner_id in OWNER_IDS:
        if owner_id != message.from_user.id:
            try:
                bot.send_message(owner_id, notify_text)
            except Exception as e:
                print(f"Failed to notify owner {owner_id}: {e}")

def is_instagram_url(url):
    instagram_url_pattern = r"^(https?://)?(www\.)?instagram\.com/.*$"
    return re.match(instagram_url_pattern, url) is not None

def extract_video_from_fastvideosave(url):
    """
    Robust extraction from fastvideosave.net with multiple fallback patterns
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://fastvideosave.net/',
            'Connection': 'keep-alive',
        }
        
        response = requests.get(f"https://fastvideosave.net/?url={url}", headers=headers, timeout=20)
        
        if response.status_code != 200:
            print(f"[FALLBACK] fastvideosave returned status: {response.status_code}")
            return None
            
        html = response.text
        
        # Multiple regex patterns to catch different possible video URL formats
        patterns = [
            r'(https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*)',  # Direct .mp4 links
            r'data-video=["\'](https?://[^"\']+\.mp4[^"\']*)["\']',  # data-video attribute
            r'src=["\'](https?://[^"\']+\.mp4[^"\']*)["\']',  # src attribute
            r'"url"\s*:\s*["\'](https?://[^"\']+\.mp4[^"\']*)["\']',  # JSON-like url field
            r'(https?://cdn[^"\']+\.mp4[^\s"\'<>]*)',  # CDN links
        ]
        
        for pattern in patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                video_url = match.group(1).replace('\\', '')  # Clean escaped chars
                print(f"[FALLBACK] Found video URL with pattern: {video_url[:50]}...")
                return video_url
        
        # Last resort: look for any http URL that contains "video" or "mp4"
        broad_match = re.search(r'(https?://[^\s"\'<>]*(?:video|mp4)[^\s"\'<>]*\.mp4[^\s"\'<>]*)', html, re.IGNORECASE)
        if broad_match:
            video_url = broad_match.group(1).replace('\\', '')
            print(f"[FALLBACK] Found video URL with broad pattern: {video_url[:50]}...")
            return video_url
            
        print("[FALLBACK] No video URL found in fastvideosave response")
        return None
        
    except Exception as e:
        print(f"[FALLBACK] Exception during extraction: {str(e)}")
        return None

@bot.message_handler(func=lambda message: re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def download_reel_with_caption(message):
    if not check_user_membership(message):
        return

    url = message.text.strip()
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻𝗸......")

    video_url = None
    combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
    use_fallback = False

    # === STEP 1: Try Primary API ===
    try:
        print(f"[PRIMARY] Requesting: {url}")
        api_v2_url = f"https://api.yabes-desu.workers.dev/download/instagram/v2?url={url}"
        response_v2 = requests.get(api_v2_url, timeout=15)
        
        print(f"[PRIMARY] Status: {response_v2.status_code}")
        
        if response_v2.status_code == 200:
            try:
                data_v2 = response_v2.json()
                print(f"[PRIMARY] Response keys: {list(data_v2.keys()) if isinstance(data_v2, dict) else 'Not a dict'}")
                
                # Validate response structure deeply
                if (isinstance(data_v2, dict) and 
                    'data' in data_v2 and 
                    isinstance(data_v2['data'], dict) and
                    'url' in data_v2['data'] and 
                    isinstance(data_v2['data']['url'], list) and 
                    len(data_v2['data']['url']) > 0 and
                    data_v2['data']['url'][0]):
                    
                    video_url = data_v2['data']['url'][0]
                    print(f"[PRIMARY] Got video URL: {video_url[:50]}...")
                    
                    # Build caption from primary API
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                    if caption_text is None:
                        caption_text = "No caption available."
                    
                    max_caption_length = 500
                    if len(caption_text) > max_caption_length:
                        caption_text = caption_text[:max_caption_length] + "..."
                    
                    footer = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                    combined_caption = f"{caption_text}{footer}"
                    
                    if len(combined_caption) > 1024:
                        caption_text = caption_text[:1024 - len(footer) - 3] + "..."
                        combined_caption = f"{caption_text}{footer}"
                        
                else:
                    print("[PRIMARY] Invalid response structure - triggering fallback")
                    use_fallback = True
                    
            except ValueError as e:
                print(f"[PRIMARY] JSON decode error: {e} - triggering fallback")
                use_fallback = True
        else:
            print(f"[PRIMARY] Non-200 status - triggering fallback")
            use_fallback = True
            
    except Exception as e:
        print(f"[PRIMARY] Exception: {str(e)} - triggering fallback")
        use_fallback = True

    # === STEP 2: Fallback to fastvideosave.net if needed ===
    if use_fallback or not video_url:
        print("[FALLBACK] Attempting fastvideosave.net extraction...")
        try:
            fallback_url = extract_video_from_fastvideosave(url)
            if fallback_url:
                video_url = fallback_url
                # Use the exact static caption you requested for fallback
                combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                print("[FALLBACK] Successfully extracted video URL")
            else:
                print("[FALLBACK] Failed to extract video URL")
        except Exception as e:
            print(f"[FALLBACK] Exception: {str(e)}")

    # === STEP 3: Final check and send ===
    if not video_url:
        try:
            bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
        except Exception:
            pass
        bot.reply_to(message, "‼ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 𝗹𝗮𝘁𝗲𝗿.‼")
        return

    # Clean up processing message
    try:
        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
    except Exception:
        pass

    # Send progress message
    progress_msg = bot.reply_to(message, "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗻𝗱 ! 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ⤵ ")
    threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

    # Ensure caption is UTF-8 safe
    try:
        combined_caption = combined_caption.encode('utf-8').decode('utf-8')
    except Exception:
        combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"

    # Send the video
    try:
        bot.send_video(message.chat.id, video_url, caption=combined_caption)
    except Exception as e:
        print(f"[SEND] Error: {str(e)}")
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘃𝗶𝗱𝗲𝗼. 𝗘𝗿𝗿𝗼𝗿 : {str(e)}")
        return

    # Ready message
    bot.send_message(
        message.chat.id,
        "𝗜 𝗮𝗺 𝗿𝗲𝗮𝗱𝘆 𝗳𝗼 𝘆𝗼 𝗻𝗲𝘅𝘁 𝘃𝗶𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝘂 👀 \n\n[ 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
    )

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

print("🤖 Bot started successfully...")
bot.polling()
