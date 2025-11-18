\"\"\"
BadgeSystem: Gamification badges and achievement tracking for motivation and engagement.
\"\"\"

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class BadgeType(Enum):
    \"\"\"Types of badges students can earn.\"\"\"
    COMPLETION = \"completion\"      # Complete X lessons
    SPEED = \"speed\"                # Complete lesson under time limit
    PERFECT = \"perfect\"            # Perfect quiz score
    CHALLENGE_MASTER = \"challenge_master\"  # Complete all challenges
    STREAK = \"streak\"              # Consistent completion streak
    EXPLORER = \"explorer\"          # Try multiple topics
    CODE_WARRIOR = \"code_warrior\"  # Complete many code challenges
    QUIZ_ACE = \"quiz_ace\"          # High average quiz scores


@dataclass
class Badge:
    \"\"\"Represents a badge/achievement.\"\"\"
    id: str
    name: str
    description: str
    badge_type: BadgeType
    icon_emoji: str
    points: int
    criteria_description: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            \"id\": self.id,
            \"name\": self.name,
            \"description\": self.description,
            \"type\": self.badge_type.value,
            \"icon\": self.icon_emoji,
            \"points\": self.points,
            \"criteria\": self.criteria_description,
        }


class BadgeSystem:
    \"\"\"Manages badge definitions and achievement logic.\"\"\"
    
    def __init__(self):
        self.badges: Dict[str, Badge] = self._initialize_badges()
    
    def _initialize_badges(self) -> Dict[str, Badge]:
        \"\"\"Initialize standard badges.\"\"\"
        return {
            \"first_lesson\": Badge(
                id=\"first_lesson\",
                name=\"First Steps\",
                description=\"Complete your first lesson!\",
                badge_type=BadgeType.COMPLETION,
                icon_emoji=\"🎓\",
                points=50,
                criteria_description=\"Complete 1 lesson\",
            ),
            \"lesson_streak_5\": Badge(
                id=\"lesson_streak_5\",
                name=\"On a Roll!\",
                description=\"Complete 5 lessons in a row!\",
                badge_type=BadgeType.STREAK,
                icon_emoji=\"🔥\",
                points=250,
                criteria_description=\"Complete 5 consecutive lessons\",
            ),
            \"lesson_streak_10\": Badge(
                id=\"lesson_streak_10\",
                name=\"Unstoppable!\",
                description=\"Complete 10 lessons in a row!\",
                badge_type=BadgeType.STREAK,
                icon_emoji=\"⚡\",
                points=500,
                criteria_description=\"Complete 10 consecutive lessons\",
            ),
            \"perfect_quiz\": Badge(
                id=\"perfect_quiz\",
                name=\"Quiz Master\",
                description=\"Get a perfect score on a quiz!\",
                badge_type=BadgeType.PERFECT,
                icon_emoji=\"100️⃣\",
                points=150,
                criteria_description=\"Score 100% on a quiz\",
            ),
            \"code_warrior\": Badge(
                id=\"code_warrior\",
                name=\"Code Warrior\",
                description=\"Complete 5 code challenges!\",
                badge_type=BadgeType.CODE_WARRIOR,
                icon_emoji=\"⚔️\",
                points=300,
                criteria_description=\"Complete 5 code challenges\",
            ),
            \"explorer\": Badge(
                id=\"explorer\",
                name=\"Topic Explorer\",
                description=\"Explore lessons in 3 different topics!\",
                badge_type=BadgeType.EXPLORER,
                icon_emoji=\"🗺️\",
                points=200,
                criteria_description=\"Learn 3 different topics\",
            ),
            \"speed_learner\": Badge(
                id=\"speed_learner\",
                name=\"Speed Learner\",
                description=\"Complete a lesson in half the estimated time!\",
                badge_type=BadgeType.SPEED,
                icon_emoji=\"⏱️\",
                points=100,
                criteria_description=\"Complete lesson faster than estimate\",
            ),
            \"all_challenges\": Badge(
                id=\"all_challenges\",
                name=\"Challenge Master\",
                description=\"Complete all challenges in a module!\",
                badge_type=BadgeType.CHALLENGE_MASTER,
                icon_emoji=\"🏆\",
                points=400,
                criteria_description=\"Complete all module challenges\",
            ),
        }
    
    def get_badge(self, badge_id: str) -> Badge:
        \"\"\"Retrieve a badge by ID.\"\"\"
        return self.badges.get(badge_id)
    
    def get_all_badges(self) -> List[Badge]:
        \"\"\"Get all available badges.\"\"\"
        return list(self.badges.values())
    
    def get_badges_by_type(self, badge_type: BadgeType) -> List[Badge]:
        \"\"\"Get all badges of a specific type.\"\"\"
        return [b for b in self.badges.values() if b.badge_type == badge_type]
    
    def create_custom_badge(self, badge_id: str, name: str, description: str,
                          badge_type: BadgeType, icon_emoji: str, points: int,
                          criteria: str) -> Badge:
        \"\"\"Create a custom badge.\"\"\"
        badge = Badge(
            id=badge_id,
            name=name,
            description=description,
            badge_type=badge_type,
            icon_emoji=icon_emoji,
            points=points,
            criteria_description=criteria,
        )
        self.badges[badge_id] = badge
        return badge
    
    def get_badge_display(self, badge: Badge) -> str:
        \"\"\"Get a nice formatted string for displaying a badge.\"\"\"
        return f\"{badge.icon_emoji} **{badge.name}** - {badge.description} (+{badge.points} points)\"
