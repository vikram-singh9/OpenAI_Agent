import os 
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_Api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_Api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai",
),

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider,

)