from pytube import YouTube

class Download:
    def __init__(self,url):
        """
        self.itagsData = {17:['144p','3gpp','True'],
                18:['360p','mp4',True],22:['720p','mp4',True],137:['1080p','mp4',False]}
        print(self.itagsData[17])"""
        self.url = url
        self.youtube_video = YouTube(self.url)
        self.streams = self.youtube_video.streams
        self.VideoTitle()
    def VideoTitle(self):
        self.titleText = self.youtube_video.title
        return self.titleText
    def itagList(self):
        itags = self.streams.itag_index
        itagsId = []
        for itag in itags:
            itagsId.append(itag.real)
        return itagsId
    def resList(self):
        uData = []
        resData = []
        for i in self.streams:
            uData.append(str(i).split('"'))
        for b in uData:
            for a in b:
                if a[-2::] == 'pp':
                    pass
                elif a[-1] == 'p':
                    if a not in resData:
                        resData.append(a)
        return resData
    def videoType(self):
        uData = []
        self.typeData = []
        for i in self.streams:
            uData.append(str(i).split('"'))
        for a in uData:
            for b in a:
                if 'video/' in b or 'audio/' in b:
                    if b in self.typeData:
                        pass
                    else:
                        if str(b).split('/')[1] not in self.typeData:
                            self.typeData.append(str(b).split('/')[1])
        return self.typeData
    def resListComplete(self):
        uData = []
        resData = []
        for i in self.streams:
            uData.append(str(i).split('"'))
        for b in uData:
            for a in b:
                if a[-2::] == 'pp':
                    pass
                elif a[-1] == 'p' or a[-3::] == 'bps':
                    resData.append(a)
        return resData
    def videoTypeComplete(self):
        uData = []
        self.typeData = []
        for i in self.streams:
            uData.append(str(i).split('"'))
        for a in uData:
            for b in a:
                if 'video/' in b or 'audio/' in b:
                    if b in self.typeData:
                        pass
                    else:
                        self.typeData.append(str(b).split('/')[1])
        return self.typeData
    def itag(self):
        itagSingle = []
        itagIndexData = []
        for i in range(len(self.itagList())):
            itagSingle = [self.itagList()[i],self.resListComplete()[i],self.videoTypeComplete()[i]]
            itagIndexData.append(itagSingle)
        return itagIndexData