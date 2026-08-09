import pytest
from src.core.models import UserProfile, BehavioralProfile, Transaction, Challenge
from src.core.bank_integration import BankIntegrationSimulator
from src.core.challenge_library import ChallengeLibrary
from src.core.app import App
from src.core.config import settings
from datetime import datetime, timedelta

def test_models():
    bp = BehavioralProfile(frequent_categories=["Food & Drink"])
    user = UserProfile(user_id="test1", name="Test User", behavioral_profile=bp)

    assert user.user_id == "test1"
    assert user.streak_count == 0
    assert len(user.active_challenges) == 0
    assert user.behavioral_profile.frequent_categories == ["Food & Drink"]

def test_bank_integration():
    bank = BankIntegrationSimulator()
    assert bank.connected is False

    bank.connect_account("user1")
    assert bank.connected is True

    txns = bank.fetch_recent_transactions("user1", days=7)
    assert len(txns) == 10

    # Dates are generated randomly within the past N days but timedelta calculation has milliseconds difference
    # add a small buffer for check
    now = datetime.now()
    for txn in txns:
        assert isinstance(txn, Transaction)
        assert txn.date >= now - timedelta(days=7, seconds=10)

def test_challenge_library():
    library = ChallengeLibrary()

    # Test getting challenges by valid category
    spending_challenges = library.get_challenges_by_category("spending")
    assert len(spending_challenges) > 0
    for challenge in spending_challenges:
        assert isinstance(challenge, Challenge)
        assert challenge.category == "spending"

    # Test invalid category
    invalid = library.get_challenges_by_category("invalid_cat")
    assert len(invalid) == 0

def test_app_core_logic():
    app = App(settings=settings)

    # Verify initial state
    assert app.current_user.streak_count == 0
    assert len(app.current_user.active_challenges) == 0

    # Run the app which simulates the full flow
    app.run()

    # After run, the mock flow should have updated the user
    # 1. Connected bank and analyzed txns (frequent_categories should be populated)
    assert len(app.current_user.behavioral_profile.frequent_categories) > 0

    # 2. Generated a daily challenge (should have one active, but complete_challenge pops it)
    # 3. Completed the challenge (streak should be 1, completed should have 1)
    assert app.current_user.streak_count == 1
    assert len(app.current_user.completed_challenges) == 1
    assert len(app.current_user.active_challenges) == 0 # It was popped
