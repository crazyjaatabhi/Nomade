# ==========================================================
# Group Manager Bot
# Author: learningbots79 (https://github.com/learningbots79)
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ==========================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("4202458936", 0))
API_HASH = os.getenv("1a413a1530d4202458936bb0c7c92d8a", "")
BOT_TOKEN = os.getenv("8238269712:AAGR4MMqrBXnHfb3gWC1IBsz336f_UPXmrs", "")
MONGO_URI = os.getenv("mongodb+srv://crazyjaatabhi_86: crazyjaatabhi_86@crazyjaatabhi.wbikzkk.mongodb.net/?appName=crazyjaatabhi", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("8418386439", 0))
BOT_USERNAME = os.getenv("@Atanki_bot", "NomadeHelpBot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/atankigodfather")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/atankigod")
START_IMAGE = os.getenv("START_IMAGE", "https://graph.org/file/5cf6daecfbbccc395e745-4e238d8a5fa04921a0.jpg")
