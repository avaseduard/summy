from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()

# Get your OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Create the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Transcribe the audio files of the video
def transcribe_audio_files(audio_files, output_file=None):
    transcripts = []
    # Loop through each audio file
    for audio_file in audio_files:
        # Open the audio file in binary mode
        audio = open(audio_file, 'rb')
        # Use OpenAI API to transcribe the audio using Whisper
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio, 
            response_format="text"
          )
        # Append the transcribed text to the transcripts list
        transcripts.append(transcript)

    # If an output file is specified, save all transcripts to a .txt file
    if output_file is not None:
        with open(output_file, 'w') as file:
            for transcript in transcripts:
                file.write(transcript + '\n')
    # Return the list of transcripts
    return transcripts

# Test run
# transcribe_audio_files(['segments/segment_0.mp3'], 'text_file')