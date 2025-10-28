import pygame
import time
import os
import re
import sys

# ANSI color codes for terminal
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"

# Get the folder where this script is located
mypath = os.path.dirname(os.path.abspath(__file__))

# File names
MP3_FILE = os.path.join(mypath, "song1.mp3")
LYRICS_FILE = os.path.join(mypath, "song1.txt")
# Check if files exist
for f in [MP3_FILE, LYRICS_FILE]:
    if not os.path.exists(f):
        print(f"❌ ERROR: File not found -> {f}")
        sys.exit(1)

# Parse lyrics file (ignores timestamps if present)
def parse_lyrics(file_path):
    pattern = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\]\s*(.*)")
    lyrics = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = pattern.match(line)
            if m:
                text = m.group(3)  # ignore time, just keep text
                lyrics.append(text)
            else:
                lyrics.append(line)
    return lyrics

# Animate text letter by letter
def print_animated(text, color=GREEN, speed=0.06):
    print(color, end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print(RESET)

# Display karaoke lyrics with 2-second gap
def karaoke_display(lyrics, gap=2):
    start = time.time()
    previous_lines = []
    for line in lyrics:
        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print last 5 previous lines dimmed
        for pline in previous_lines[-5:]:
            print(DIM + pline + RESET)

        # Print current line animated
        print_animated(line)

        # Save current line
        previous_lines.append(line)

        # Wait gap seconds before next line
        time.sleep(gap)

# Play song and show karaoke
def play_song_with_lyrics(mp3, lyrics_txt):
    # Parse lyrics
    lyrics = parse_lyrics(lyrics_txt)
    if not lyrics:
        print("⚠️ No lyrics found.")
        return

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()

    # Wait 15 seconds before showing lyrics
    time.sleep(15)

    # Show karaoke lyrics with 2-second gap
    karaoke_display(lyrics, gap=1.8)

    # Wait for song to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
    pygame.mixer.quit()
    print("✅ Song finished.")

# Main
if __name__ == "__main__":
    play_song_with_lyrics(MP3_FILE, LYRICS_FILE)
