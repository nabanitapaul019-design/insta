import telebot
import requests
import threading
import time
import re
import os
import shutil
from urllib.parse import quote

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
    print("[INFO] ✅ Selenium imported successfully")
except ImportError as e:
    SELENIUM_AVAILABLE = False
    print(f"[WARNING] ❌ Selenium not available: {e}")

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

# === RAILWAY-SPECIFIC: Detect Chrome path ===
def get_chrome_path():
    """Get Chromium path for various environments including Railway."""
    # Check environment variable first
    if os.environ.get('CHROME_BIN') and os.path.exists(os.environ['CHROME_BIN']):
        return os.environ['CHROME_BIN']
    
    # Common paths for different Linux distros
    paths = [
        '/usr/bin/chromium',           # Debian/Ubuntu (Railway)
        '/usr/bin/chromium-browser',   # Ubuntu
        '/usr/bin/google-chrome',      # Chrome
        '/usr/bin/google-chrome-stable',
        '/snap/bin/chromium',          # Snap
        '/snap/bin/chromium-browser',
    ]
    
    for path in paths:
        if os.path.exists(path):
            return path
    
    # Fallback: use shutil.which
    chrome = shutil.which('chromium') or shutil.which('chromium-browser') or shutil.which('google-chrome')
    if chrome:
        return chrome
    
    return None

CHROME_PATH = get_chrome_path()
if CHROME_PATH:
    os.environ['CHROME_BIN'] = CHROME_PATH
    print(f"[INFO] ✅ Chrome detected at: {CHROME_PATH}")
else:
    print(f"[WARNING] ❌ Chrome NOT found - fallback will fail without it")

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

def _extract_instagram_shortcode(url: str):
    """Extract Instagram shortcode from URL."""
    match = re.search(r"instagram\.com/(?:reel|reels|p|tv)/(?P<shortcode>[A-Za-z0-9_\-]+)", url, re.IGNORECASE)
    if match:
        return match.group("shortcode")
    return None

def _create_fallback_driver(download_path=None):
    """Create headless Chrome driver - Railway optimized."""
    if not SELENIUM_AVAILABLE:
        print("[FALLBACK] ❌ Selenium not available")
        return None
    
    if not CHROME_PATH:
        print("[FALLBACK] ❌ Chrome binary not found")
        return None
    
    try:
        if download_path:
            os.makedirs(download_path, exist_ok=True)
            download_path = os.path.abspath(download_path)
        else:
            download_path = DOWNLOAD_DIR
            os.makedirs(download_path, exist_ok=True)
        
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')  # Required for Docker/Railway
        chrome_options.add_argument('--disable-dev-shm-usage')  # Required for Docker/Railway
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Set binary location EXPLICITLY
        chrome_options.binary_location = CHROME_PATH
        print(f"[FALLBACK] Using Chrome binary: {CHROME_PATH}")
        
        prefs = {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        # Use webdriver-manager for ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        print("[FALLBACK] Initializing Chrome driver...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(300)
        driver.set_script_timeout(300)
        
        print(f"[FALLBACK] ✅ Driver created successfully")
        return driver
        
    except Exception as e:
        print(f"[FALLBACK] ❌ Driver creation error: {e}")
        import traceback
        traceback.print_exc()
        return None

def download_via_fastvideosave(url: str) -> str:
    """Fallback: Download Instagram video via fastvideosave.net using Selenium."""
    if not SELENIUM_AVAILABLE:
        raise RuntimeError("Selenium is not installed")
    
    if not CHROME_PATH:
        raise RuntimeError("Chrome browser not found - cannot use Selenium fallback")
    
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
        
        driver = _create_fallback_driver()
        if not driver:
            raise RuntimeError("Failed to create browser driver")
        
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
        
        # Click Download button
        print("[FALLBACK] Clicking Download button...")
        download_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        download_button.click()
        time.sleep(2)
        
        # Wait for "Download Video" button
        print("[FALLBACK] Waiting for Download Video button...")
        download_video_button = None
        for i in range(90):
            try:
                # Try multiple selectors
                selectors = [
                    "button svg path[d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4m4-5 5 5 5-5m-5 5V3']",
                    "//button[contains(text(), 'Download Video')]",
                    "button[data-testid='download-video']",
                    "a[href*='download'][href*='.mp4']"
                ]
                
                for selector in selectors:
                    try:
                        if selector.startswith('//'):
                            elements = driver.find_elements(By.XPATH, selector)
                        else:
                            elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        
                        for elem in elements:
                            if "Download Video".lower() in elem.text.lower() or elem.tag_name == 'a':
                                download_video_button = elem if elem.tag_name == 'button' else elem.find_element(By.XPATH, "./ancestor::button")
                                break
                        if download_video_button:
                            break
                    except:
                        continue
                
                if download_video_button:
                    print(f"[FALLBACK] ✅ Download Video button found!")
                    break
            except Exception:
                pass
            
            if i % 10 == 0 and i > 0:
                print(f"[FALLBACK] Still searching... ({i}s)")
            time.sleep(1)
        
        if not download_video_button:
            raise RuntimeError("Download Video button not found after 90 seconds")
        
        # Click and wait for download link
        print("[FALLBACK] Clicking Download Video button...")
        download_video_button.click()
        time.sleep(3)
        
        # Find the actual .mp4 download link
        print("[FALLBACK] Searching for download link...")
        download_link = None
        for i in range(30):
            try:
                links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.mp4']")
                for link in links:
                    href = link.get_attribute('href')
                    if href and '.mp4' in href:
                        download_link = href
                        print(f"[FALLBACK] ✅ Found download link")
                        break
                if download_link:
                    break
            except:
                pass
            time.sleep(1)
        
        # Fallback: check current URL
        if not download_link:
            current_url = driver.current_url
            if current_url and '.mp4' in current_url:
                download_link = current_url
        
        if driver:
            driver.quit()
            driver = None
        
        if not download_link:
            raise RuntimeError("No download link found")
        
        # Download the file via requests
        print(f"[FALLBACK] Downloading file...")
        response = requests.get(download_link, stream=True, timeout=120, headers=DEFAULT_HEADERS)
        response.raise_for_status()
        
        filename = f"instagram_{shortcode}.mp4"
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=256 * 1024):
                if chunk:
                    f.write(chunk)
        
        if os.path.exists(file_path) and os.path.getsize(file_path) > 1000:
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"[FALLBACK] ✅ Downloaded: {file_path} ({file_size_mb:.2f} MB)")
            return file_path
        
        raise RuntimeError("Downloaded file is empty")
        
    except Exception as e:
        print(f"[FALLBACK] ❌ Error: {e}")
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
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻𝗸......")

    video_url = None
    video_file_path = None
    combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
    use_fallback = False

    # === STEP 1: Try Primary API ===
    try:
        api_v2_url = f"https://api.yabes-desu.workers.dev/download/instagram/v2?url={url}"
        response_v2 = requests.get(api_v2_url, timeout=15)
        
        if response_v2.status_code == 200:
            try:
                data_v2 = response_v2.json()
                video_url = None
                
                # Check multiple response structures
                if (isinstance(data_v2, dict) and 'data' in data_v2 and isinstance(data_v2['data'], dict) and
                    'url' in data_v2['data'] and isinstance(data_v2['data']['url'], list) and len(data_v2['data']['url']) > 0):
                    video_url = data_v2['data']['url'][0]
                    caption_text = data_v2['data'].get('caption') or "No caption available."
                
                elif (isinstance(data_v2, dict) and 'success' in data_v2 and data_v2.get('success') == True and 'url' in data_v2):
                    video_url = data_v2['url']
                    caption_text = data_v2.get('caption') or "No caption available."
                
                elif isinstance(data_v2, dict) and 'video_url' in data_v2:
                    video_url = data_v2['video_url']
                    caption_text = data_v2.get('caption') or "No caption available."
                
                if video_url:
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
                    use_fallback = True
            except:
                use_fallback = True
        else:
            use_fallback = True
    except:
        use_fallback = True

    # === STEP 2: Fallback ===
    if use_fallback or not video_url:
        print("[FALLBACK] Attempting fastvideosave.net...")
        try:
            if CHROME_PATH:
                video_file_path = download_via_fastvideosave(url)
                if video_file_path:
                    combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
            else:
                print("[FALLBACK] ❌ Chrome not available for Selenium fallback")
        except Exception as e:
            print(f"[FALLBACK] ❌ Exception: {e}")

    # === STEP 3: Send ===
    if not video_url and not video_file_path:
        try:
            bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
        except:
            pass
        bot.reply_to(message, "‼ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 𝗹𝗮𝘁𝗲𝗿.‼")
        return

    try:
        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
    except:
        pass

    progress_msg = bot.reply_to(message, "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗻𝗱 ! 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ⤵ ")
    threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

    try:
        combined_caption = combined_caption.encode('utf-8').decode('utf-8')
    except:
        combined_caption = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"

    try:
        if video_file_path and os.path.exists(video_file_path):
            with open(video_file_path, 'rb') as video_file:
                bot.send_video(message.chat.id, video_file, caption=combined_caption)
            try:
                os.remove(video_file_path)
            except:
                pass
        else:
            bot.send_video(message.chat.id, video_url, caption=combined_caption)
    except Exception as e:
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘃𝗶𝗱𝗲𝗼. 𝗘𝗿𝗿𝗼𝗿 : {str(e)}")
        return

    bot.send_message(
        message.chat.id,
        "𝗜 𝗮𝗺 𝗿𝗲𝗮𝗱𝘆 𝗳𝗼 𝘆𝗼 𝗻𝗲𝘅𝘁 𝘃𝗶𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝘂 👀 \n\n[ 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
    )

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

print("="*60)
print("🤖 Bot started")
print(f"Selenium: {SELENIUM_AVAILABLE}")
print(f"Chrome: {CHROME_PATH or 'NOT FOUND'}")
print("="*60)
bot.polling()
