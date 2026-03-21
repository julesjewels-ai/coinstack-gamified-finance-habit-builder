"""
Core application logic for Coinstack.
Handles the main business processes of the gamified finance habit builder.
"""

from src.core.models import UserProfile, BehavioralProfile
from src.core.challenge_library import ChallengeLibrary
from src.core.bank_integration import BankIntegrationSimulator
from src.core.config import COINSTACK_DEBUG
import random

class App:
    """
    The main Coinstack application class.

    This class orchestrates the various components of the gamified finance
    habit builder, including connecting to bank accounts, processing transactions,
    generating challenges, and tracking user progress.
    """

    def __init__(self, debug_mode: bool | None = None) -> None:
        """
        Initializes the Coinstack application.

        Args:
            debug_mode (bool | None): If True, enables debug logging and features.
                                      If None, falls back to the COINSTACK_DEBUG environment variable.
        """
        if debug_mode is not None:
            self.debug_mode = debug_mode
        else:
            self.debug_mode = COINSTACK_DEBUG
        self.version = "0.1.0"
        self._initialized = False

        # Core components
        self.challenge_library = ChallengeLibrary()
        self.bank_integration = BankIntegrationSimulator()

        # Default user for MVP
        self.current_user = UserProfile(
            user_id="user_123",
            name="Alex",
            behavioral_profile=BehavioralProfile()
        )

        self._initialize_components()

    def _initialize_components(self) -> None:
        """
        Initializes internal components like database connections, API clients, etc.
        """
        print(f"Coinstack App (v{self.version}) initializing...")
        if self.debug_mode:
            print("Debug mode is ENABLED.")

        self._initialized = True
        print("Coinstack App initialization complete.")

    def analyze_transactions(self) -> None:
        """Analyze recent transactions to update user profile."""
        transactions = self.bank_integration.fetch_recent_transactions(self.current_user.user_id)

        # Simple analysis: find most frequent category
        categories = {}
        for txn in transactions:
            categories[txn.category] = categories.get(txn.category, 0) + 1

        if categories:
            sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
            self.current_user.behavioral_profile.frequent_categories = [cat[0] for cat in sorted_categories[:3]]

        if self.debug_mode:
            print(f"User frequent spending categories: {self.current_user.behavioral_profile.frequent_categories}")

    def generate_daily_challenge(self) -> None:
        """Generate a personalized challenge based on user profile."""
        if not self.current_user.active_challenges:
            # Map frequent spending categories to challenge categories
            # This is a simplified mapping for the MVP
            frequent_cats = self.current_user.behavioral_profile.frequent_categories

            selected_category = "spending" # Default

            if frequent_cats:
                # If they spend a lot, give them a saving or spending challenge
                # For MVP, let's just alternate or randomly pick based on their top category
                top_cat = frequent_cats[0]
                if top_cat in ["Subscriptions", "Shopping", "Entertainment"]:
                    selected_category = "spending"
                elif top_cat in ["Food & Drink", "Groceries"]:
                    selected_category = random.choice(["spending", "saving"])
                else:
                    selected_category = random.choice(["saving", "debt"])
            else:
                 # Randomly select a category to focus on if no data
                categories = ["spending", "saving", "debt"]
                selected_category = random.choice(categories)

            challenges = self.challenge_library.get_challenges_by_category(selected_category)
            if challenges:
                challenge = random.choice(challenges)
                self.current_user.active_challenges.append(challenge)
                print(f"\n🎯 New Challenge Assigned: {challenge.title}")
                print(f"   Description: {challenge.description}")
                print(f"   Duration: {challenge.duration_minutes} minutes")

    def complete_challenge(self, challenge_id: str) -> bool:
        """Mark a challenge as complete and update streaks."""
        for i, challenge in enumerate(self.current_user.active_challenges):
            if challenge.id == challenge_id:
                # Mark complete
                completed = self.current_user.active_challenges.pop(i)
                completed.completed = True
                self.current_user.completed_challenges.append(completed)

                # Increment streak
                self.current_user.streak_count += 1

                print(f"\n🎉 Challenge Completed: {completed.title}!")
                print(f"🔥 Current Streak: {self.current_user.streak_count} days")
                return True

        return False

    def run(self) -> None:
        """
        Starts the main application loop or process.

        This method connects to external services, fetches data,
        processes challenges, and interacts with the user.
        """
        if not self._initialized:
            raise RuntimeError("App not initialized. Call _initialize_components first.")

        print("Coinstack App is running!")

        # 1. Authenticate and connect
        print(f"Welcome back, {self.current_user.name}!")
        self.bank_integration.connect_account(self.current_user.user_id)

        # 2 & 3. Fetch and process data
        print("Analyzing financial profile...")
        self.analyze_transactions()

        # 4. Generate daily challenges
        self.generate_daily_challenge()

        # 5. Simulate challenge completion (for MVP demo)
        if self.current_user.active_challenges:
            challenge_to_complete = self.current_user.active_challenges[0]
            self.complete_challenge(challenge_to_complete.id)

        print("\nApplication finished its primary task (MVP simulation).")
