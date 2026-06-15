import time

from src.brain import MediumBrain
from src.eyes import Eyes
from src.hands import Hands
from src.logger import Logger
from src.types import Cell


class Bot:
    def __init__(self, brain: MediumBrain, eyes: Eyes, hands: Hands, logger: Logger):
        self.brain = brain
        self.eyes = eyes
        self.hands = hands
        self.logger = logger

    def run(self) -> list[list[Cell]]:
        self.finish_game()

        cells = self.eyes.get_cells()

        if cells is None:
            raise RuntimeError("Cells not found")

        cell = self.brain.compute(cells=cells)

        if cell is None:
            return []

        self.hands.click_cell(cell)

        return cells

    def finish_game(self) -> None:
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
