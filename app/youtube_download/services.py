import yt_dlp


class DownloadError(Exception):
    pass


async def download_video(url: str) -> bytes:
    ydl_opts = {
        'format': 'best',
        'outtmpl': '-',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict['url']
            video_data = ydl.urlopen(video_url).read()
        return video_data
    except Exception as e:
        raise DownloadError(f"Error downloading video: {str(e)}")
