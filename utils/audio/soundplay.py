import playsound

class SoundPlayer:
    """
    A class for playing sound files.
    """

    def __init__(self):
        pass

    def play(self, soundfile: str):
        """
        Plays a sound file.

        Args:
            soundfile (str): The path to the sound file.

        Returns:
            None
        """
        playsound.playsound(soundfile)
