from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()  # Load environment variables from .env file

agent = Agent(
    'groq:openai/llama-3.3-70b-versatile',
    instructions='You are a helpful assistant that gives concise answers.'
)

result = agent.run_sync('What is PydanticAI and why should I use it?')
print(result.output)


print(result.output)           # The actual response text
print(result.usage)            # Token counts — input, output
print(result.all_messages())   # Full conversation history

""""""

agent = Agent(
    'groq:openai/llama-3.3-70b-versatile',
    instructions="""You are CodeBuddy, a senior Python developer.
    You explain code concepts using real-world analogies.
    You always suggest best practices.
    Keep responses under 200 words."""
)

result = agent.run_sync('Explain what a decorator is in Python')
print(result.output)