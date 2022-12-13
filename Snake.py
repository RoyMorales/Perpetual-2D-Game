# Snake game controlled by Ai

# Import Packages
import pygame
import numpy as np
import sys
import random


# Import Class
from settings import SettingsClass


class SnakeGame:
    def __init__(self):
        # Inheritance Class
        self.ai_user_choice = False
        self.settings = SettingsClass()

        # Title App
        pygame.display.set_caption("Snake Game")

        # Screen Settings
        self.screen_game = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.get_surface().fill((0, 10, 0))

        # Initial Matrix
        self.snake_position_x = self.settings.snake_position_x
        self.snake_position_y = self.settings.snake_position_y
        """
        self.grid_matrix = np.zeros(
            (self.settings.number_squares, self.settings.number_squares), dtype=int
        )
        """
        self.grid_matrix = np.random.rand(self.settings.number_squares, self.settings.number_squares)
        self.grid_matrix[
            self.snake_position_x, self.snake_position_y
        ] = self.settings.snake_value

        # Level Config
        self.current_level = self.settings.initial_level
        self.player_hp = self.settings.player_hp

    # ________________________________ Runner____________________________________
    def run_app(self):
        # user_input = input('Game mode (ai/user): ')
        # match user_input:
        #     case 'ai':
        #         self.ai_user_choice = True
        #     case 'user':
        #         self.ai_user_choice = False
        while True:
            self.rewards_placement()
            self.draw_squares()
            self.check_event()

            pygame.display.update()

    # ___________________________________________________________________________

    # ________________________________  Player Events ___________________________
    def check_event(self):
        event = pygame.event.wait(10000)
        if event.type == pygame.QUIT:
            sys.exit()
        elif self.ai_user_choice is False and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.movement_logic_up(self.snake_position_x, self.snake_position_y)
            elif event.key == pygame.K_a:
                self.movement_logic_left(self.snake_position_x, self.snake_position_y)
            elif event.key == pygame.K_s:
                self.movement_logic_down(self.snake_position_x, self.snake_position_y)
            elif event.key == pygame.K_d:
                self.movement_logic_right(self.snake_position_x, self.snake_position_y)

    # ___________________________________________________________________________

    # ________________________________ Movement Logic ___________________________
    def movement_logic_up(self, position_x, position_y):
        print("Up", end=" ")
        print(self.snake_position_x, self.snake_position_y)
        self.snake_position_x = position_x - 1
        self.player_hp += self.grid_matrix[
            int(position_x - 1), int(self.snake_position_y)
        ]
        print(self.player_hp)

        self.grid_matrix[
            int(self.snake_position_x), int(self.snake_position_y)
        ] = self.settings.snake_value
        self.grid_matrix[position_x, position_y] = self.settings.background_value

    def movement_logic_down(self, position_x, position_y):
        print("Down", end=" ")
        print(self.snake_position_x, self.snake_position_y)
        self.snake_position_x = position_x + 1
        self.player_hp += self.grid_matrix[
            int(position_x + 1), int(self.snake_position_y)
        ]
        print(self.player_hp)

        self.grid_matrix[
            int(self.snake_position_x), int(self.snake_position_y)
        ] = self.settings.snake_value
        self.grid_matrix[position_x, position_y] = self.settings.background_value

    def movement_logic_left(self, position_x, position_y):
        print("Left", end=" ")
        print(self.snake_position_x, self.snake_position_y)
        self.snake_position_y = position_y - 1
        self.player_hp += self.grid_matrix[int(position_x), int(position_y - 1)]
        print(self.player_hp)

        self.grid_matrix[
            int(self.snake_position_x), int(self.snake_position_y)
        ] = self.settings.snake_value
        self.grid_matrix[position_x, position_y] = self.settings.background_value

    def movement_logic_right(self, position_x, position_y):
        print("Right", end=" ")
        print(self.snake_position_x, self.snake_position_y)
        self.snake_position_y = position_y + 1
        self.player_hp += self.grid_matrix[
            int(self.snake_position_x), int(position_y + 1)
        ]
        print(self.player_hp)

        self.grid_matrix[
            int(self.snake_position_x), int(self.snake_position_y)
        ] = self.settings.snake_value
        self.grid_matrix[position_x, position_y] = self.settings.background_value

    # ____________________________________________________________________________

    # ________________________________ Draw Board ________________________________
    def draw_squares(self):
        draw_y = 0
        for row in self.grid_matrix:
            draw_x = 0
            for value in row:
                if value == self.settings.background_value:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.square_colour_background,
                        [
                            draw_x,
                            draw_y,
                            self.settings.grid_width,
                            self.settings.grid_width,
                        ],
                    )
                elif value == self.settings.snake_value:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.snake_colour,
                        [
                            draw_x,
                            draw_y,
                            self.settings.grid_width,
                            self.settings.grid_width,
                        ],
                    )
                elif value == self.settings.reward_positive:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.square_colour_reward_positive,
                        [
                            draw_x,
                            draw_y,
                            self.settings.grid_width,
                            self.settings.grid_width,
                        ],
                    )
                elif value == self.settings.reward_negative:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.square_colour_reward_negative,
                        [
                            draw_x,
                            draw_y,
                            self.settings.grid_width,
                            self.settings.grid_width,
                        ],
                    )
                draw_x += self.settings.grid_width
            draw_y += self.settings.grid_height

    # _________________________________________________________________________

    def rewards_placement(self):
        if not any(
            self.settings.reward_positive in element for element in self.grid_matrix
        ):
            self.current_level += 1
            for quant_reward in range(
                self.settings.negative_reward_increment_per_level * self.current_level
            ):
                self.grid_matrix[
                    random.randint(1, self.settings.number_squares - 1),
                    random.randint(1, self.settings.number_squares - 1),
                ] = self.settings.reward_negative
            for quant_reward in range(
                self.settings.positive_reward_increment_per_level * self.current_level
            ):
                self.grid_matrix[
                    random.randint(1, self.settings.number_squares - 1),
                    random.randint(1, self.settings.number_squares - 1),
                ] = self.settings.reward_positive
        else:
            pass

    def player_stats_update(self):
        self.player_hp += self.grid_matrix[
            int(self.snake_position_x), int(self.snake_position_y)
        ]
        print(self.player_hp)

    def snake_game_ai(self):
        print("ai")


if __name__ == "__main__":
    pygame.init()
    SnakeGame().run_app()
