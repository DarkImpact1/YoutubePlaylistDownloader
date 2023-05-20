
# YoutubePlaylistDownloader

This Python script allows you to download videos from a YouTube playlist using the pytube library. It provides a command-line interface that prompts the user to enter the URL of the playlist and the path where they want to save the downloaded videos of desired resolution.


## Requirements
- Python 3.x
- pytube library 


## Installation

you can run it on termux as well as in linux distribution.
#### for termux and linux
```bash
  apt-get update && apt-get upgrade
  apt install git
  git clone https://github.com/DarkImpact1/YoutubePlaylistDownloader.git
  python3 main.py
```
#### for windows
```bash
  pip install git
  install using pip install pytube
  git clone https://github.com/DarkImpact1/YoutubePlaylistDownloader.git
  python3 main.py
```
## Features
- Downloads all the videos in a YouTube playlist by just pasting link of playlist.
- Allows the user to specify the starting point in the playlist.
- Downloads videos in the highest available resolution.
- Provides progress updates during the download process.

## Usage
- Clone the repository or download the script file.
- Open a terminal or command prompt and navigate to the directory where the script is located.
- Run the script using the command python playlist_downloader.py.
- Enter the URL of the playlist when prompted.
- Enter the path where you want to save the downloaded videos.
- Confirm the download and select the resoltion as well as optionally specify the starting point in the playlist.
- Sit back and let the script download the videos for you!
- Once the download is complete, you will be notified.

### Note: 
The script downloads videos one at a time, so it may take a while depending on the number of videos in the playlist and your internet connection speed.
