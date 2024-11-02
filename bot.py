import sys
from pyrogram import Client, enums
from fsub.config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_,
    LOGGER,
    BOT_TOKEN,
    BUTTON_ROW,
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=BUTTON_ROW,
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"BOT_TOKEN detected!\n"
                f"Username: @{self.username}\n\n"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti."
            )
            sys.exit()

        for key, channel_id in FORCE_SUB_.items():
            try:
                info = await self.get_chat(channel_id)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(channel_id)
                    link = info.invite_link
                setattr(self, f"invitelink{key}", link)
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_{key} Detected!\n"
                    f"Title: {info.title}\n"
                    f"Chat ID: {info.id}\n\n"
                )
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} "
                    f"menjadi Admin di FORCE_SUB_{key}\n\n"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Bot Aktif!\n\n", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_DB Detected!\n"
                f"Title: {db_channel.title}\n"
                f"Chat ID: {db_channel.id}\n\n"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda\n"
                f"CHANNEL_ID Saat Ini: {CHANNEL_ID}\n\n"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti."
            )
            sys.exit()

        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
