from model.data.frame import Frame


class Sound:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame: Frame):
        self.frames.append(frame)

    def __len__(self):
        return len(self.frames)
