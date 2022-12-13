# Settings for Fly Simulator

class SettingsClass:
    def __init__(self):

        # Window Settings
        self.window_width = 800
        self.window_height = 800

        # Game grid
        self.number_squares = int(40)

        self.grid_width = self.window_width / self.number_squares
        self.grid_height = self.window_width / self.number_squares

        self.square_colour_background = (13, 165, 13) # Green
        self.square_colour_reward_positive = (16, 45, 235) # Blue
        self.square_colour_reward_negative = (235, 52, 16) # Red
        self.snake_colour = (255, 255, 255) # White

        # Snake Variables
        self.snake_position_x = int(self.number_squares/2)
        self.snake_position_y = int(self.number_squares/2)
        self.snake_initial_velocity = 1
        self.snake_velocity_increment = 1

        # Level Design
        self.initial_level = 0
        self.negative_reward_increment_per_level = 2
        self.positive_reward_increment_per_level = 1

        # Game Rewards Value
        self.background_value = 0
        self.snake_value = 1
        self.reward_negative = -10
        self.reward_positive = 2

        # Player Stat
        self.player_hp = 100

