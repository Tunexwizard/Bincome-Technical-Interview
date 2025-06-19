
# Bincom Python Exam Solution (Supabase + Secure)

## Overview

This project analyzes color data and includes:
- Mean, median, mode, variance
- Probability
- Recursive search
- Binary to decimal
- Fibonacci sum
- ✅ Supabase PostgreSQL storage with hidden password

## Files
- `bincom_exam_solution.py`: main script
- `.env`: contains your secret database URL (never upload to GitHub)

## Setup Instructions

1. Install dependencies:
```bash
pip install python-dotenv psycopg2
```

2. Add your Supabase DB password inside `.env`:
```
SUPABASE_DB_URL=postgresql://postgres:yourpassword@aws-0-eu-west-1.pooler.supabase.com:6543/postgres
```

3. Run your script:
```bash
python bincom_exam_solution.py
```

🛡️ Keep `.env` private. Use `.gitignore` to exclude it from version control.
