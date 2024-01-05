import os, shutil
from download import download_audio
from split import split_audio_file
from transcribe import transcribe_audio_files
from summarize import summarize_text

# 
def summarize_youtube_video(youtube_url, outputs_dir):
    raw_audio_dir = f"{outputs_dir}/raw_audio/"
    segments_dir = f"{outputs_dir}/segments"
    transcripts_file = f"{outputs_dir}/transcripts.txt"
    summary_file = f"{outputs_dir}/summary.txt"
    segment_length = 10 * 60  # chunk to 10 min segments
    # Delete the outputs folder and start from scratch
    if os.path.exists(outputs_dir):
        shutil.rmtree(outputs_dir)
        os.mkdir(outputs_dir)
    # Download the video using youtube_dlp
    audio_filename = download_audio(youtube_url, raw_audio_dir)
    # Split each audio file
    chunked_audio_files = split_audio_file(audio_filename, segment_length, segments_dir)
    # Transcribe each splitted audio file using Whisper
    transcriptions = transcribe_audio_files(chunked_audio_files, transcripts_file)
    # Summarize each transcription using chatGPT
    summaries = summarize_text(transcriptions, summary_file)
    # Put the entire summary into a single entry
    final_summary = '\n'.join(summaries)
    # Return the complete summary in text
    return final_summary

youtube_url = 'https://www.youtube.com/watch?v=pGUmiLvBIzk&t=1510s'
outputs_dir = 'outputs/'

summary = summarize_youtube_video(youtube_url, outputs_dir)
print(summary)