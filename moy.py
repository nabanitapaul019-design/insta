import telebot
import requests
import threading
import time
import re
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
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗧 𝗝𝗢𝗜 𝗛𝗘𝗘 𝗢 𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL, style="danger")
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗢𝗧𝗦 | ➖]", url=BOT_LIST, style="primary")
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
            telebot.types.InlineKeyboardButton("[➖ 𝟭𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥 𝗧 𝗨𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL, style="primary")
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
    button1 = telebot.types.InlineKeyboardButton(text="[➖ 𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗘 ➖]", url=OWNER_URL, style="primary")
    button2 = telebot.types.InlineKeyboardButton(text="[➖ 𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘 ➖]", url=CHANNEL_URL, style="danger")
    button3 = telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 ™ 𝗔𝗟 𝗢𝗦  | ➖]", url=BOT_LIST, style="success")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    welcome_text = (
        "𝗪𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗥𝗶 𝘅 𝗗𝗶𝗟𝗗𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗗𝗘 𝗕𝗢𝗧\n\n"
        " 📎 𝗣𝗹𝗲𝗮𝗲 𝘀𝗻 𝗮 𝗮𝗹𝗶𝗱 𝗜𝗻𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹 𝗱𝗼𝘄𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝘂 👀 !\n\n"
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
    notify_text = f"👤 𝗘𝗪 𝗨𝗦𝗥 𝗛𝗔𝗦 𝗦𝗧𝗥𝗧𝗘𝗗 𝗨𝗥 𝗕𝗢𝗧\n\n 𝗨𝗘𝗥𝗔𝗠𝗘: {user_name}\n 𝗨𝗘 𝗜𝗗: {message.from_user.id}"

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
    Extract video URL from fastvideosave.net using multiple methods
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://fastvideosave.net/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # Step 1: Make request to fastvideosave
        session = requests.Session()
        response = session.get(f"https://fastvideosave.net/?url={quote(url)}", headers=headers, timeout=20)
        
        if response.status_code != 200:
            print(f"[FALLBACK] fastvideosave returned status: {response.status_code}")
            return None
            
        html = response.text
        
        # Debug: Save HTML to file for inspection
        with open('fastvideosave_debug.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("[FALLBACK] Saved HTML response to fastvideosave_debug.html for inspection")
        
        # Method 1: Look for video URL in script tags (common pattern)
        script_patterns = [
            r'["\']video_url["\']\s*:\s*["\']([^"\']+\.mp4[^"\']*)["\']',
            r'["\']downloadUrl["\']\s*:\s*["\']([^"\']+\.mp4[^"\']*)["\']',
            r'["\']url["\']\s*:\s*["\']([^"\']+\.mp4[^"\']*)["\']',
            r'var\s+videoUrl\s*=\s*["\']([^"\']+\.mp4[^"\']*)["\']',
            r'var\s+downloadUrl\s*=\s*["\']([^"\']+\.mp4[^"\']*)["\']',
        ]
        
        for pattern in script_patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                video_url = match.group(1).replace('\\', '').replace('\/', '/')
                print(f"[FALLBACK] Found video in script tag: {video_url[:80]}...")
                return video_url
        
        # Method 2: Look for data attributes in HTML
        data_attr_patterns = [
            r'data-video-url=["\']([^"\']+\.mp4[^"\']*)["\']',
            r'data-download=["\']([^"\']+\.mp4[^"\']*)["\']',
            r'data-url=["\']([^"\']+\.mp4[^"\']*)["\']',
        ]
        
        for pattern in data_attr_patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                video_url = match.group(1).replace('\\', '').replace('\/', '/')
                print(f"[FALLBACK] Found video in data attribute: {video_url[:80]}...")
                return video_url
        
        # Method 3: Look for direct .mp4 links in the HTML
        mp4_pattern = r'(https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*)'
        matches = re.findall(mp4_pattern, html)
        if matches:
            for match in matches:
                video_url = match.replace('\\', '').replace('\/', '/')
                # Filter out common non-video URLs
                if any(x in video_url.lower() for x in ['video', 'instagram', 'cdn']):
                    print(f"[FALLBACK] Found direct mp4 link: {video_url[:80]}...")
                    return video_url
        
        # Method 4: Try to find API endpoint and call it
        # Look for fetch/XHR endpoints in the JavaScript
        api_endpoint_patterns = [
            r'fetch\(["\']([^"\']*download[^"\']*)["\']',
            r'axios\.(get|post)\(["\']([^"\']*download[^"\']*)["\']',
            r'\$\.ajax\({[^}]*url["\']?\s*:\s*["\']([^"\']*download[^"\']*)["\']',
        ]
        
        for pattern in api_endpoint_patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                api_path = match.group(1) if match.group(0).startswith('fetch') else match.group(2)
                print(f"[FALLBACK] Found potential API endpoint: {api_path}")
                # Try to call the API if it's a full URL
                if api_path.startswith('http'):
                    try:
                        api_response = session.get(api_path, headers=headers, timeout=10)
                        if api_response.status_code == 200:
                            api_data = api_response.json()
                            # Try to extract video URL from JSON
                            for key in ['url', 'video_url', 'download_url', 'data']:
                                if key in api_data:
                                    if isinstance(api_data[key], str) and '.mp4' in api_data[key]:
                                        print(f"[FALLBACK] Got video from API: {api_data[key][:80]}...")
                                        return api_data[key]
                                    elif isinstance(api_data[key], dict):
                                        for subkey in ['url', 'video_url', 'download_url']:
                                            if subkey in api_data[key] and '.mp4' in str(api_data[key][subkey]):
                                                print(f"[FALLBACK] Got video from API nested: {api_data[key][subkey][:80]}...")
                                                return api_data[key][subkey]
                    except Exception as e:
                        print(f"[FALLBACK] API call failed: {e}")
        
        print("[FALLBACK] No video URL found after all extraction methods")
        return None
        
    except Exception as e:
        print(f"[FALLBACK] Exception during extraction: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

@bot.message_handler(func=lambda message: re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def download_reel_with_caption(message):
    if not check_user_membership(message):
        return

    url = message.text.strip()
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻......")

    video_url = None
    combined_caption = "\n\n🎥 𝗛𝗲𝗿 𝗶𝘀 𝘆𝗼𝘂 𝗿𝗾𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
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
                
                # Check for multiple possible response structures
                video_url = None
                
                # Structure 1: data.url[0] (original)
                if (isinstance(data_v2, dict) and 
                    'data' in data_v2 and 
                    isinstance(data_v2['data'], dict) and
                    'url' in data_v2['data'] and 
                    isinstance(data_v2['data']['url'], list) and 
                    len(data_v2['data']['url']) > 0):
                    video_url = data_v2['data']['url'][0]
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                    print(f"[PRIMARY] Got video via data.url[0]: {video_url[:50]}...")
                
                # Structure 2: success + direct url
                elif (isinstance(data_v2, dict) and 
                      'success' in data_v2 and 
                      data_v2.get('success') == True and
                      'url' in data_v2):
                    video_url = data_v2['url']
                    caption_text = data_v2.get('caption') or "No caption available."
                    print(f"[PRIMARY] Got video via success+url: {video_url[:50]}...")
                
                # Structure 3: direct video_url field
                elif (isinstance(data_v2, dict) and 'video_url' in data_v2):
                    video_url = data_v2['video_url']
                    caption_text = data_v2.get('caption') or "No caption available."
                    print(f"[PRIMARY] Got video via video_url: {video_url[:50]}...")
                
                # Structure 4: data object with video_url
                elif (isinstance(data_v2, dict) and 
                      'data' in data_v2 and 
                      isinstance(data_v2['data'], dict) and
                      'video_url' in data_v2['data']):
                    video_url = data_v2['data']['video_url']
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                    print(f"[PRIMARY] Got video via data.video_url: {video_url[:50]}...")
                
                if video_url:
                    # Build caption
                    if caption_text is None:
                        caption_text = "No caption available."
                    
                    max_caption_length = 500
                    if len(caption_text) > max_caption_length:
                        caption_text = caption_text[:max_caption_length] + "..."
                    
                    footer = "\n\n🎥 𝗛𝗲𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                    combined_caption = f"{caption_text}{footer}"
                    
                    if len(combined_caption) > 1024:
                        caption_text = caption_text[:1024 - len(footer) - 3] + "..."
                        combined_caption = f"{caption_text}{footer}"
                else:
                    print("[PRIMARY] No video URL found in any expected structure - triggering fallback")
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
                combined_caption = "\n\n🎥 𝗲𝗿𝗲 𝗶𝘀 𝘆𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                print("[FALLBACK] Successfully extracted video URL")
            else:
                print("[FALLBACK] Failed to extract video URL")
        except Exception as e:
            print(f"[FALLBACK] Exception: {str(e)}")
            import traceback
            traceback.print_exc()

    # === STEP 3: Final check and send ===
    if not video_url:
        try:
            bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
        except Exception:
            pass
        bot.reply_to(message, "‼ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝗶𝗱𝗲𝗼. 𝗹𝗮𝘀𝗲 𝘁𝗿 𝗮𝗮𝗶𝗻 𝗹𝗮𝗲𝗿.‼")
        return

    # Clean up processing message
    try:
        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
    except Exception:
        pass

    # Send progress message
    progress_msg = bot.reply_to(message, "➖ 𝗩𝗱𝗲𝗼 𝗙𝗼𝘂𝗱 ! 𝗗𝗼𝘄𝗹𝗼𝗮𝗱𝗶𝗻 ⤵ ")
    threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

    # Ensure caption is UTF-8 safe
    try:
        combined_caption = combined_caption.encode('utf-8').decode('utf-8')
    except Exception:
        combined_caption = "\n\n🎥 𝗛𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗾𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"

    # Send the video
    try:
        bot.send_video(message.chat.id, video_url, caption=combined_caption)
    except Exception as e:
        print(f"[SEND] Error: {str(e)}")
        bot.reply_to(message, f"⚠️ 𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗱 𝗶𝗱𝗲𝗼. 𝗿𝗿𝗿 : {str(e)}")
        return

    # Ready message
    bot.send_message(
        message.chat.id,
        "𝗜 𝗮𝗺 𝗿𝗲𝗱 𝗳 𝘆 𝗻𝘅𝘁 𝘃𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗻𝗱 𝗮 𝘃𝗹𝗶 𝗜𝘀𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗲𝗲𝗹 𝗹𝗶𝗸, 𝗜 𝘄𝗹 𝗱𝗼𝘄𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆 👀 \n\n[ 𝗕𝗢 𝗖𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
    )

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

print("🤖 Bot started successfully...")
bot.polling()
