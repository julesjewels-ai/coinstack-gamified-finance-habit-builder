# MVP Checklist — Coinstack - Gamified Finance Habit Builder

> `coinstack-gamified-finance-habit-builder` · Plaid API (for bank connectivity), Mobile application framework (e.g., React Native, Flutter, iOS Swift/Kotlin Android)

## Features

- [ ] **P0** — **Project Environment Setup & Config Loading**
  - *What*: Implement robust environment variable loading using `python-decouple` or similar in `src/core/app.py` and ensure `main.py` passes debug mode correctly. Update `.env.example` to reflect new required variables.
  - *Accept*: Application starts successfully with environment variables configured in .env.
  - *Accept*: DEBUG_MODE setting from .env is correctly reflected in App instance via `app.debug_mode`.
  - *Files*: `main.py`, `src/core/app.py`, `.env.example`, `requirements.txt`

- [ ] **P0** — **Plaid API Client Integration**
  - *What*: Integrate an official Plaid Python client into `src/core/app.py` or a new `src/services/plaid_service.py`. Implement initial client setup using environment variables for `PLAID_CLIENT_ID`, `PLAID_SECRET`, `PLAID_ENV`.
  - *Accept*: Plaid client can be initialized successfully.
  - *Accept*: Plaid client can connect to the specified Plaid environment (e.g., Sandbox).
  - *Files*: `src/core/app.py`, `src/services/plaid_service.py`, `.env.example`, `requirements.txt`

- [ ] **P0** — **User & Account Database Models**
  - *What*: Define basic SQLAlchemy (or similar ORM) models for `User` and `BankAccount` (linking to Plaid `item_id` and `access_token`) in a new `src/models/` directory. Initialize database connection in `src/core/app.py`.
  - *Accept*: Database can be initialized and tables created.
  - *Accept*: A new User can be created and saved to the database.
  - *Accept*: A new BankAccount can be created and linked to a User.
  - *Files*: `src/core/app.py`, `src/models/user.py`, `src/models/bank_account.py`, `src/database/database.py`, `requirements.txt`, `.env.example`

- [ ] **P0** — **Plaid Link Flow Integration**
  - *What*: Implement the Plaid Link token creation and public token exchange flow. The app should generate a `link_token` and exchange a `public_token` for an `access_token` and `item_id`, storing them for a user's `BankAccount`.
  - *Accept*: A link_token can be successfully generated via Plaid API.
  - *Accept*: A public_token can be exchanged for an access_token and item_id.
  - *Accept*: The access_token and item_id are securely stored and associated with a user's bank account in the database.
  - *Files*: `src/core/app.py`, `src/services/plaid_service.py`, `src/models/bank_account.py`

- [ ] **P0** — **Initial Transaction Fetching & Storage**
  - *What*: Implement logic to fetch historical transactions for a linked bank account via Plaid's `transactions/get` endpoint and store relevant data (amount, description, date, category) in a `src/models/transaction.py` model.
  - *Accept*: Transactions for a linked account can be fetched from Plaid.
  - *Accept*: Fetched transactions are correctly parsed and saved to the database.
  - *Accept*: Duplicate transactions are handled (e.g., by checking Plaid transaction ID).
  - *Files*: `src/core/app.py`, `src/services/plaid_service.py`, `src/models/transaction.py`

- [ ] **P1** — **Basic Challenge Generation Logic**
  - *What*: Create a `src/challenges/challenge_generator.py` module. Implement basic logic in `src/core/app.py` to select one of the 20 predefined challenges based on simple criteria (e.g., random, or based on a single high-spending category from recent transactions).
  - *Accept*: A challenge can be successfully generated and assigned to a user.
  - *Accept*: The generated challenge is selected from the initial library of 20.
  - *Accept*: Challenges can be viewed by the user.
  - *Files*: `src/core/app.py`, `src/challenges/challenge_generator.py`, `src/models/challenge.py`, `src/models/user_challenge.py`

- [ ] **P1** — **Gamification: Streak Tracking**
  - *What*: Add logic to `src/core/app.py` to track a user's daily challenge streak. Increment streak on successful challenge completion and reset if a daily challenge is missed.
  - *Accept*: User's streak count increases upon challenge completion.
  - *Accept*: Streak resets if a challenge is not completed within a given timeframe (e.g., 24 hours).
  - *Files*: `src/core/app.py`, `src/models/user.py`, `src/models/user_challenge.py`

- [ ] **P1** — **Basic Behavioral Profile Tracking**
  - *What*: Implement a rudimentary behavioral profile in `src/core/app.py` and `src/models/user_profile.py` that tracks aggregated spending by category or overall saving vs. spending ratio.
  - *Accept*: User's spending by category is calculated and stored.
  - *Accept*: A simple spending vs. saving ratio is maintained in the user profile.
  - *Accept*: Profile data updates as new transactions are processed.
  - *Files*: `src/core/app.py`, `src/models/user_profile.py`, `src/models/transaction.py`

- [ ] **P1** — **API Endpoint for User & Challenges**
  - *What*: Set up a lightweight web framework (e.g., Flask or FastAPI) in a new `src/api/` directory. Expose basic endpoints to (1) get user data and their linked accounts, and (2) get the current active challenge and mark it as complete.
  - *Accept*: API server starts successfully.
  - *Accept*: GET /user endpoint returns user and linked account information.
  - *Accept*: GET /challenge endpoint returns the current active challenge for the user.
  - *Accept*: POST /challenge/complete endpoint successfully marks a challenge as complete and updates streak.
  - *Files*: `src/core/app.py`, `src/api/main.py`, `src/api/routes.py`, `requirements.txt`

- [ ] **P2** — **Demo Data Seeder Script**
  - *What*: Create a `scripts/seed_db.py` script that can populate the database with sample users, linked dummy bank accounts (using Plaid Sandbox test credentials), and a few completed challenges for demonstration purposes.
  - *Accept*: Running `python scripts/seed_db.py` populates the database with predefined demo data.
  - *Accept*: Demo users can log in and see their pre-seeded progress.
  - *Accept*: Demo bank accounts show example transactions for challenge generation.
  - *Files*: `scripts/seed_db.py`, `src/models/`, `src/database/database.py`

- [ ] **P2** — **Enhanced CLI for Dev Operations**
  - *What*: Extend `main.py` with additional CLI commands beyond `run` for developers, such as `main.py --seed-db` to run the demo data seeder or `main.py --sync-plaid <user_id>` to manually trigger a Plaid sync for a specific user.
  - *Accept*: CLI command `python main.py --seed-db` successfully seeds the database.
  - *Accept*: CLI command `python main.py --sync-plaid <user_id>` triggers a transaction sync for the specified user.
  - *Files*: `main.py`, `src/core/app.py`, `scripts/seed_db.py`


---
*Generated by jules-idea-automation. Items reference actual project files when available.*
