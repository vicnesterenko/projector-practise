class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps
        elif self.orientation == "left":
            self.position_x -= steps
        elif self.orientation == "right":
            self.position_x += steps

    def turn(self, direction):
        if direction == "left":
            directions = ["up", "left", "down", "right"]
        elif direction == "right":
            directions = ["up", "right", "down", "left"]

        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index + 1) % 4]

    def display_position(self):
        print(
            f"Position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}"
        )


if __name__ == "__main__":
    robot = Robot(orientation="up", position_x=0, position_y=0)
    robot.display_position()
    robot.move(3)
    robot.turn("right")
    robot.move(2)
    robot.display_position()
