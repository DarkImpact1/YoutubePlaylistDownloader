from pytube import Playlist,YouTube


def download_playlist(url):
    playlist = Playlist(url)
    # displaying number of videos in the playlist
    print(f"[+] Number of videos in the playlist: {len(playlist.video_urls)}")
    # asking for confirmation 
    confirmation = input("[+] Would you like to continue...? (y/n)").lower()
    if confirmation == 'y':
        try:
            for video_url in playlist.video_urls:
                video = YouTube(video_url)
                print(f"[+] Downloading '{video.title}'...")
                # here you can also select opt for the resolution and provide path in download
                video.streams.get_highest_resolution().download("F:\Machine_learning")
            
            # once all videos are downloaded you'll be notified
            print("[+] Download complete!")
        except Exception as error:
            print(error)
    else:
        print("[-] Download cancelled")

if __name__=="__main__":
    playlist_url =  input("[+] Enter the URL of playlist :- \t")
    download_playlist(playlist_url)