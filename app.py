from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        problem = request.form["problem"]

        prompt = create_prompt(problem)

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        result = response.output_text

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)