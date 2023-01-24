#!/usr/bin/python
# encoding: utf-8

import sys
import requests
import os

if not "OPENAI_API_KEY" in os.environ:
    sys.stdout.write("Error: OPENAI_API_KEY not set")
    sys.exit(1)

query = sys.argv[1]

# OpenAI API key
api_key = os.environ["OPENAI_API_KEY"]

# Set the model to use (e.g. "text-davinci-003")
model = "text-davinci-003"

# Set the temperature for the model (values between 0 and 1, higher values will generate more random text)
temperature = 0.5

# Set the max length of the generated text
max_tokens = 500

# Set the top_p value (values between 0 and 1, higher values will generate more likely text)
top_p = 1

# Set the frequency penalty (values between 0 and 1, higher values will generate more diverse text)
frequency_penalty = 0

# Set the presence penalty (values between 0 and 1, higher values will generate more diverse text)
presence_penalty = 0

if query.startswith("code:"):
    query = query.replace("code:", "", 1)
    model = "code-davinci-002"
    temperature = 0
    max_tokens = 300
    presence_penalty = 0

prompt = query

# Make the request to the API
response = requests.post(
    "https://api.openai.com/v1/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "stop": "\n###\n"
    },
)

# Get the generated text from the response
if "choices" in response.json():
    generated_text = response.json()["choices"][0]["text"]
if "choices" not in response.json():
    generated_text = "Error: " + response.json()["error"]["message"]

sys.stdout.write(generated_text)
