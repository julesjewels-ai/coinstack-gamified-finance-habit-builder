from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Transaction:
    id: str
    amount: float
    merchant_name: str
    category: str
    date: datetime

@dataclass
class Challenge:
    id: str
    title: str
    description: str
    category: str # spending, saving, debt
    duration_minutes: int = 3
    completed: bool = False

@dataclass
class BehavioralProfile:
    spending_score: int = 50
    saving_score: int = 50
    debt_score: int = 50
    frequent_categories: List[str] = field(default_factory=list)

@dataclass
class UserProfile:
    user_id: str
    name: str
    behavioral_profile: BehavioralProfile = field(default_factory=BehavioralProfile)
    streak_count: int = 0
    active_challenges: List[Challenge] = field(default_factory=list)
    completed_challenges: List[Challenge] = field(default_factory=list)
