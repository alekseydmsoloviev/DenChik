# Telegram Mantra Bot

This project implements a simple Telegram bot that guides a user through a short Socratic dialog and generates a personal mantra. Answers and mantras are stored in a PostgreSQL database. The GPT-4 call is currently stubbed and the bot returns a predefined mantra without contacting OpenAI.


## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with the following variables:

```bash
BOT_TOKEN=<telegram token>
# OPENAI_API_KEY=<openai key>  # optional, stub mantra used if empty
DATABASE_URL=postgresql://user:pass@localhost/db
```

3. Initialize the database schema:

```bash
psql -f schema.sql
```

4. Run migrations:

```bash
alembic upgrade head
```

5. Start the bot:

```bash
python bot/main.py
```

## Project Structure

See `minimal_spec_for_codex.md` for the full specification.
