from pytube import YouTube

class Download:
    def __init__(self,url):
        self.url = url
        self.youtube_video = YouTube(self.url)
        self.streams = self.youtube_video.streams
        self.VideoTitle()
    def VideoTitle(self):
        self.titleText = self.youtube_video.title
        return self.titleText
    def itagList(self):
        itags = self.streams.itag_index
        for i in itags:
            print(i.real)

yt = Download("https://www.youtube.com/watch?v=RmyUEEUFU3o")
yt.itagList()