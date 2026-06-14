import pyautogui

from src.logger import Logger
from src.types import Cell


class Hands:
    def __init__(self, logger: Logger):
        self.logger = logger

    def click(self, x: int, y: int) -> None:
        self.logger.info("CLICK:", x, y)
        pyautogui.click(x, y)

    def click_cell(self, cell: Cell) -> None:
        self.logger.info("CLICK_CELL:", cell)
        pyautogui.click(cell.x, cell.y)
