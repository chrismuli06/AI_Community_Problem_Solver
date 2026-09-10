# AI Community Problem-Solving Assistant

## Project Description

The AI Community Problem-Solving Assistant is a web-based application that uses Artificial Intelligence to help community members analyze problems and develop practical solutions.

## Problem

Community members often face problems but may not know how to identify the causes, understand the effects, compare possible solutions, or create practical action plans.

## Objective

To develop an AI-powered assistant that uses prompt engineering and a Large Language Model (LLM) to analyze community problems and generate structured, realistic solutions and action plans.

## Target Users

- Community members
- Students
- Youth groups
- Community organizations

## Main Features

- Identifies possible causes of a community problem
- Explains effects on the community
- Generates practical solutions
- Recommends the best solution
- Creates a 30-day action plan
- Provides affordable and realistic recommendations

## Technologies Used

- Python
- Flask
- HTML
- CSS
- OpenAI API
- Prompt Engineering

## How It Works

1. The user enters a community problem through the web interface.
2. Flask receives the problem.
3. Python creates an engineered prompt.
4. The prompt is sent to the OpenAI API.
5. The AI analyzes the problem.
6. The result is returned to the Flask application.
7. The analysis is displayed on the webpage.

## Example Problem

Youth unemployment is increasing in my community.

The assistant analyzes the problem and provides possible causes, effects, practical solutions, a recommended solution, and a 30-day action plan.

## Project Structure

- app.py - Flask web application
- prompt_engine.py - AI prompt and analysis logic
- templates/index.html - Web interface
- project_objective.txt - Project objectives and information
- .gitignore - Files excluded from Git

## Security

The OpenAI API key is stored as an environment variable and is not included in the GitHub repository.

## Author

Chris



