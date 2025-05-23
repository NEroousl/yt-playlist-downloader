import yt_dlp
import os
from tqdm import tqdm

def get_playlist_url():
    return input("Enter the YouTube playlist URL: ")

def choose_quality():
    print("Select the quality (from 144p to 1080p):")
    print("1. 144p\n2. 240p\n3. 360p\n4. 480p\n5. 720p\n6. 1080p")
    choice = input("Enter the number corresponding to the quality: ")
    quality_map = {
        '1': '144p', '2': '240p', '3': '360p',
        '4': '480p', '5': '720p', '6': '1080p'
    }
    return quality_map.get(choice, '1080p')

def get_output_folder():
    output_folder = input("Enter the output folder path: ")
    if not os.path.exists(output_folder):
        print(f"Creating folder: {output_folder}")
        os.makedirs(output_folder)
    return output_folder

def print_download_status(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        percent = d.get('_percent_str', '0.0%').strip()
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r{d['filename']} - {percent} - {downloaded / 1024 / 1024:.2f}MB "
              f"of {total / 1024 / 1024:.2f}MB - Speed: {speed} - ETA: {eta}", end="")
    elif d['status'] == 'finished':
        print(f"\nFinished downloading: {d['filename']}\n")

def get_format_for_quality(quality):
    quality_map = {
        '144p': 144, '240p': 240, '360p': 360,
        '480p': 480, '720p': 720, '1080p': 1080
    }
    target = quality_map.get(quality, 1080)
    return f'bestvideo[height<={target}]+bestaudio/best[height<={target}]'

def download_playlist(url, quality, output_folder):
    ffmpeg_path = os.path.dirname(os.path.abspath(__file__))

    ydl_opts = {
        'format': get_format_for_quality(quality),
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'progress_hooks': [print_download_status],
        'noplaylist': False,
        'quiet': True,
        'no_warnings': True,
        'ffmpeg_location': ffmpeg_path,  # <--- Use local ffmpeg/ffprobe
    }

    try:
        print(f"Downloading playlist from: {url}\n")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"An error occurred: {e}")

def header():
    print(""" 
         __   __         _____      _                             
         ` ` / /__  _   |_   _|   _| |__   ___                    
          ` V / _ `| | | || || | | | '_ ` / _ `                   
           | | (_) | |_| || || |_| | |_) |  __/                   
          _|_|`___/ `__,_||_| `__,_|_.__/ `___/                   
         |  _ `| | __ _ _   _| (_)___| |_                         
         | |_) | |/ _` | | | | | / __| __|                        
         |  __/| | (_| | |_| | | `__ ` |_                         
         |_|__ |_|`__,_|`__, |_|_|___/`__|            _          
         |  _ `  _____  |___/__ __ | | ___   __ _  __| | ___ _ __ 
         | | | |/ _ ` ` /` / / '_ `| |/ _ ` / _` |/ _` |/ _ ` '__| 
         | |_| | (_) ` V  V /| | | | | (_) | (_| | (_| |  __/ |    
         |____/ `___/ `_/`_/ |_| |_|_|`___/ `__,_|`__,_|`___|_|   

    -Malinda Vitharana @NEroousl-
    Download all your favorite videos with ease!
    """)

def main():
    header()
    url = get_playlist_url()
    quality = choose_quality()
    folder = get_output_folder()
    download_playlist(url, quality, folder)

if __name__ == '__main__':
    main()
