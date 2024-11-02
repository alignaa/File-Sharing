from fsub.config import FORCE_SUB_, BUTTON_ROW
from pyrogram.types import InlineKeyboardButton
from pyrogram import enums

async def start_button(client):
    if not FORCE_SUB_:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons

    dynamic_button = []
    current_row = []
    for key in FORCE_SUB_.keys():
        chat_id = FORCE_SUB_[key]
        chat = await client.get_chat(chat_id)
        chat_type = (
            "ɢʀᴏᴜᴘ"
            if chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]
            else "ᴄʜᴀɴɴᴇʟꜱ"
        )
        name = chat_type
        current_row.append(InlineKeyboardButton(text=name, url=getattr(client, f'invitelink{key}')))
        if len(current_row) == BUTTON_ROW:
            dynamic_button.append(current_row)
            current_row = []

    if current_row:
        dynamic_button.append(current_row)

    buttons = [
        [
            InlineKeyboardButton(text="ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
        ],
    ] + dynamic_button + [
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons

async def fsub_button(client, message):
    if FORCE_SUB_:
        dynamic_button = []
        current_row = []
        for key in FORCE_SUB_.keys():
            chat_id = FORCE_SUB_[key]
            chat = await client.get_chat(chat_id)
            chat_type = (
                "ɢʀᴏᴜᴘ"
                if chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]
                else "ᴄʜᴀɴɴᴇʟꜱ"
                )
            name = chat_type
            current_row.append(InlineKeyboardButton(text=name, url=getattr(client, f'invitelink{key}')))
            if len(current_row) == BUTTON_ROW:
                dynamic_button.append(current_row)
                current_row = []

        if current_row:
            dynamic_button.append(current_row)
            
        try:
            dynamic_button.append(
                [
                    InlineKeyboardButton(text="ᴄᴏʙᴀ ʟᴀɢɪ", url=f"https://t.me/{client.username}?start={message.command[1]}"),
                ]
            )
        except IndexError:
            pass

        return dynamic_button
