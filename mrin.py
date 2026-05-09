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
BOT_LIST = "https://t.me/MRiNxDiLDOS/92"
OWNER_URL = "https://t.me/MrinMoYxCB"
OWNER_IDS = {2007860433}
CHANNEL_URL = "https://t.me/mrinxdildos"

# Define the required channel
required_channel = '@MRiNxDiLDOS'

# Delete existing webhook before polling
bot.remove_webhook()

# Function to delete message after delay
def delete_after_delay(chat_id, message_id):
    time.sleep(9)
    bot.delete_message(chat_id, message_id)

def check_user_membership(message):
    try:
        user_status = bot.get_chat_member(REQUIRED_CHANNEL, message.from_user.id).status
        if user_status not in ["member", "administrator", "creator"]:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL)
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦 | ➖]", url=BOT_LIST)
            )
            user_id = message.from_user.id
            try:
                photos = bot.get_user_profile_photos(user_id)
                has_photo = photos.total_count > 0
            except Exception:
                has_photo = False
            caption = f"🚨𝗛𝗜 👋 *{message.from_user.first_name}*\n‼ 𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 !\n🔒 *Join our official channel to use this bot!* 🔒"
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
            telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL)
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
    button1 = telebot.types.InlineKeyboardButton(text="[➖ 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥 ➖]", url=OWNER_URL)
    button2 = telebot.types.InlineKeyboardButton(text="[➖ 𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ➖]", url=CHANNEL_URL)
    button3 = telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦 | ➖]", url=BOT_LIST)
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    welcome_text = (
        "𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗘𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧\n"
        "📎 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀 !\n"
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
    notify_text = f"👤 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗛𝗔𝗦 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗢𝗨𝗥 𝗕𝗢𝗧\n 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: {user_name}\n 𝗨𝗦𝗘𝗥 𝗜𝗗: {message.from_user.id}"
    for owner_id in OWNER_IDS:
        if owner_id != message.from_user.id:  # Don't notify if owner starts the bot
            try:
                bot.send_message(owner_id, notify_text)
            except Exception as e:
                print(f"Failed to notify owner {owner_id}: {e}")

# Regular expression to check if the message is a valid Instagram URL
def is_instagram_url(url):
    instagram_url_pattern = r"^(https?://)?(www\.)?instagram\.com/.*$"
    return re.match(instagram_url_pattern, url) is not None

@bot.message_handler(func=lambda message: re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def download_reel_with_caption(message):
    # Check membership
    if not check_user_membership(message):
        return

    url = message.text.strip()
    # Send the processing message instantly
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻𝗸......")

    try:
        # Fetch video URL, caption, username, and type using the NEW API
        # Note: The URL needs to be properly encoded. We'll remove any trailing spaces or extra characters.
        clean_url = url.strip()
        api_url = f"https://insta-api.mrinmoy.workers.dev/?url={clean_url}"
        response = requests.get(api_url)

        # Debug log for API response
        print(f"API Response: {response.status_code}, {response.text}")

        if response.status_code == 200:
            data = response.json()

            # Check if the API returned success
            if data.get("status") == "success":
                # Extract data from the new API response structure
                video_url = data.get("download_url")
                thumbnail_url = data.get("thumbnail")
                channel_name = data.get("channel_name", "@UnknownChannel") # Use default if not found


                caption = f"Downloaded via {channel_name}"

                # Validate the video URL
                if not video_url:
                    bot.reply_to(message, "‼️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗠𝗶𝘀𝘀𝗶𝗻𝗴 𝗼𝗿 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝘃𝗶𝗱𝗲𝗼 𝗨𝗥𝗟.‼️")
                    return

                # Truncate caption to fit within Telegram's character limit (1024)
                max_caption_length = 1024
                if len(caption) > max_caption_length:
                    caption = caption[:max_caption_length - 3] + "..."

                # Construct the final caption with the desired format
                footer = (
                    f"🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️"
                )
                combined_caption = f"{caption}{footer}"

                # Ensure combined caption does not exceed 1024 characters
                if len(combined_caption) > 1024:
                    # Further truncate the caption to fit within the limit
                    caption = caption[:1024 - len(footer) - 3] + "..."  # Reserve space for footer and ellipsis
                    combined_caption = f"{caption}{footer}"

                # Debug log for combined caption
                print(f"Combined Caption: {combined_caption}")

                # Delete the processing message
                try:
                    bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
                except Exception:
                    pass

                # Send the progress message when the video is found
                progress_msg = bot.reply_to(message, "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗻𝗱 ! 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ⤵️")
                threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

                # Encode combined caption to UTF-8 to avoid encoding issues
                try:
                    combined_caption = combined_caption.encode('utf-8').decode('utf-8')
                except Exception as e:
                    print(f"Encoding error: {str(e)}")
                    combined_caption = "No caption available.\n\n•     💀 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 : Unknown\n\n🎥 Here is your requested Reel 👀 provided by @instra_dwn_bymrin_bot ❤️"

                # Send video with caption
                try:
                    bot.send_video(message.chat.id, video_url, caption=combined_caption)
                except Exception as e:
                    bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘃𝗶𝗱𝗲𝗼. 𝗘𝗿𝗿𝗼𝗿: {str(e)}")
                    return

                # Notify the user that the bot is ready for the next request
                bot.send_message(
                    message.chat.id,
                    "𝗜 𝗮𝗺 𝗿𝗲𝗮𝗱𝘆 𝗳𝗼𝗿 𝘆𝗼𝘂 𝗻𝗲𝘅𝘁 𝘃𝗶𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀\n[ 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
                )
            else:
                # Handle API failure
                error_msg = data.get("error", "Unknown error from API.")
                bot.reply_to(message, f"‼️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗔𝗣𝗜 𝗲𝗿𝗿𝗼𝗿: {error_msg}‼️")
        else:
            bot.reply_to(message, f"‼️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗔𝗣𝗜 𝘀𝘁𝗮𝘁𝘂𝘀: {response.status_code}‼️")
    except requests.RequestException as e:
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘁𝗼 𝗦𝗲𝗿𝘃𝗲𝗿 ⚠️ : {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 ⚠️ : {str(e)}")

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

bot.polling()