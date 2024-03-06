from gtts import gTTS

class TextConverter:
    def __init__(self):
        pass
    def convert(self, text, path, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save(path)