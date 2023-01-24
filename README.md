# AlfredGPT
Alfred workflow for generating completion using OpenAI Completion API

Super fast text completion using GPT model. It will perform a request in background and copy completion to the clipboard.

## Usage

Set `OPENAI_API_KEY` in `alfred.py` or in workflow script.

- `gpt text` will copy completion to clipboard and notify user via sound
- `gpt code: text` same, but it will use `code-davinci-002` model

## TODO:
- Write instructions on how to use/setup
- Make it possible to set API key from user input
- More explicitely notify user about an error
