from kokoro import KPipeline
import numpy as np
import soundfile as sf
import io

class text_to_speech:

    def __init__(self):
        self.pipeline = KPipeline(lang_code="a")

    def speak(self, text):
        text = text.replace("**", "")
        text = text.replace("\n", " ")

        generator = self.pipeline(
            text=text,
            voice="af_heart"
        )

        chunks = []

        for _, _, audio in generator:
            chunks.append(audio)

        full_audio = np.concatenate(chunks)

        buffer = io.BytesIO()
        sf.write(buffer, full_audio, 24000, format="WAV")
        buffer.seek(0)

        return buffer