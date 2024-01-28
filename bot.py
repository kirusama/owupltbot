# from pyrogram import Client, filters
# from pyrogram.types import Message
# import requests

# # Telegram bot token
# API_ID = "1638897"
# API_HASH = "f970b41ffe6560473fd9da2bff560af2"
# BOT_TOKEN = "1646107601:AAGYliNs6gfj6tYf57fEXoFKx9wnOvXXuN0"

# app = Client(
#     "my_bot",
#     api_id=API_ID,
#     api_hash=API_HASH,
#     bot_token=BOT_TOKEN
# )

# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text('Hello! Send me a direct link and I will download and send the file back to you.')

# @app.on_message(filters.text & ~filters.command("start"))
# def handle_message(client, message):
#     text = message.text
#     if text.startswith("http"):
#         file_path = download_file(text)
#         message.reply_document(document=open(file_path, 'rb'))

# def download_file(url: str) -> str:
#     # Download the file
#     response = requests.get(url)
#     filename = url.split("/")[-1]

#     # Save the file
#     with open(filename, "wb") as f:
#         f.write(response.content)

#     return filename

# app.run()

# from pyrogram import Client, filters
# import requests
# import os
# import m3u8
# import mimetypes

# # Telegram bot token
# API_ID = "1638897"
# API_HASH = "f970b41ffe6560473fd9da2bff560af2"
# BOT_TOKEN = "1646107601:AAGYliNs6gfj6tYf57fEXoFKx9wnOvXXuN0"

# app = Client(
#     "my_bot",
#     api_id=API_ID,
#     api_hash=API_HASH,
#     bot_token=BOT_TOKEN
# )

# def download_media_with_progress(url: str, message: 'pyrogram.types.Message') -> str:
#     # Follow redirection to get direct link
#     response = requests.get(url, allow_redirects=True)
#     final_url = response.url

#     # Extract file name from URL
#     file_name = url.split("/")[-1]

#     # Determine media type based on file name extension
#     media_type, _ = mimetypes.guess_type(file_name)
#     if media_type:
#         media_type = media_type.split("/")[0]  # Extract the main type (e.g., "image" from "image/jpeg")
#     else:
#         media_type = "unknown"

#     if media_type == "image":
#         return "photo", final_url
#     elif media_type == "video":
#         return "video", final_url
#     elif media_type == "audio":
#         return "audio", final_url
#     elif media_type == "unknown" and final_url.endswith(".m3u8"):
#         # Download M3U8 playlist
#         playlist = requests.get(final_url).text
#         m3u8_obj = m3u8.loads(playlist)
#         media_urls = [media_segment.uri for media_segment in m3u8_obj.segments]

#         # Send initial message
#         message.reply_text("Downloading media segments...")
        
#         # Download each segment and send progress updates
#         for i, media_url in enumerate(media_urls):
#             download_file(media_url)
#             progress_percentage = ((i + 1) / len(media_urls)) * 100
#             message.reply_text(f"Downloaded {i+1}/{len(media_urls)} segments ({progress_percentage:.2f}% complete)")

#         message.reply_text("Download complete!")
#         return "m3u8", media_urls
#     else:
#         return "unknown", final_url

# def download_file(url: str) -> None:
#     # Download the file
#     response = requests.get(url)
#     filename = url.split("/")[-1]

#     # Save the file
#     with open(filename, "wb") as f:
#         f.write(response.content)

# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text('Hello! Send me a direct link and I will download and send the media back to you.')

# @app.on_message(filters.text & ~filters.command("start"))
# def handle_message(client, message):
#     text = message.text
#     if text.startswith("http"):
#         media_type, media_file = download_media_with_progress(text, message)
#         if media_type == "photo":
#             message.reply_photo(photo=media_file)
#         elif media_type == "video":
#             message.reply_video(video=media_file)
#         elif media_type == "audio":
#             message.reply_audio(audio=media_file)
#         elif media_type == "m3u8":
#             # Reply with downloaded media URLs
#             for url in media_file:
#                 message.reply_text(url)
#         else:
#             message.reply_text("Unknown media type or unsupported file format.")

# app.run()

# import os
# import subprocess
# import requests
# import m3u8
# import mimetypes

# from pyrogram import Client, filters

# # Telegram bot token
# API_ID = "1638897"
# API_HASH = "f970b41ffe6560473fd9da2bff560af2"
# BOT_TOKEN = "1646107601:AAGYliNs6gfj6tYf57fEXoFKx9wnOvXXuN0"

# app = Client(
#     "my_bot",
#     api_id=API_ID,
#     api_hash=API_HASH,
#     bot_token=BOT_TOKEN
# )

# def download_media_with_progress(url: str, message: 'pyrogram.types.Message') -> None:
#     # Follow redirection to get direct link
#     response = requests.get(url, allow_redirects=True)
#     final_url = response.url

#     # Extract file name from URL
#     file_name = url.split("/")[-1]

#     # Determine media type based on file name extension
#     media_type, _ = mimetypes.guess_type(file_name)
#     if media_type:
#         media_type = media_type.split("/")[0]  # Extract the main type (e.g., "image" from "image/jpeg")
#     else:
#         media_type = "unknown"

#     # Create a directory to save the downloaded files
#     os.makedirs("downloads", exist_ok=True)
#     output_file = os.path.join("downloads", file_name)

#     # Download the file using aria2
#     download_file_with_aria2(final_url, output_file)

#     # Send the downloaded file
#     message.reply_document(document=open(output_file, 'rb'))

# def download_file_with_aria2(url: str, output_file: str) -> None:
#     # Call Aria2c to download the file
#     subprocess.run(["aria2c", url, "-o", output_file])

# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text('Hello! Send me a direct link and I will attempt to download and send the file back to you.')

# @app.on_message(filters.text & ~filters.command("start"))
# def handle_message(client, message):
#     text = message.text
#     if text.startswith("http"):
#         download_media_with_progress(text, message)

# app.run()

# filename
import os
import subprocess
import requests
import m3u8
import mimetypes

from pyrogram import Client, filters

# Telegram bot token
API_ID = "1638897"
API_HASH = "f970b41ffe6560473fd9da2bff560af2"
BOT_TOKEN = "1646107601:AAGYliNs6gfj6tYf57fEXoFKx9wnOvXXuN0"

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def download_media_with_progress(url: str, message: 'pyrogram.types.Message') -> None:
    # Follow redirection to get direct link
    response = requests.get(url, allow_redirects=True)
    final_url = response.url

    # Extract file name from URL
    file_name = url.split("/")[-1]

    download_file(url, file_name, message)

def download_file(url: str, filename: str, message: 'pyrogram.types.Message') -> None:
    # Determine media type based on file name extension
    media_type, _ = mimetypes.guess_type(filename)
    if media_type:
        media_type = media_type.split("/")[0]  # Extract the main type (e.g., "image" from "image/jpeg")
    else:
        media_type = "unknown"

    # Create a directory to save the downloaded files
    os.makedirs("downloads", exist_ok=True)
    output_file = os.path.join("downloads", filename)

    # Download the file using aria2
    download_file_with_aria2(url, output_file, message)

def download_file_with_aria2(url: str, output_file: str, message: 'pyrogram.types.Message') -> None:
    # Call Aria2c to download the file
    subprocess.run(["aria2c", url, "-o", output_file])

    # Send the downloaded file
    message.reply_document(document=open(output_file, 'rb'))

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text('Hello! Send me a direct link and I will attempt to download and send the file back to you.')

@app.on_message(filters.regex(r'^[^\s]+$') & ~filters.command("start"))
def handle_message(client, message):
    text = message.text
    if text.startswith("http"):
        download_media_with_progress(text, message)

app.run()
