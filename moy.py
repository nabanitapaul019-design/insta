import telebot
import requests
import threading
import time
import re
import os
import sys
from urllib.parse import urlparse

# Try importing selenium
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
    print("[INFO] Selenium imported successfully")
except ImportError as e:
    SELENIUM_AVAILABLE = False
    print(f"[WARNING] Selenium not available: {e}")
    print("[WARNING] Install with: pip install selenium webdriver-manager")

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

# Download directory for fallback
DOWNLOAD_DIR = os.path.abspath('downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Default headers for requests
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

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
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥 𝗧 𝗨𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL, style="danger")
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
            caption = f"🚨𝗛 👋 *{message.from_user.first_name}* \n\n‼ 🔒𝗠𝗥𝗶𝗡 𝘅 𝗶𝗗𝗦™ 𝗜𝗡𝗧𝗔𝗚𝗥𝗔𝗠 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗢𝗧 𝗔𝗖𝗖𝗦𝗦 𝗗𝗘𝗡𝗘𝗗 ! 🔒 \n\n🔒 *𝗼𝗶𝗻 𝗼𝘂𝗿 𝗳𝗳𝗰𝗮𝗹 𝗵𝗮𝗻𝗻𝗲 𝘁𝗼 𝘂𝘀 𝘁𝗶 𝗯𝗼𝘁 !* 🔒"
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
    button1 = telebot.types.InlineKeyboardButton(text="[➖ 𝗖𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗘𝗥 ➖]", url=OWNER_URL, style="primary")
    button2 = telebot.types.InlineKeyboardButton(text="[➖ 𝗠𝗜𝗡 𝗛𝗔𝗡𝗡𝗘 ➖]", url=CHANNEL_URL, style="danger")
    button3 = telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 ™ 𝗔𝗟𝗟 𝗢𝗦  | ➖]", url=BOT_LIST, style="success")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    welcome_text = (
        "𝗪𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗥𝗶𝗡 𝘅 𝗗𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗘 𝗗𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗢𝗧\n\n"
        " 📎 𝗣𝗹𝗲𝗮𝗲 𝘀𝗻𝗱 𝗮 𝘃𝗹𝗶 𝗜𝘀𝘁𝗮𝗴𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗶𝗻𝗸, 𝗜 𝘄𝗹𝗹 𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝘂 👀 !\n\n"
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
    notify_text = f"👤 𝗡𝗪 𝗨𝗘 𝗛𝗦 𝗦𝗔𝗥𝗧𝗘𝗗 𝗨𝗥 𝗕𝗢𝗧\n\n 𝗨𝗘𝗥𝗡𝗔𝗠𝗘: {user_name}\n 𝗨𝗦𝗘𝗥 𝗗: {message.from_user.id}"

    for owner_id in OWNER_IDS:
        if owner_id != message.from_user.id:
            try:
                bot.send_message(owner_id, notify_text)
            except Exception as e:
                print(f"Failed to notify owner {owner_id}: {e}")

def is_instagram_url(url):
    instagram_url_pattern = r"^(https?://)?(www\.)?instagram\.com/.*$"
    return re.match(instagram_url_pattern, url) is not None

def _extract_instagram_shortcode(url: str):
    """Extract Instagram shortcode from URL."""
    match = re.search(r"instagram\.com/(?:reel|reels|p|tv)/(?P<shortcode>[A-Za-z0-9_\-]+)", url, re.IGNORECASE)
    if match:
        return match.group("shortcode")
    return None

def download_via_fastvideosave(url: str) -> str:
    """
    Fallback: Download Instagram video via fastvideosave.net using Selenium.
    Returns path to downloaded file or raises exception.
    """
    if not SELENIUM_AVAILABLE:
        raise RuntimeError("Selenium is not installed. Please install with: pip install selenium webdriver-manager")
    
    shortcode = _extract_instagram_shortcode(url)
    if not shortcode:
        raise ValueError("Invalid Instagram URL")
    
    driver = None
    try:
        print(f"[FALLBACK] Starting fastvideosave.net download for: {shortcode}")
        
        # Clean old downloads
        for f in os.listdir(DOWNLOAD_DIR):
            if f.endswith('.mp4'):
                try:
                    os.remove(os.path.join(DOWNLOAD_DIR, f))
                except:
                    pass
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        prefs = {
            "download.default_directory": DOWNLOAD_DIR,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        print("[FALLBACK] Creating Chrome driver...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(300)
        driver.set_script_timeout(300)
        
        print(f"[FALLBACK] Driver created successfully")
        
        # Navigate to fastvideosave
        print("[FALLBACK] Navigating to fastvideosave.net...")
        driver.get("https://fastvideosave.net/video")
        time.sleep(3)
        
        # Find and fill URL input
        print("[FALLBACK] Finding URL input field...")
        search_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='url'][name='url']"))
        )
        search_input.clear()
        search_input.send_keys(url)
        print(f"[FALLBACK] URL entered: {url}")
        
        # Click Download button
        print("[FALLBACK] Clicking Download button...")
        download_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        download_button.click()
        time.sleep(2)
        
        # Wait for "Download Video" button with specific SVG path
        print("[FALLBACK] Waiting for Download Video button...")
        download_video_button = None
        for i in range(90):
            try:
                buttons = driver.find_elements(By.CSS_SELECTOR, "button svg path[d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4m4-5 5 5 5-5m-5 5V3']")
                for btn in buttons:
                    parent = btn.find_element(By.XPATH, "./ancestor::button")
                    if parent and "Download Video" in parent.text:
                        download_video_button = parent
                        print(f"[FALLBACK] Download Video button found!")
                        break
                if download_video_button:
                    break
            except Exception as e:
                pass
            if i % 5 == 0:
                print(f"[FALLBACK] Still searching... ({i}s)")
            time.sleep(1)
        
        if not download_video_button:
            # Try alternative selector
            try:
                buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Download Video')]")
                if buttons:
                    download_video_button = buttons[0]
                    print("[FALLBACK] Found button via text search")
            except:
                pass
        
        if not download_video_button:
            raise RuntimeError("Download Video button not found after 90 seconds")
        
        # Click the download button
        print("[FALLBACK] Clicking Download Video button...")
        download_video_button.click()
        time.sleep(3)
        
        # Find the actual .mp4 download link
        print("[FALLBACK] Searching for download link...")
        download_link = None
        for i in range(30):
            try:
                links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.mp4'], a[href*='download']")
                for link in links:
                    href = link.get_attribute('href')
                    if href and ('.mp4' in href or 'download' in href) and 'fastvideosave' in href:
                        download_link = href
                        print(f"[FALLBACK] Found download link: {href[:80]}...")
                        break
                if download_link:
                    break
            except Exception as e:
                pass
            if i % 5 == 0:
                print(f"[FALLBACK] Still searching for link... ({i}s)")
            time.sleep(1)
        
        # Fallback: check current URL if it's a direct .mp4
        if not download_link:
            current_url = driver.current_url
            if current_url and '.mp4' in current_url:
                download_link = current_url
                print(f"[FALLBACK] Using current URL: {current_url[:80]}...")
        
        driver.quit()
        driver = None
        
        if not download_link:
            raise RuntimeError("No download link found on page")
        
        # Download the file via requests
        print(f"[FALLBACK] Downloading file via requests...")
        response = requests.get(download_link, stream=True, timeout=120, headers=DEFAULT_HEADERS)
        response.raise_for_status()
        
        filename = f"instagram_{shortcode}.mp4"
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        
        with open(file_path, "wb") as f:
            total_downloaded = 0
            for chunk in response.iter_content(chunk_size=256 * 1024):
                if chunk:
                    f.write(chunk)
                    total_downloaded += len(chunk)
        
        if os.path.exists(file_path) and os.path.getsize(file_path) > 1000:
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"[FALLBACK] ✅ Downloaded: {file_path} ({file_size_mb:.2f} MB)")
            return file_path
        
        raise RuntimeError(f"Downloaded file is empty or too small")
        
    except Exception as e:
        print(f"[FALLBACK] ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

@bot.message_handler(func=lambda message: re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def download_reel_with_caption(message):
    if not check_user_membership(message):
        return

    url = message.text.strip()
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗲𝘀𝘀𝗶𝗴 𝗼𝗿 𝗿𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻......")

    video_url = None
    video_file_path = None
    combined_caption = "\n\n🎥 𝗛𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗲𝗲 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
    use_fallback = False
    fallback_error = None

    # === STEP 1: Try Primary API ===
    try:
        print(f"\n{'='*60}")
        print(f"[PRIMARY] Requesting: {url}")
        api_v2_url = f"https://api.yabes-desu.workers.dev/download/instagram/v2?url={url}"
        response_v2 = requests.get(api_v2_url, timeout=15)
        
        print(f"[PRIMARY] Status: {response_v2.status_code}")
        
        if response_v2.status_code == 200:
            try:
                data_v2 = response_v2.json()
                print(f"[PRIMARY] Response keys: {list(data_v2.keys()) if isinstance(data_v2, dict) else 'Not a dict'}")
                print(f"[PRIMARY] Full response: {data_v2}")
                
                video_url = None
                
                # Check multiple possible response structures
                if (isinstance(data_v2, dict) and 
                    'data' in data_v2 and 
                    isinstance(data_v2['data'], dict) and
                    'url' in data_v2['data'] and 
                    isinstance(data_v2['data']['url'], list) and 
                    len(data_v2['data']['url']) > 0):
                    video_url = data_v2['data']['url'][0]
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                    print(f"[PRIMARY] ✅ Got video via data.url[0]")
                
                elif (isinstance(data_v2, dict) and 
                      'success' in data_v2 and 
                      data_v2.get('success') == True and
                      'url' in data_v2):
                    video_url = data_v2['url']
                    caption_text = data_v2.get('caption') or "No caption available."
                    print(f"[PRIMARY] ✅ Got video via success+url")
                
                elif (isinstance(data_v2, dict) and 'video_url' in data_v2):
                    video_url = data_v2['video_url']
                    caption_text = data_v2.get('caption') or "No caption available."
                    print(f"[PRIMARY] ✅ Got video via video_url")
                
                elif (isinstance(data_v2, dict) and 
                      'data' in data_v2 and 
                      isinstance(data_v2['data'], dict) and
                      'video_url' in data_v2['data']):
                    video_url = data_v2['data']['video_url']
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                    print(f"[PRIMARY] ✅ Got video via data.video_url")
                
                if video_url:
                    # Build caption from primary API
                    if caption_text is None:
                        caption_text = "No caption available."
                    
                    max_caption_length = 500
                    if len(caption_text) > max_caption_length:
                        caption_text = caption_text[:max_caption_length] + "..."
                    
                    footer = "\n\n🎥 𝗲𝗿 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                    combined_caption = f"{caption_text}{footer}"
                    
                    if len(combined_caption) > 1024:
                        caption_text = caption_text[:1024 - len(footer) - 3] + "..."
                        combined_caption = f"{caption_text}{footer}"
                else:
                    print("[PRIMARY] ❌ No valid video URL found in response - triggering fallback")
                    use_fallback = True
                    
            except ValueError as e:
                print(f"[PRIMARY] ❌ JSON decode error: {e} - triggering fallback")
                use_fallback = True
        else:
            print(f"[PRIMARY] ❌ Non-200 status ({response_v2.status_code}) - triggering fallback")
            use_fallback = True
            
    except Exception as e:
        print(f"[PRIMARY] ❌ Exception: {str(e)} - triggering fallback")
        use_fallback = True

    # === STEP 2: Fallback to fastvideosave.net via Selenium ===
    if use_fallback or not video_url:
        print(f"\n{'='*60}")
        print("[FALLBACK] ========== STARTING FALLBACK ==========")
        try:
            video_file_path = download_via_fastvideosave(url)
            if video_file_path and os.path.exists(video_file_path):
                # Use the exact static caption you requested for fallback
                combined_caption = "\n\n🎥 𝗛𝗲𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                print("[FALLBACK] ✅ Successfully downloaded via fastvideosave")
            else:
                print("[FALLBACK] ❌ Failed to download via fastvideosave")
                fallback_error = str(e)
        except Exception as e:
            print(f"[FALLBACK] ❌ Exception: {str(e)}")
            fallback_error = str(e)
            import traceback
            traceback.print_exc()

    # === STEP 3: Final check and send ===
    if not video_url and not video_file_path:
        try:
            bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
        except Exception:
            pass
        
        error_msg = "‼ 𝗙𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗱𝗲𝗼. 𝗹𝗲𝗮𝗲 𝘁𝘆 𝗴𝗮𝗶𝗻 𝗮𝗲𝗿.‼"
        if fallback_error:
            error_msg += f"\n\nDebug: {fallback_error[:200]}"
        
        bot.reply_to(message, error_msg)
        print(f"\n{'='*60}\n")
        return

    # Clean up processing message
    try:
        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
    except Exception:
        pass

    # Send progress message
    progress_msg = bot.reply_to(message, "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗱 ! 𝗗𝗼𝘄𝗹𝗼𝗮𝗱𝗶𝗻 ⤵ ")
    threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

    # Ensure caption is UTF-8 safe
    try:
        combined_caption = combined_caption.encode('utf-8').decode('utf-8')
    except Exception:
        combined_caption = "\n\n🎥 𝗲𝗿 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗹 👀 𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"

    # Send the video (from URL or file)
    try:
        if video_file_path and os.path.exists(video_file_path):
            # Send from local file (fallback method)
            print(f"[SEND] Sending from file: {video_file_path}")
            with open(video_file_path, 'rb') as video_file:
                bot.send_video(message.chat.id, video_file, caption=combined_caption)
            # Clean up downloaded file
            try:
                os.remove(video_file_path)
                print(f"[CLEANUP] Removed: {video_file_path}")
            except:
                pass
        else:
            # Send from URL (primary API method)
            print(f"[SEND] Sending from URL: {video_url[:80]}...")
            bot.send_video(message.chat.id, video_url, caption=combined_caption)
    except Exception as e:
        print(f"[SEND] ❌ Error: {str(e)}")
        bot.reply_to(message, f"⚠️ 𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘃𝗱𝗲𝗼. 𝗘𝗿𝗿𝗼𝗿 : {str(e)}")
        return

    # Ready message
    bot.send_message(
        message.chat.id,
        "𝗜 𝗮𝗺 𝗲𝗮𝗱𝘆 𝗳 𝘆𝗼 𝗻𝗲𝘅𝘁 𝗶𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗻𝗱 𝗮 𝘃𝗹𝗶 𝗜𝘀𝘁𝗮𝗴𝗮𝗺 𝗶𝗲𝗼 / 𝗲𝗲𝗹 𝗹𝗻𝗸, 𝗜 𝘄𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆 👀 \n\n[ 𝗕𝗢 𝗖𝗥𝗔𝗧𝗘𝗗 𝗬 > ー @M_o_Y_zZz ]"
    )
    
    print(f"\n{'='*60}\n")

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

print("="*60)
print("🤖 Bot started successfully")
print(f"Selenium available: {SELENIUM_AVAILABLE}")
print(f"Download directory: {DOWNLOAD_DIR}")
print("="*60)
bot.polling()
