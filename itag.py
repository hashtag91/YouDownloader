from pytube import YouTube
from YouDownloader import Download

url = 'https://www.youtube.com/watch?v=sCLYhoKEqqk'

yt = Download(url)
print(yt.itag())
