class MP3Header:
    def __init__(self, raw: bytearray):
        self.raw = raw
        self.mpeg_version = None
        self.layer = None
        self.error_protection = None
        self.bit_rate = None
        self.frequency = None
        self.padding = None
        self.mode = None
        self.mode_extension = None
        self.copyright = None
        self.original = None
        self.emphasis = None

    def __len__(self):
        return 4

    def __str__(self):
        return (f'['
                f'MPEG_VERSION: {self.mpeg_version}, '
                f'LAYER: {self.layer}, '
                f'ERROR_PROTECTION: {self.error_protection}, '
                f'BIT_RATE: {self.bit_rate}, '
                f'FREQUENCY: {self.frequency}, '
                f'PADDING: {self.padding}, '
                f'MODE: {self.mode}, '
                f'MODE_EXTENSION: {self.mode_extension}, '
                f'COPYRIGHT: {self.copyright}, '
                f'ORIGINAL: {self.original}, '
                f'EMPHASIS: {self.emphasis}'
                f']')


class MP3HeaderConstants:
    HEADER_LEN = 4

    SYNC_VALUE = (0xff, 0xe0)
    SYNC_MASK = (0xff, 0xe0)

    MPEG_VERSION_VALUE = {
        0x00: 'MPEG_VERSION_2_5',
        0x08: 'RESERVED',
        0x10: 'MPEG_VERSION_2',
        0x18: 'MPEG_VERSION_1',
    }
    MPEG_VERSION_MASK = 0x18

    LAYER_VALUE = {
        0x00: 'RESERVED',
        0x02: 'LAYER_3',
        0x04: 'LAYER_2',
        0x06: 'LAYER_1',
    }
    LAYER_MASK = 0x06

    ERROR_PROTECTION_VALUE = {
        0x00: 'CRC',
        0x01: 'NO_PROTECTION',
    }
    ERROR_PROTECTION_MASK = 0x01

    BIT_RATE_VALUE = {
        'MPEG_VERSION_1': {
            'LAYER_1': {
                0x00: 'FREE',
                0x10: 32,
                0x20: 64,
                0x30: 96,
                0x40: 128,
                0x50: 160,
                0x60: 192,
                0x70: 224,
                0x80: 256,
                0x90: 288,
                0xa0: 320,
                0xb0: 352,
                0xc0: 384,
                0xd0: 416,
                0xe0: 448,
                0xf0: 'BAD',
            },
            'LAYER_2': {
                0x00: 'FREE',
                0x10: 32,
                0x20: 48,
                0x30: 56,
                0x40: 64,
                0x50: 80,
                0x60: 96,
                0x70: 112,
                0x80: 128,
                0x90: 160,
                0xa0: 192,
                0xb0: 224,
                0xc0: 256,
                0xd0: 320,
                0xe0: 384,
                0xf0: 'BAD',
            },
            'LAYER_3': {
                0x00: 'FREE',
                0x10: 32,
                0x20: 40,
                0x30: 48,
                0x40: 56,
                0x50: 64,
                0x60: 80,
                0x70: 96,
                0x80: 112,
                0x90: 128,
                0xa0: 160,
                0xb0: 192,
                0xc0: 224,
                0xd0: 256,
                0xe0: 320,
                0xf0: 'BAD',
            },
        },
        'MPEG_VERSION_2': {
            'LAYER_1': {
                0x00: 'FREE',
                0x10: 32,
                0x20: 48,
                0x30: 56,
                0x40: 64,
                0x50: 80,
                0x60: 96,
                0x70: 112,
                0x80: 128,
                0x90: 144,
                0xa0: 160,
                0xb0: 176,
                0xc0: 192,
                0xd0: 224,
                0xe0: 256,
                0xf0: 'BAD',
            },
            'LAYER_2': {
                0x00: 'FREE',
                0x10: 8,
                0x20: 16,
                0x30: 24,
                0x40: 32,
                0x50: 40,
                0x60: 48,
                0x70: 56,
                0x80: 64,
                0x90: 80,
                0xa0: 96,
                0xb0: 112,
                0xc0: 128,
                0xd0: 144,
                0xe0: 160,
                0xf0: 'BAD',
            },
            'LAYER_3': {
                0x00: 'FREE',
                0x10: 8,
                0x20: 16,
                0x30: 24,
                0x40: 32,
                0x50: 40,
                0x60: 48,
                0x70: 56,
                0x80: 64,
                0x90: 80,
                0xa0: 96,
                0xb0: 112,
                0xc0: 128,
                0xd0: 144,
                0xe0: 160,
                0xf0: 'BAD',
            },
        },
        'MPEG_VERSION_2_5': {
            'LAYER_1': {
                0x00: 'FREE',
                0x10: 32,
                0x20: 48,
                0x30: 56,
                0x40: 64,
                0x50: 80,
                0x60: 96,
                0x70: 112,
                0x80: 128,
                0x90: 144,
                0xa0: 160,
                0xb0: 176,
                0xc0: 192,
                0xd0: 224,
                0xe0: 256,
                0xf0: 'BAD',
            },
            'LAYER_2': {
                0x00: 'FREE',
                0x10: 8,
                0x20: 16,
                0x30: 24,
                0x40: 32,
                0x50: 40,
                0x60: 48,
                0x70: 56,
                0x80: 64,
                0x90: 80,
                0xa0: 96,
                0xb0: 112,
                0xc0: 128,
                0xd0: 144,
                0xe0: 160,
                0xf0: 'BAD',
            },
            'LAYER_3': {
                0x00: 'FREE',
                0x10: 8,
                0x20: 16,
                0x30: 24,
                0x40: 32,
                0x50: 40,
                0x60: 48,
                0x70: 56,
                0x80: 64,
                0x90: 80,
                0xa0: 96,
                0xb0: 112,
                0xc0: 128,
                0xd0: 144,
                0xe0: 160,
                0xf0: 'BAD',
            },
        },
    }
    BIT_RATE_MASK = 0xf0

    FREQUENCY_VALUE = {
        0x00: 44100,
        0x04: 48000,
        0x08: 32000,
        0x0c: 'RESERVED',
    }
    FREQUENCY_MASK = 0x0c

    PADDING_VALUE = {
        0x00: 'NOT_PADDED',
        0x02: 'PADDED',
    }
    PADDING_MASK = 0x02

    MODE_VALUE = {
        0x00: 'STEREO',
        0x40: 'JOINT_STEREO',
        0x80: 'DUAL',
        0xc0: 'MONO',
    }
    MODE_MASK = 0xc0

    MODE_EXTENSION_VALUE = {
        0x00: 'NO_INTENSITY_NO_MS',
        0x10: 'INTENSITY_NO_MS',
        0x20: 'NO_INTENSITY_MS',
        0x30: 'INTENSITY_MS',
    }
    MODE_EXTENSION_MASK = 0x30

    COPYRIGHT_VALUE = {
        0x00: 'NO_COPYRIGHT',
        0x08: 'COPYRIGHT',
    }
    COPYRIGHT_MASK = 0x08

    ORIGINAL_VALUE = {
        0x00: 'COPY_OF_ORIGINAL',
        0x04: 'ORIGINAL',
    }
    ORIGINAL_MASK = 0x04

    EMPHASIS_VALUE = {
        0x00: 'NONE',
        0x01: '50_15',
        0x02: 'RESERVED',
        0x03: 'CCIT_J_17',
    }
    EMPHASIS_MASK = 0x03
