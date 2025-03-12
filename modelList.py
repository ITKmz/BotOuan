import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

models = openai.models.list()
for model in models:
    print(model.id)

# output:
# gpt-4.5-preview
# gpt-4.5-preview-2025-02-27
# gpt-4o-mini-2024-07-18
# gpt-4o-mini-audio-preview-2024-12-17
# dall-e-3
# dall-e-2
# gpt-4o-audio-preview-2024-10-01     
# gpt-4o-audio-preview
# o1-mini-2024-09-12
# o1-mini
# omni-moderation-latest
# gpt-4o-mini-audio-preview
# omni-moderation-2024-09-26
# whisper-1
# babbage-002
# tts-1-hd-1106
# text-embedding-3-large
# gpt-4o-2024-05-13
# tts-1-hd
# o1-preview
# o1-preview-2024-09-12
# gpt-4o-2024-11-20
# gpt-3.5-turbo-instruct-0914
# gpt-4o-mini-search-preview
# tts-1-1106
# davinci-002
# gpt-3.5-turbo-1106
# gpt-4o-search-preview
# gpt-3.5-turbo-instruct
# gpt-4o-mini-search-preview-2025-03-11
# gpt-3.5-turbo-0125
# gpt-4o-2024-08-06
# gpt-3.5-turbo
# gpt-3.5-turbo-16k
# gpt-4o
# text-embedding-3-small
# text-embedding-ada-002
# gpt-4o-mini
# gpt-4o-search-preview-2025-03-11
# tts-1