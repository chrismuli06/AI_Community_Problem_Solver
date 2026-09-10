import os
from openai import OpenAI


def create_prompt(problem):
    prompt = f"""
Act as a community development advisor.

Analyze the following community problem:

{problem}

Provide:

1. Three possible causes.
2. Three effects on the community.
3. Five practical solutions.
4. The best recommended solution and explain why.
5. A 30-day action plan.

Keep the recommendations affordable, realistic,
and suitable for a local community.
"""

    return prompt


# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Ask the user for a community problem
problem = input("Enter a community problem: ")


# Create the engineered prompt
prompt = create_prompt(problem)


# Send the prompt to the AI
response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)


# Display the AI's answer
print("\nAI COMMUNITY PROBLEM ANALYSIS")
print("==============================")
print(response.output_text)