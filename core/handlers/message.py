from aiogram import types, F, Router
from aiogram.types import InputFile, BufferedInputFile
from tortoise.transactions import in_transaction

from app.youtube_download.model import YouTubeVideo
from app.youtube_download.services import download_video, DownloadError


router = Router()


@router.message(F.text.startswith("https"))
async def handle_video(message: types.Message):
    url = message.text

    existing_video = await YouTubeVideo.get_or_none(youtube_url=url)

    if existing_video:
        await message.bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=existing_video.telegram_chat_id,
            message_id=existing_video.telegram_message_id
        )

    else:
        try:
            video_data = await download_video(url)
            video = BufferedInputFile(video_data, filename="video.mp4")
            sent_message = await message.answer_video(video=video)

            async with in_transaction() as conn:
                await YouTubeVideo.create(
                    youtube_url=url,
                    telegram_chat_id=message.chat.id,
                    telegram_message_id=sent_message.message_id
                )
        except DownloadError as e:
            await message.reply(f"Failed to download video: {str(e)}")
        except Exception as e:
            await message.reply(f"An error occurred: {str(e)}")
