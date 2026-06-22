# MVP Checklist — Coinstack - Gamified Finance Habit Builder

> `coinstack-gamified-finance-habit-builder` · Plaid API (for bank connectivity), Mobile application framework (e.g., React Native, Flutter, iOS Swift/Kotlin Android)

## Features

- [x] **P0** — **Project Environment Setup & Config Loading**
  - *What*: Implement robust environment variable loading using `python-decouple` or similar in `src/core/app.py` and ensure `main.py` passes debug mode correctly. Update `.env.example` to reflect new required variables.
  - *Accept*: Application starts successfully with environment variables configured in .env.
  - *Accept*: DEBUG_MODE setting from .env is correctly reflected in App instance via `app.debug_mode`.
  - *Files*: `main.py`, `src/core/app.py`, `.env.example`, `requirements.txt`

- [ ] **P0** — **Plaid API Client Integration**
  - *What*: Integrate an official Plaid Python client into `src/core/app.py` or a new `src/services/plaid_service.py`. Implement initial client setup using environment variables for `PLAID_CLIENT_ID`, `PLAID_SECRET`, `PLAID_ENV`.
  - *Accept*: Plaid client can be initialized successfully.
  - *Accept*: Plaid client can connect to the specified Plaid environment (e.g., Sandbox).
  - *Files*: `src/core/app.py`, `src/services/plaid_service.py`, `.env.example`, `requirements.txt`
