import uuid
from uuid import UUID

from tortoise import Model, fields


class YouTubeVideo(Model):
    id = fields.IntField(pk=True)
    youtube_url = fields.CharField(max_length=255)
    telegram_chat_id = fields.IntField()
    telegram_message_id = fields.IntField()

    class Meta:
        table = "videos"
