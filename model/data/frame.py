from model.data.mp3_data import MP3FrameData
from model.header.mp3_header import MP3Header


class Frame:
    def __init__(self, header: MP3Header, data: MP3FrameData):
        self.header = header
        self.data = data

    def __len__(self):
        return len(self.header) + len(self.data)
