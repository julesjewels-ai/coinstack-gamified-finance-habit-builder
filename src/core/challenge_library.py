from src.core.models import Challenge
from typing import List

class ChallengeLibrary:
    def __init__(self):
        self.challenges: List[Challenge] = [
            Challenge(
                id="c1",
                title="Identify a Subscription to Cancel",
                description="Review your recent transactions and find one subscription you no longer need. Take 3 minutes to cancel it.",
                category="spending"
            ),
            Challenge(
                id="c2",
                title="Calculate Your Daily Coffee Cost",
                description="Check how much you spent on coffee or drinks out this week. Could you make it at home tomorrow?",
                category="spending"
            ),
            Challenge(
                id="c3",
                title="Set a 24-Hour Rule",
                description="Find an item you want to buy online right now, but wait 24 hours before purchasing it.",
                category="spending"
            ),
            Challenge(
                id="c4",
                title="Setup Auto-Transfer to Savings",
                description="Log into your bank and set up a small automatic transfer (even $5) to your savings account on payday.",
                category="saving"
            ),
            Challenge(
                id="c5",
                title="Round Up Savings",
                description="Look at your last 5 purchases. Calculate the round-up to the nearest dollar and manually transfer that total to savings.",
                category="saving"
            ),
            Challenge(
                id="c6",
                title="Identify Highest Interest Debt",
                description="Check your credit cards or loans. Find the one with the highest interest rate and make a plan to target it first.",
                category="debt"
            ),
            Challenge(
                id="c7",
                title="Make a Small Extra Payment",
                description="Make an extra payment of just $10 towards your lowest balance debt to start the snowball effect.",
                category="debt"
            )
        ]

    def get_challenges_by_category(self, category: str) -> List[Challenge]:
        return [c for c in self.challenges if c.category == category]

    def get_challenge_by_id(self, challenge_id: str) -> Challenge | None:
        for challenge in self.challenges:
            if challenge.id == challenge_id:
                return challenge
        return None
