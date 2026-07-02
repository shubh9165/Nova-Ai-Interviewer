from kokoro import KPipeline
import sounddevice as sd
import numpy as np

class text_to_speech:

    def __init__(self):
        self.pipeline = KPipeline(lang_code="a")

    def speak(self, text):
            # Remove markdown
        text = text.replace("**", "")

        # Replace newlines with spaces
        text = text.replace("\n", " ")

        print(repr(text))
        generator = self.pipeline(text=text, voice="af_heart")

        chunks = []

        for i, (gs, ps, audio) in enumerate(generator):
            chunks.append(audio)

        #print("Total chunks:", len(chunks))

        full_audio = np.concatenate(chunks)

        sd.play(full_audio, 24000)
        sd.wait()