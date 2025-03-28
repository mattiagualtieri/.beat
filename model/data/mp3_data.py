class MP3FrameData:
    def __init__(self, data: bytearray):
        self.bytes = data

    def __len__(self):
        return len(self.bytes)
