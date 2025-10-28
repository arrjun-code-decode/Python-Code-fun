
### 🎵 **Description — Karaoke Lyrics Player (Python + Pygame)**

This Python script is a **terminal-based karaoke player** that plays an MP3 song while displaying its lyrics line by line — with smooth animation and color effects for a dynamic karaoke experience.

---

### 🧠 **How It Works**

1. **Imports Required Modules**
   Uses `pygame` for audio playback, `time` for delays, `os` and `sys` for file handling, and `re` for parsing lyric timestamps.

2. **File Setup**

   * Looks for two files in the same folder:

     * `song1.mp3` — the audio file
     * `song1.txt` — the lyrics file
   * If either file is missing, the program exits with an error message.

3. **Lyrics Parsing**
   The function `parse_lyrics()` reads the lyrics file and removes any timestamps like `[00:45.23]`, keeping only the text lines for display.

4. **Animated Text Display**
   The function `print_animated()` prints each character of the current lyric line with a slight delay, creating a **typing animation** effect in green color.

5. **Karaoke Display**
   The `karaoke_display()` function:

   * Clears the terminal before each new line
   * Shows the last 5 lines dimmed (as a lyric history)
   * Displays the current line with animation
   * Waits a short gap before showing the next line

6. **Music Playback**
   The function `play_song_with_lyrics()`:

   * Initializes `pygame.mixer`
   * Plays the MP3 file
   * Waits 15 seconds (for intro music)
   * Starts showing the lyrics in sync with the song
   * Keeps running until the music finishes

---

### ⚙️ **Main Features**

* 🎶 Plays MP3 audio using `pygame.mixer`
* 📝 Reads and animates lyrics from a `.txt` file
* 🌈 Uses **ANSI color codes** for colorful terminal output
* 🕒 Optional timestamp handling (auto ignored)
* 💡 Displays previous lines dimmed for karaoke effect

---

### 🧩 **Requirements**

* Python 3.x
* `pygame` library (`pip install pygame`)
* `song1.mp3` and `song1.txt` in the same directory

---

### 🚀 **Usage**

Run the script:

```bash
python play_song_with_lyrics.py
```

The song starts playing, and after 15 seconds, the lyrics appear line by line like a karaoke screen.

---
