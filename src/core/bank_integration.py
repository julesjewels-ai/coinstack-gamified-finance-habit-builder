from src.core.models import Transaction
from typing import List
from datetime import datetime, timedelta
import random

class BankIntegrationSimulator:
    def __init__(self):
        self.connected = False

    def connect_account(self, user_id: str) -> bool:
        """Simulates connecting to a bank account via Plaid or similar API."""
        print(f"Simulating connection to bank account for user {user_id}...")
        self.connected = True
        return True

    def fetch_recent_transactions(self, user_id: str, days: int = 30) -> List[Transaction]:
        """Simulates fetching recent transactions."""
        if not self.connected:
            raise Exception("Bank account not connected. Call connect_account first.")

        print(f"Fetching transactions for the last {days} days...")
        transactions = []
        now = datetime.now()

        categories = ["Food & Drink", "Subscriptions", "Groceries", "Entertainment", "Shopping", "Transport"]
        merchants = ["Starbucks", "Netflix", "Whole Foods", "AMC Theatres", "Amazon", "Uber"]

        for i in range(10):  # Generate 10 random transactions
            days_ago = random.randint(1, days)
            amount = round(random.uniform(5.0, 150.0), 2)
            category = random.choice(categories)
            merchant = random.choice(merchants)

            transactions.append(
                Transaction(
                    id=f"txn_{i}",
                    amount=amount,
                    merchant_name=merchant,
                    category=category,
                    date=now - timedelta(days=days_ago)
                )
            )

        # Sort by date descending
        transactions.sort(key=lambda t: t.date, reverse=True)
        return transactions
