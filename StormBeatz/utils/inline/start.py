#
# Copyright (C) 2021-2022 by StormBeatz@Github, < https://github.com/StormBeatz >.
#
# This file is part of < https://github.com/StormBeatz/StormBeatz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/StormBeatz/StormBeatz/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="📚 All Commands", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="Dev", url="https://t.me/kassim_darlzzz"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="Updates", url="https://t.me/LoveofmusicUpdates"
            ),
            InlineKeyboardButton(
                text="Support", url="https://t.me/loveofmusic"
            ),                       
        ],        
        [
            InlineKeyboardButton(
                text="owner", url="https://t.me/LoCaL_kInG_01"
            ),                                  
        ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to your group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="Updates", url=f"https://t.me/loveofmusicUpdates"),
            InlineKeyboardButton(
                text="Support", url=f"https://t.me/loveofmusicSupport"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🏳️‍🌈 Language", callback_data="LG"
                )
        ],
        [
            InlineKeyboardButton(
                text="owner", url="https://t.me/LoCaL_kInG_01"
            )
        ]
     ]
    return buttons
