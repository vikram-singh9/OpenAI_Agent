import os 
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel


load_dotenv()

gemini_Api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_Api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider,

)

agent = Agent(
    name = "Greet Agent",
    instructions = "You are Greet AI, a simple and friendly chatbot that speaks on behalf of Vikram.",
    model = model,
     

)
while True:
    user = input("Enter your prompt: ")
    result = Runner.run_sync(agent, user)
    print(result.final_output)
    print("Do you want to ask another question? (yes/no)")
    if input().lower() != "yes":
        print("Goodbye!")
        break


    dffdfdfdfdfsa