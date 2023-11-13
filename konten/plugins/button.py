# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
            InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink2),
	],
	[
           InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink),
            ],
	[
           InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [           
            [
                InlineKeyboardButton(text="JOIN 1", url=client.invitelink),
                InlineKeyboardButton(text="JOIN 2", url=client.invitelink2),
            ],
[
           InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ", url=client.invitelink2),
            ],
[
           InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ", url=client.invitelink),
            ],
[
            InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink2),
            ],
[
           InlineKeyboardButton("JOIN VIP", url=f"https://t.me/vip4646neverdie"),
        ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
