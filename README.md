**Open as administrator** (windows)

To run the script with cookies, follow these steps:

1. **Export Your Cookies:**

   - Use a browser extension (like [EditThisCookie](https://www.editthiscookie.com/) for Chrome or a similar tool for your browser) to export your YouTube cookies. Save the exported cookies to a file named `cookies.txt`.

2. **Place the Cookies File:**

   - Run `python convert_cookies.py`
   - Make sure the `cookies.txt` file is in the same directory as your `download_audio.py` script.
   - If you want to store it in a different location, update the `'cookies': 'cookies.txt'` line in the script with the correct file path.

   **Optional**
   Instead of manually handling cookies, yt-dlp has an option to load cookies from your browser. For example, you can try:
   `yt-dlp --cookies-from-browser chrome "https://www.youtube.com/..."`
   This pulls your session cookies directly from Chrome (or replace chrome with firefox as needed). In a Python script, you might need to modify the options accordingly. Check the yt-dlp documentation for details.

3. **Run the Script as Usual:**
   - Open your terminal (or command prompt) in the directory containing the script and `cookies.txt`.
   - To download a single video's audio, use:
     ```bash
     python download_audio.py "https://www.youtube.com/watch?v=exampleVideoID"
     ```
   - To download the audio for all videos in a playlist, add the `-p` or `--playlist` flag:
     ```bash
     python download_audio.py "https://www.youtube.com/playlist?list=examplePlaylistID" -p
     ```
   - Optionally, you can use the `-o` flag to specify an output directory:
     ```bash
     python download_audio.py "https://www.youtube.com/watch?v=exampleVideoID" -o /path/to/output
     ```

Since the script is already configured to use the cookies file (via `'cookies': 'cookies.txt'`), running it with these commands will automatically use your authenticated cookies for the download process.

That’s it—your script is now ready to run using the cookies you provided.
