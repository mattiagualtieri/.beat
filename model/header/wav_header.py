class WAVHeader:
    def __init__(self, raw: bytearray):
        self.raw = raw
        self.riff = None
        self.size = None
        self.wave = None
        self.fmt = None
        self.fmt_len = None
        self.format_type = None
        self.channels = None
        self.frequency = None
        self.byte_rate = None
        self.mode_extension = None
        self.bits_per_sample = None
        self.data = None
        self.data_len = None

    def __len__(self):
        return 44

    def __str__(self):
        return (f'['
                f'RIFF: {self.riff}, '
                f'SIZE: {self.size}, '
                f'WAVE: {self.wave}, '
                f'FMT: {self.fmt}, '
                f'FMT_LEN: {self.fmt_len}, '
                f'FORMAT_TYPE: {self.format_type}, '
                f'CHANNELS: {self.channels}, '
                f'FREQUENCY: {self.frequency}, '
                f'BYTE_RATE: {self.byte_rate}, '
                f'MODE_EXTENSION: {self.mode_extension}, '
                f'BITS_PER_SAMPLE: {self.bits_per_sample}, '
                f'DATA: {self.data}, '
                f'DATA_LEN: {self.data_len}'
                f']')


class WAVHeaderConstants:
    HEADER_LEN = 44

    RIFF_LEN = 4
    RIFF_VALUE = bytearray([82, 73, 70, 70])
    SIZE_LEN = 4
    WAVE_LEN = 4
    WAVE_VALUE = bytearray([87, 65, 86, 69])

    FMT_LEN = 4
    FMT_VALUE = bytearray([102, 109, 116, 32])
    FMT_SIZE_LEN = 4
    FORMAT_TYPE_LEN = 2
    CHANNELS_LEN = 2
    FREQUENCY_LEN = 4
    BYTE_RATE_LEN = 4
    BLOCK_ALIGN_LEN = 2
    BITS_PER_SAMPLE_LEN = 2

    DATA_LEN = 4
    DATA_VALUE = bytearray([100, 97, 116, 97])
    DATA_SIZE_LEN = 4
