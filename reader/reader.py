from typing import Tuple

from model.data.frame import Frame
from model.data.mp3_data import MP3FrameData
from model.header.mp3_header import MP3HeaderConstants, MP3Header
from model.header.wav_header import WAVHeader, WAVHeaderConstants
from model.sound.sound import Sound


class SoundReader:
    def __init__(self):
        pass

    def read(self, path: str) -> Sound:
        raise NotImplementedError()


class MP3SoundReader(SoundReader):
    def __init__(self):
        super().__init__()

    def read(self, path: str) -> Sound:
        sound = Sound()
        with open(path, 'rb') as file:
            bytes = bytearray(file.read())
            index = 0
            while index < len(bytes):
                if self._is_sync((bytes[index], bytes[index + 1])):
                    header = self._read_header(bytes[index:index + MP3HeaderConstants.HEADER_LEN])
                    index += MP3HeaderConstants.HEADER_LEN
                    frame_length = self._compute_frame_length(header.bit_rate, header.frequency, header.padding, header.error_protection)
                    data = MP3FrameData(bytes[index:index + frame_length - MP3HeaderConstants.HEADER_LEN])
                    index += frame_length - MP3HeaderConstants.HEADER_LEN
                    sound.add_frame(Frame(header, data))
                else:
                    index += 1

        print(f'Loaded {len(sound)} frames from {path}')
        return sound

    @staticmethod
    def _is_sync(bytes: Tuple[int, int]) -> bool:
        return (bytes[0] & MP3HeaderConstants.SYNC_MASK[0] == MP3HeaderConstants.SYNC_VALUE[0]
                and bytes[1] & MP3HeaderConstants.SYNC_MASK[1] == MP3HeaderConstants.SYNC_VALUE[1])

    @staticmethod
    def _read_header(bytes: bytearray) -> MP3Header:
        header = MP3Header(bytes)
        header.mpeg_version = MP3HeaderConstants.MPEG_VERSION_VALUE[bytes[1] & MP3HeaderConstants.MPEG_VERSION_MASK]
        header.layer = MP3HeaderConstants.LAYER_VALUE[bytes[1] & MP3HeaderConstants.LAYER_MASK]
        header.error_protection = MP3HeaderConstants.ERROR_PROTECTION_VALUE[bytes[1] & MP3HeaderConstants.ERROR_PROTECTION_MASK]
        header.bit_rate = MP3HeaderConstants.BIT_RATE_VALUE[header.mpeg_version][header.layer][bytes[2] & MP3HeaderConstants.BIT_RATE_MASK]
        header.frequency = MP3HeaderConstants.FREQUENCY_VALUE[bytes[2] & MP3HeaderConstants.FREQUENCY_MASK]
        header.padding = MP3HeaderConstants.PADDING_VALUE[bytes[2] & MP3HeaderConstants.PADDING_MASK]
        header.mode = MP3HeaderConstants.MODE_VALUE[bytes[3] & MP3HeaderConstants.MODE_MASK]
        header.mode_extension = MP3HeaderConstants.MODE_EXTENSION_VALUE[bytes[3] & MP3HeaderConstants.MODE_EXTENSION_MASK]
        header.copyright = MP3HeaderConstants.COPYRIGHT_VALUE[bytes[3] & MP3HeaderConstants.COPYRIGHT_MASK]
        header.original = MP3HeaderConstants.ORIGINAL_VALUE[bytes[3] & MP3HeaderConstants.ORIGINAL_MASK]
        header.emphasis = MP3HeaderConstants.EMPHASIS_VALUE[bytes[3] & MP3HeaderConstants.EMPHASIS_MASK]
        return header

    @staticmethod
    def _compute_frame_length(bit_rate: int, frequency: int, padding: str, error_protection: str) -> int:
        pad = 1 if padding == 'PADDED' else 0
        crc = 2 if error_protection == 'CRC' else 0
        return int((144 * bit_rate * 1000 / frequency) + pad + crc)


class WAVSoundReader(SoundReader):
    def __init__(self):
        super().__init__()

    def read(self, path: str) -> Sound:
        sound = Sound()
        with open(path, 'rb') as file:
            bytes = bytearray(file.read())
            header = self._read_header(bytes, 0)
            print(header)

        print(f'Loaded {len(sound)} frames from {path}')
        return sound

    @staticmethod
    def _read_header(bytes: bytearray, index: int) -> WAVHeader:
        header = WAVHeader(bytes)
        header.riff = bytes[index:index + WAVHeaderConstants.RIFF_LEN]
        index += WAVHeaderConstants.RIFF_LEN
        header.size = int.from_bytes(bytes[index:index + WAVHeaderConstants.SIZE_LEN], 'little')
        index += WAVHeaderConstants.SIZE_LEN
        header.wave = bytes[index:index + WAVHeaderConstants.WAVE_LEN]
        index += WAVHeaderConstants.WAVE_LEN

        header.fmt = bytes[index:index + WAVHeaderConstants.FMT_LEN]
        index += WAVHeaderConstants.FMT_LEN
        header.fmt_len = int.from_bytes(bytes[index:index + WAVHeaderConstants.FMT_SIZE_LEN], 'little')
        index += WAVHeaderConstants.FMT_SIZE_LEN
        header.format_type = int.from_bytes(bytes[index:index + WAVHeaderConstants.FORMAT_TYPE_LEN], 'little')
        index += WAVHeaderConstants.FORMAT_TYPE_LEN
        header.channels = int.from_bytes(bytes[index:index + WAVHeaderConstants.CHANNELS_LEN], 'little')
        index += WAVHeaderConstants.CHANNELS_LEN
        header.frequency = int.from_bytes(bytes[index:index + WAVHeaderConstants.FREQUENCY_LEN], 'little')
        index += WAVHeaderConstants.FREQUENCY_LEN
        header.byte_rate = int.from_bytes(bytes[index:index + WAVHeaderConstants.BYTE_RATE_LEN], 'little')
        index += WAVHeaderConstants.BYTE_RATE_LEN
        header.block_align = int.from_bytes(bytes[index:index + WAVHeaderConstants.BLOCK_ALIGN_LEN], 'little')
        index += WAVHeaderConstants.BLOCK_ALIGN_LEN
        header.bits_per_sample = int.from_bytes(bytes[index:index + WAVHeaderConstants.BITS_PER_SAMPLE_LEN], 'little')
        index += WAVHeaderConstants.BITS_PER_SAMPLE_LEN

        header.data = bytes[index:index + WAVHeaderConstants.DATA_LEN]
        index += WAVHeaderConstants.DATA_LEN
        header.data_len = int.from_bytes(bytes[index:index + WAVHeaderConstants.DATA_SIZE_LEN], 'little')

        return header


if __name__ == '__main__':
    reader = WAVSoundReader()
    sound = reader.read('../input/addf8-mulaw-GW.wav')

    # with open('../output/test.mp3', 'wb') as file:
    #     for i in range(len(sound)):
    #         file.write(sound.frames[i].header.raw)
    #         file.write(sound.frames[i].data.bytes)
