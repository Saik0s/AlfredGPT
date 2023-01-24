#!/usr/bin/python
# encoding: utf-8

import sys
import os
import json
import urllib.request

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
data = json.dumps({
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "stop": "\n###\n"
    }).encode("utf-8")
req = urllib.request.Request("https://api.openai.com/v1/completions", data=data, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    }, method='POST')

response = urllib.request.urlopen(req)

# Get the generated text from the response
response_text = json.loads(response.read())
if "choices" in response_text:
    generated_text = response_text["choices"][0]["text"]
if "choices" not in response_text:
    generated_text = "Error: " + response_text["error"]["message"]

sys.stdout.write(generated_text)
