from functools import lru_cache

import scipy.io.wavfile
from pocket_tts import TTSModel


@lru_cache(maxsize=1)
def load_tts_model():
    return TTSModel.load_model()


def text_to_speech(text, output_filename="output.wav", voice="alba"):
    """
    Converts text to speech using the pocket-tts library and saves it as a WAV file.

    Args:
        text (str): The text to convert to speech.
        output_filename (str, optional): The name of the output WAV file. Defaults to "output.wav".
        voice (str, optional): The voice name to use. Defaults to "alba".
    """

    try:
        model = load_tts_model()
        voice_state = model.get_state_for_audio_prompt(voice)
        audio = model.generate_audio(voice_state, text)
        scipy.io.wavfile.write(output_filename, model.sample_rate, audio.numpy())

        print(f"Successfully converted '{text}' to speech and saved it as '{output_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    my_text = "Hello, this is a test of pocket-tts."
    text_to_speech(my_text)

    my_text2 = "This is another example with a different voice."
    text_to_speech(my_text2, "another_output.wav", "anna")