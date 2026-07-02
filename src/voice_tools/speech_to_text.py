from faster_whisper import WhisperModel


class SpeechToText:

    def __init__(self):
        self.model = WhisperModel(
            "small",
            device="cpu",          # use "cpu" if you don't have NVIDIA GPU
            compute_type="int8"  # use "int8" for CPU
        )

    def transcribe(self, audio_path):

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()