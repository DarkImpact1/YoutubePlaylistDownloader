from pytube import Playlist, YouTube
import os


def availableResolution(main_url):
    url = list(Playlist(main_url).video_urls)[0]
    available_resolutions = []
    video = YouTube(url)
    for stream in video.streams:
        resolution = f"{stream.resolution} {stream.mime_type.split('/')[1]}"
        if resolution not in available_resolutions:
            available_resolutions.append(resolution[:5])
    return list(set(available_resolutions))


def download_playlist(url, path=os.getcwd()):
    playlist = Playlist(url)
    # displaying number of videos in the playlist
    print(f"[+] Number of videos in the playlist: {len(playlist.video_urls)}")
    # asking for confirmation
    confirmation = input("[+] Would you like to continue...? (y/n)\t ").lower()
    avail_reso = availableResolution(url)
    print(f'[+] Available Resolutions are : ', avail_reso)
    resolution = input('Enter the resolution of video (Ex: 720p)\t')
    if confirmation == 'y':
        try:
            num_input = input(
                "[+] Enter the starting point of the playlist from where you want to download the video (leave blank for 0): ")
            # Assign 0 as default if num_input is blank
            num = int(num_input) if num_input.strip().isdigit() else 0
            for index, video_url in enumerate(list(playlist.video_urls)[num:]):
                video = YouTube(video_url)
                print(
                    f"[+] Downloading '{video.title}'........\n[-] Remaining : {len(playlist.video_urls)-(index+num)}")
                # here you can also select opt for the resolution and provide path in download
                video.streams.filter(res=resolution).first().download(
                    path, filename_prefix=(str(num+index)+" "))
            # once all videos are downloaded you'll be notified
            print("[+] Download complete!")
        except Exception as error:
            print(error)
    else:
        print("[-] Download cancelled")


if __name__ == "__main__":
    playlist_url = input("[+] Enter the URL of playlist :-\t")
    path = input(
        "[+] Enter the path where you want to download your videos :-\t")
    download_playlist(playlist_url, path)
