import time

from src.brain import EasyBrain
from src.eyes import Eyes
from src.hands import Hands


class Bot:
    def __init__(self, brain: EasyBrain, eyes: Eyes, hands: Hands, logger):
        self.brain = brain
        self.eyes = eyes
        self.hands = hands
        self.logger = logger

    def run(self):
        self.finish_game()

        cell = self.brain.compute(self.eyes.get_cells())

        if cell is None:
            return

        self.hands.click_cell(cell)

    def finish_game(self):
        ok_coords = self.eyes.find_ok_button()

        if ok_coords is None:
            return

        x, y = ok_coords
        self.hands.click(x + 20, y + 5)

        time.sleep(0.5)

        easy_coords = self.eyes.find_easy_level()

        if easy_coords is None:
            return

        x, y = easy_coords
        self.hands.click(x + 20, y + 8)

        hard_coords = self.eyes.find_hard_level()

        if hard_coords is None:
            return

        x, y = hard_coords
        self.hands.click(x + 10, y + 3)
