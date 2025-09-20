# README

## LLM API Basic Scripts

This repository demonstrates the basics of working with multiple Large Language Model (LLM) providers. It shows how to send requests to different models in both streaming and non-streaming modes.

### Supported providers

- Anthropic (Claude)
- Azure OpenAI
- Google Gemini
- Mistral
- OpenAI

---

## Structure

- `anthropic/` → examples with Claude models
- `azure_open_ai/` → examples with Azure-hosted OpenAI models
- `google/` → examples with Gemini models
- `mistral/` → examples with Mistral models
- `open_ai/` → examples with OpenAI models
- `.env.example` → template for environment variables

Each provider directory contains scripts for:

- **Streaming responses** (real-time output)
- **Non-streaming responses** (full output returned at once)

---

## Setup

1. Clone the repository.

2. Create a Python virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On Linux/macOS:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows (PowerShell):

     ```bash
     .venv\Scripts\Activate.ps1
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and fill in your API keys.

---

## requirements

```
anthropic
openai
mistralai
google-genai
python-dotenv
```

## Credits

Examples inspired by and adapted from official SDK documentation of:

- OpenAI
- Azure OpenAI
- Anthropic
- Google Generative AI
- Mistral

---
