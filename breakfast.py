
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
# 1. Set API Key & Initialize Model
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model.
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=1,
)

# Define what "healthy" means and constrain the output.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a nutrition-conscious breakfast assistant.

Recommend exactly 5 healthy breakfast ideas for a typical adult.

For this task, healthy means:
- Include protein and fiber where practical.
- Prefer whole grains, fruits, vegetables, nuts, or seeds.
- Limit added sugar and highly processed ingredients.
- Suggest balanced, practical meals.

Output rules:
- Number the ideas from 1 to 5.
- Use exactly one line per idea.
- Do not include a title, introduction, or conclusion.
- Keep each idea concise.
"""
    ),
    (
        "human",
        "Suggest 5 healthy breakfast ideas."
    ),
])

# Build the LangChain chain and invoke it.
chain = prompt | llm
response = chain.invoke({})

# Print only the generated text.
print(response.content)