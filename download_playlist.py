import yt_dlp
import os

# Function to ask for a valid URL
def get_playlist_url():
    url = input("Enter the YouTube playlist URL: ")
    return url

# Function to choose the quality
def choose_quality():
    print("Select the quality (from 144p to 1080p):")
    print("1. 144p")
    print("2. 240p")
    print("3. 360p")
    print("4. 480p")
    print("5. 720p")
    print("6. 1080p")
    
    choice = input("Enter the number corresponding to the quality: ")
    quality_map = {
        '1': '144p',
        '2': '240p',
        '3': '360p',
        '4': '480p',
        '5': '720p',
        '6': '1080p'
    }
    
    return quality_map.get(choice, '1080p')  # Default to 1080p if invalid choice

# Function to get the output folder
def get_output_folder():
    output_folder = input("Enter the output folder path: ")
    
    # Ensure the folder exists
    if not os.path.exists(output_folder):
        print(f"Creating folder: {output_folder}")
        os.makedirs(output_folder)
    
    return output_folder

# Function to ask if user wants .mp4 format
def ask_for_mp4():
    choice = input("Do you want to download the video in .mp4 format? (y/n): ").strip().lower()
    return choice == 'y'

# Progress hook to show download status
def print_download_status(d):
    if d['status'] == 'downloading':
        # Calculate the progress as a percentage
        percent = d.get('_percent_str', '0.0%')  # Using .get() to avoid KeyError
        speed = d.get('_speed_str', 'N/A')  # Using .get() to avoid KeyError
        size = d.get('downloaded_bytes', 0)    # Downloaded bytes

        # Convert downloaded size to MB
        size_mb = size / 1_048_576  # 1 MB = 1,048,576 bytes

        # Print status with downloaded size in MB
        print(f"\r{d['filename']} - {percent} - {size_mb:.2f} MB - {speed}", end="")


    elif d['status'] == 'finished':
        print(f"\nFinished downloading: {d['filename']}")

# Function to download the playlist
def download_playlist(url, quality, output_folder, force_mp4):
    if force_mp4:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio
            'outtmpl': os.path.join(output_folder, '%(title)s.mp4'),  # Force MP4 extension
            'progress_hooks': [print_download_status],
        }
    else:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'progress_hooks': [print_download_status],
        }

    # Start the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading playlist from: {url}")
        ydl.download([url])

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
                                                                  
""")
    print("\n            -Malinda Vitharana @NEroousl-")
    print("    Download all your favorite videos with ease!  \n\n")

# Main function to orchestrate the download
def main():
    header()
    url = get_playlist_url()
    quality = choose_quality()
    output_folder = get_output_folder()
    force_mp4 = ask_for_mp4()
    
    download_playlist(url, quality, output_folder, force_mp4)

if __name__ == '__main__':
    main()


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
                                                                  
""")
    print("\n            -Malinda Vitharana @NEroousl-")
    print("    Download all your favorite videos with ease!  \n\n")

# Main function to orchestrate the download
def main():
    header()
    url = get_playlist_url()
    quality = choose_quality()
    output_folder = get_output_folder()
    download_playlist(url, quality, output_folder)

if __name__ == '__main__':
    main()
