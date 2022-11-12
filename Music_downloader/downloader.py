import youtube_dl
import os

def download_ytvid_as_mp3(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url, download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':f'{curr_path}/MyDownloadedMusic/{filename}',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

curr_path = os.getcwd()
print(curr_path)