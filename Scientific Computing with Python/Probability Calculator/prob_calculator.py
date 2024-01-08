import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # Constructor initializes a Hat instance with contents based on input kwargs
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        # Method to draw n balls randomly from the hat
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Function to perform experiments and calculate the probability of drawing expected balls
    successful_experiments_count = 0

    # Perform the specified number of experiments
    for _ in range(num_experiments):
        # Create a deep copy of the original hat for each experiment
        another_hat = copy.deepcopy(hat)

        # Draw a specified number of balls from the hat
        balls_drawn = another_hat.draw(num_balls_drawn)

        # Count the number of drawn balls that match the expected_balls dictionary
        balls_req = sum([1 for k, v in expected_balls.items()
                        if balls_drawn.count(k) >= v])

        # Increment the counter if all expected balls are drawn
        successful_experiments_count += 1 if balls_req == len(
            expected_balls) else 0

    # Calculate and return the probability
    return successful_experiments_count / num_experiments
