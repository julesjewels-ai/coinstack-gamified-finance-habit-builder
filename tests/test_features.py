import pytest
from datetime import datetime
from src.core.models import Transaction, Challenge, BehavioralProfile, UserProfile
from src.core.bank_integration import BankIntegrationSimulator
from src.core.challenge_library import ChallengeLibrary
from src.core.app import App

def test_models():
    txn = Transaction(id="1", amount=10.5, merchant_name="Starbucks", category="Food & Drink", date=datetime.now())
    assert txn.id == "1"
    assert txn.amount == 10.5

    challenge = Challenge(id="c1", title="Test", description="Test desc", category="saving")
    assert challenge.id == "c1"
    assert not challenge.completed
    assert challenge.duration_minutes == 3

    profile = BehavioralProfile()
    assert profile.spending_score == 50
    assert len(profile.frequent_categories) == 0

    user = UserProfile(user_id="u1", name="Test User")
    assert user.user_id == "u1"
    assert user.streak_count == 0
    assert len(user.active_challenges) == 0

def test_bank_integration():
    simulator = BankIntegrationSimulator()
    assert not simulator.connected

    simulator.connect_account("u1")
    assert simulator.connected

    transactions = simulator.fetch_recent_transactions("u1", days=7)
    assert len(transactions) == 10

    # Test un-connected behavior
    sim2 = BankIntegrationSimulator()
    with pytest.raises(Exception, match="Bank account not connected"):
        sim2.fetch_recent_transactions("u2")

def test_challenge_library():
    lib = ChallengeLibrary()
    assert len(lib.challenges) > 0

    spending_challenges = lib.get_challenges_by_category("spending")
    assert len(spending_challenges) > 0
    for c in spending_challenges:
        assert c.category == "spending"

    c1 = lib.get_challenge_by_id("c1")
    assert c1 is not None
    assert c1.id == "c1"

def test_app_core_logic():
    app = App()
    assert app.current_user is not None

    # Simulate setup
    app.bank_integration.connect_account(app.current_user.user_id)
    app.analyze_transactions()

    # Check that behavioral profile was updated
    assert len(app.current_user.behavioral_profile.frequent_categories) > 0

    # Generate challenge
    app.generate_daily_challenge()
    assert len(app.current_user.active_challenges) == 1

    # Complete challenge
    active_challenge = app.current_user.active_challenges[0]
    success = app.complete_challenge(active_challenge.id)

    assert success is True
    assert len(app.current_user.active_challenges) == 0
    assert len(app.current_user.completed_challenges) == 1
    assert app.current_user.streak_count == 1
    assert app.current_user.completed_challenges[0].completed is True
