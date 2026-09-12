"""
مزودو AI المتاحون
"""

from .gemini import GeminiProvider

# لإضافة مزودين جدد لاحقاً:
# from .claude import ClaudeProvider
# from .openai import OpenAIProvider

PROVIDERS = {
    "gemini": GeminiProvider,
    # "claude": ClaudeProvider,
    # "openai": OpenAIProvider,
}


def get_provider(name, api_key):
    """يعيد المزود المطلوب"""
    if name not in PROVIDERS:
        raise ValueError(f"مزود غير معروف: {name}")
    return PROVIDERS[name](api_key)
