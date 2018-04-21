"""
This module contains the definitions for commands that can be sent to the ACC.
"""

class TurnOffCommand:
    pass

class ChangeSettingsCommand:
    def __init__(self, user_set_speed, safe_distance):
        self.user_set_speed = user_set_speed
        self.safe_distance = safe_distance
