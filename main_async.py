"""import json
import os
import asyncio
from pyrogram import Client
from auto_zip import process_folder
from tqdm import tqdm
from utils import *
import uvloop

async def clear_screen():
    await asyncio.to_thread(os.system, 'clear || cls')

async def read_caption():
    try:
        with open('caption.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

async def upload_file(app, file_path, channel_id):
    await clear_screen()
    async with app:
        async def progress(current, total, progress_bar):
            progress_bar.update(current - progress_bar.n)

        if file_path.endswith(('.jpg', '.jpeg', '.png')):
            caption = await read_caption()
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                await app.send_photo(channel_id, file_path, caption=caption, progress=lambda current, total: progress(current, total, progress_bar))
        else:
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                await app.send_document(channel_id, file_path, progress=lambda current, total: progress(current, total, progress_bar))

async def main():
    with open('config.json', 'r') as file:
        config = json.load(file)
    channel_id = config['channel_id']

    app = Client("user")
    
    input_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input")
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    process_folder(input_folder, output_folder, 1900 * (1024 ** 2))  # 1900 MB
    for folder in sorted(os.listdir(output_folder)):
        folder_path = os.path.join(output_folder, folder)

        for cover_name in ['cover.jpg', 'cover.png']:
            cover_path = os.path.join(folder_path, cover_name)
            if os.path.exists(cover_path):
                await upload_file(app, cover_path, channel_id)
                break
        for zip_file in sorted(os.listdir(folder_path)):
            if zip_file.endswith('.zip'):
                await upload_file(app, os.path.join(folder_path, zip_file), channel_id)

        sticker_path = 'sticker.webp'
        if os.path.exists(sticker_path):
            async with app:
                await app.send_sticker(channel_id, sticker_path)

if __name__ == "__main__":
    show_banner()
    authenticate()
    uvloop.install()
    asyncio.run(main())
"""


import json
import os
import asyncio
from pyrogram import Client
from auto_zip import process_folder
from tqdm import tqdm
from utils import *
import uvloop
from natsort import natsorted  # Importe a função natsorted

async def clear_screen():
    await asyncio.to_thread(os.system, 'clear || cls')

async def read_caption():
    try:
        with open('caption.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

async def upload_file(app, file_path, channel_id):
    await clear_screen()
    async with app:
        async def progress(current, total, progress_bar):
            progress_bar.update(current - progress_bar.n)

        if file_path.endswith(('.jpg', '.jpeg', '.png')):
            caption = await read_caption()
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                await app.send_photo(channel_id, file_path, caption=caption, progress=lambda current, total: progress(current, total, progress_bar))
        else:
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                await app.send_document(channel_id, file_path, progress=lambda current, total: progress(current, total, progress_bar))

async def main():
    with open('config.json', 'r') as file:
        config = json.load(file)
    channel_id = config['channel_id']

    app = Client("user")
    
    input_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input")
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    process_folder(input_folder, output_folder, 1900 * (1024 ** 2))  # 1900 MB
    for folder in natsorted(os.listdir(output_folder)):  # Use natsorted para ordenar os nomes de pasta
        folder_path = os.path.join(output_folder, folder)

        for cover_name in ['cover.jpg', 'cover.png']:
            cover_path = os.path.join(folder_path, cover_name)
            if os.path.exists(cover_path):
                await upload_file(app, cover_path, channel_id)
                break
        for zip_file in natsorted(os.listdir(folder_path)):  # Use natsorted para ordenar os arquivos ZIP
            if zip_file.endswith('.zip'):
                await upload_file(app, os.path.join(folder_path, zip_file), channel_id)

        sticker_path = 'sticker.webp'
        if os.path.exists(sticker_path):
            async with app:
                await app.send_sticker(channel_id, sticker_path)

if __name__ == "__main__":
    show_banner()
    authenticate()
    uvloop.install()
    asyncio.run(main())

