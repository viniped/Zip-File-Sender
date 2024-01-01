import json
import os
from pyrogram import Client
from auto_zip import process_folder
from tqdm import tqdm
from utils import *
from natsort import natsorted

def clear_screen():
    os.system('clear || cls')

def read_caption():
    try:
        with open('caption.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

with open('config.json', 'r') as file:
    config = json.load(file)
channel_id = config['channel_id']

app = Client("user")

def upload_file(file_path, channel_id):
    
    clear_screen()
    with app:        
        def progress(current, total, progress_bar):
            progress_bar.update(current - progress_bar.n)
        if file_path.endswith(('.jpg', '.jpeg', '.png')):
            caption = read_caption()
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                app.send_photo(channel_id, file_path, caption=caption, progress=lambda current, total: progress(current, total, progress_bar))
        else:
            with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Enviando {os.path.basename(file_path)}") as progress_bar:
                app.send_document(channel_id, file_path, progress=lambda current, total: progress(current, total, progress_bar))

def main():
    input_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input")
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")  
    process_folder(input_folder, output_folder, 1900 * (1024 ** 2))  # 1900 MB
    for folder in natsorted(os.listdir(output_folder)):
        folder_path = os.path.join(output_folder, folder)  

        for cover_name in ['cover.jpg', 'cover.png']:
            cover_path = os.path.join(folder_path, cover_name)
            if os.path.exists(cover_path):
                upload_file(cover_path, channel_id)
                break
        for zip_file in natsorted(os.listdir(folder_path)):
            if zip_file.endswith('.zip'):
                upload_file(os.path.join(folder_path, zip_file), channel_id)

        sticker_path = 'sticker.webp'

        if os.path.exists(sticker_path):
            with app:
                app.send_sticker(channel_id, sticker_path)

if __name__ == "__main__":
    show_banner()
    authenticate()
    main()
