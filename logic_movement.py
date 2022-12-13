
# Movement Logic for a Grid Game

# Not Used

class Movement:

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





