# Minimal Spec for Telegram Mantra Bot (for Codex)

## Dependencies
Create a `requirements.txt`:
```
aiogram==3.0.0
openai==0.27.0
SQLAlchemy==2.0.15
psycopg2-binary==2.9.6
python-dotenv==1.0.0
alembic==1.13.0
```

## Project Structure
```
telegram-mantra-bot/
├── bot/
│   ├── main.py
│   ├── handlers/
│   │   ├── start.py
│   │   ├── selection.py
│   │   ├── socratic.py
│   │   ├── gpt.py
│   │   └── reminders.py
│   ├── keyboards.py
│   └── config.py
├── models.py
├── schema.sql
├── .env
└── README.md
```

## Database Schema (`schema.sql`)
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL
);
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title TEXT,
    current_step INTEGER DEFAULT 1
);
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics(id),
    question_index INTEGER,
    answer_text TEXT
);
CREATE TABLE mantras (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics(id),
    text TEXT,
    step_index INTEGER
);
CREATE TABLE reminders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    mantra_id INTEGER REFERENCES mantras(id),
    remind_at TIMESTAMP,
    sent BOOLEAN DEFAULT FALSE
);
```

## Key Flows & Handlers

1. **/start** → `start.py`  
   - Send welcome message with inline buttons:
     - ✍️ Да, у меня есть запрос → callback `has_request`
     - 🔎 Хочу сначала разобраться… → callback `explore_inside`

2. **has_request** → `selection.py`  
   - Present text or voice:
     - 🆓 Написать текстом → callback `request_text`
     - 💬 Голосом (подписка) → callback `enable_voice`

3. **explore_inside** → `selection.py`  
   - Send diagnostic intro + button 🧭 Пройти самодиагностику → `start_diag`

4. **Socratic Dialog** → `socratic.py`  
   - Ask 5–7 predefined questions (hardcoded list).  
   - Store answers in `answers` table.

5. **GPT Integration** → `gpt.py`  
   - On completion of answers: compile prompt using three-act structure and wrap with prefixes/suffixes.  
   - Call OpenAI GPT-4 API, save result as a new `mantra` (step_index = current_step).

6. **Reminders** → `reminders.py`  
   - After saving mantra: schedule a reminder record for `NOW() + INTERVAL '24 hours'`.  
   - Periodic job (simple loop or `asyncio.sleep`) checks due reminders, sends message with buttons:
     - ✅ Продолжить → `next_step`
     - 🔄 Пропустить → `skip_step`
     - ❓ Маршрут → `roadmap`

## Config (`.env`)
```
BOT_TOKEN=<telegram token>
OPENAI_API_KEY=<openai key>
DATABASE_URL=postgresql://user:pass@localhost/db
```

## README.md
Include:
- How to set up `.env`
- Initialize DB: `psql -f schema.sql`
- Run bot: `python bot/main.py`

---

**Instruction to Codex:**  
Generate the full project according to this spec, implementing handlers, database models using SQLAlchemy, Alembic migrations, and scheduling reminders in code. No tests or CI required. Ensure the bot responds and persists data correctly.
