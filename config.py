#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("27339814"))
API_HASH = getenv("d9edbf2ab27db57c22448d28125d345c")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("5651816564:AAG1CWSnWFcjHy9lRFhMfm5uY8130RrvM-4")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://Admin:Admin@cluster0.cjhcye4.mongodb.net/?retryWrites=true&w=majority)

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "5465891857").split())
)  # Input type must be interger
