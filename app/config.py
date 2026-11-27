import os
from dotenv import load_dotenv

load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
AI_BASE_URL = "https://maas.qianwenaiapi.com/compatible-mode/v1"
AI_MODEL = "qwen3.8-max"