import yt_dlp
import os
from find import find_audio_files

# Download the audio from a youtube video, save it to output_dir as an .mp3 file and return the filename
def download_audio(video_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    audio_filename = find_audio_files(output_path)[0]

    return audio_filename

# Test run
# filename = download_audio('https://www.youtube.com/watch?v=2y45Vv82Wcg', 'output')
