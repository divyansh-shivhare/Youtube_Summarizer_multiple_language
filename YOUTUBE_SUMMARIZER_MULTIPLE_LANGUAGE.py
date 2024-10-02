import os

# Install required libraries if not already installed
os.system('pip install googletrans')
os.system('pip install deep-translator')
os.system('pip install youtube-transcript-api')

import googletrans
from deep_translator import GoogleTranslator
from IPython.display import YouTubeVideo
from youtube_transcript_api import YouTubeTranscriptApi

# Function to split text into chunks of max_chars (Google API has a 5000-character limit)
def split_text(text, max_chars=5000):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

# Get the YouTube video link from the user
video = input("Enter the link of your YouTube Video: ")

# Extract the video ID from the URL
id_video = video.split("=")[1]
print(f"Video ID: {id_video}")

YouTubeVideo(id_video)

# Get the transcript of the YouTube video
summary = YouTubeTranscriptApi.get_transcript(id_video)

# Join the list of transcript segments into a single string of text
transcript_text = " ".join([item['text'] for item in summary])

print("CHECK OUT YOUR SOURCE LANGUAGE FROM BELOW:")
print(" ")
langdict = googletrans.LANGUAGES
for i in langdict:
    print(f"{i} - {langdict[i]}")

srclang = input("ENTER LANGUAGE CODE: ")

# Split the transcript text into chunks if it's too long for translation
chunks = split_text(transcript_text)

translated_text = ""
translator = GoogleTranslator(source='auto', target=srclang)

# Translate each chunk and append to the final result
for chunk in chunks:
    # Skip empty or invalid chunks
    if not chunk.strip():
        continue

    try:
        print(f"Translating chunk of size {len(chunk)}")  # Debugging to check the chunk size
        translated_chunk = translator.translate(chunk)
        translated_text += translated_chunk + " "  # Add a space after each translated chunk
    except Exception as e:
        print(f"Error translating chunk: {e}")

print("YOUR TRANSLATED SUMMARY IS GIVEN BELOW:")
print(" ")
print(translated_text)
