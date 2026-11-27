from openai import OpenAI

from app import config
from app.schemas import Emotion

client = OpenAI(api_key=config.DASHSCOPE_API_KEY, base_url=config.AI_BASE_URL)

EMOTION_INSTRUCTIONS = {
    Emotion.NEUTRAL: "准确、自然、不带任何情绪色彩地翻译。",
    Emotion.HAPPY: "以开心、热情、友好的语气翻译。",
    Emotion.SAD: "以低落、悲伤的语气翻译。",
    Emotion.ANGRY: "以生气、不满的语气翻译。",
    Emotion.SURPRISED: "以惊讶、意外的语气翻译。",
}

def translate(text: str, emotion: Emotion) -> str:
    complation = client.chat.completions.create(
        model=config.AI_MODEL,
        messages=[
            {
                "role": "system",
                "content": ("你是专业的蒙古语↔中文翻译，服务对象是在中国旅行的蒙古游客，"
                            "场景：旅行、购物、日常聊天。规则："
                            "1. 蒙古语译成中文，中文译成蒙古语。"
                            "2. 中文译文只用汉字；蒙古语译文只用西里尔蒙古文，严禁混用文字。"
                            "3. 忠实原意，不得改变意思，不得添加原文没有的信息（如货币单位、地名）。"
                            "4. 语气按指定风格调整，但意思必须准确。"
                            "5. 选择日常口语中最自然的词。"
                            "6. 只输出译文，不要解释。"
                ) + EMOTION_INSTRUCTIONS[emotion],
            },
            {"role": "user", "content": text},
        ],
        extra_body={"enable_thinking": False},
    )
    return complation.choices[0].message.content