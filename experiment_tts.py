import os
from pocket_tts import PocketTTS

def text_to_speech(text, output_filename="output.mp3", voice="en-US-Wavenet"):
    """
    Converts text into speech using the pocket-tts library and saves it as an MP3 file.

    Args:
        text (str): The text to convert to speech.
        output_filename (str, optional): The name of the output MP3 file. Defaults to "output.mp3".
        voice (str, optional): The voice to use.  Defaults to "en-US-Wavenet".
    """

    try:
        tts = PocketTTS(voice=voice) #initialize the tts object

        # Convert text to speech
        audio_data = tts.synthesize(text)

        # Save audio data as an MP3 file
        with open(output_filename, "wb") as f:
            f.write(audio_data)

        print(f"Successfully converted '{text}' to speech and saved it as '{output_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    my_text = "Hello, this is a test of pocket-tts."
    text_to_speech(my_text)  # Saves to output.mp3 using the default voice

    my_text2 = "This is another example with a different voice - en-GB-Wavenet"
    text_to_speech(my_text2, "another_output.mp3", "en-GB-Wavenet") # Saves to another_output.mp3 using specified voice