# YouTube Playlist Downloader

A Python-based tool to download YouTube playlists in various video quality options. The program handles connection interruptions and will pause/resume the download when the internet connection is restored.

## Features
- Download YouTube playlists with ease.
- Select video quality from 144p to 1080p.
- Handles internet connection interruptions by pausing the download until the connection is restored.
- Displays download progress with speed and percentage.

## Requirements
- Python 3.x
- `yt-dlp` library (a powerful YouTube downloader)
- `tqdm` library (for progress bars)

### To install the required libraries, run:

```bash
pip install yt-dlp tqdm
```

## How to Use

1. **Clone the Repository:**
    Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/yt-playlist-downloader.git
    ```

2. **Run the Script:**
    Navigate to the project folder and run the script:

    ```bash
    python download_playlist.py
    ```

3. **Enter Playlist URL:**
    The script will prompt you to enter the YouTube playlist URL.

4. **Choose Quality:**
    Select the video quality from 144p to 1080p.

5. **Select Output Folder:**
    Choose or create an output folder to store the downloaded videos.

6. **Download:**
    The program will download the playlist and display the download progress. If the internet connection is lost, the program will pause and resume once the connection is restored.
