import argparse
import os
import yt_dlp


def download_audio(url, download_playlist, output_dir):
    # Set the output template.
    # For playlists, include a consecutive number prefix.
    if download_playlist:
        outtmpl = f"{output_dir}/%(playlist_index)02d - %(title)s.%(ext)s"
    else:
        outtmpl = f"{output_dir}/%(title)s.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "256",
            }
        ],
        "cookies": "cookies.txt",  # Use your cookies file (ensure it is in Netscape format)
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/100.0.4896.127 Safari/537.36"
            )
        },
    }

    # For a single video, disable playlist mode.
    if not download_playlist:
        ydl_opts["noplaylist"] = True

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading the media: {e}")


def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    parser = argparse.ArgumentParser(
        description="Download audio from YouTube videos or playlists."
    )
    parser.add_argument("url", help="URL of the YouTube video or playlist")
    parser.add_argument(
        "-p",
        "--playlist",
        action="store_true",
        help="Download all videos from the playlist. By default, the script downloads a single video.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=".",
        help="Directory to save the downloaded audio files (default is current directory).",
    )

    args = parser.parse_args()

    # Create the output directory if it doesn't exist.
    os.makedirs(args.output, exist_ok=True)

    download_audio(args.url, args.playlist, args.output)


if __name__ == "__main__":
    main()
