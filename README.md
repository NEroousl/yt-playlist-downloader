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

## Steps to Resolve the Issues:

1. **Install `ffmpeg`:**
   You need to install `ffmpeg` on your system. Here’s how to do it:

   - **Windows**:
     - Go to the [FFmpeg download page](https://ffmpeg.org/download.html#build-windows) and download the build for Windows.
     - Extract the contents to a folder (e.g., `C:\ffmpeg`).
     - Add `C:\ffmpeg\bin` to your system’s `PATH` environment variable:
       1. Right-click on "This PC" or "My Computer" and select "Properties."
       2. Click "Advanced system settings."
       3. Under the "System Properties" window, click "Environment Variables."
       4. Under "System Variables," find and select the `Path` variable, then click "Edit."
       5. Add `C:\ffmpeg\bin` to the list and click "OK."
   
   - **Mac**:
     ```bash
     brew install ffmpeg
     ```
   - **Linux**:
     On Ubuntu or Debian:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```

2. **Verify the Installation:**
   After installing `ffmpeg`, open a new command prompt (or terminal) and type:
   ```bash
   ffmpeg -version
   ```
   This should show the version of `ffmpeg` installed, confirming that it’s correctly installed.

3. **Re-run the Script:**
   Once `ffmpeg` is installed, you should be able to run the script again without encountering the "merging of multiple formats" error.

