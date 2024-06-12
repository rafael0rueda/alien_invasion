class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screeb settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (14, 10, 13)

        # Ship settings
        self.ship_speed = 1.5
