import pyautogui

from src.config import Config
from src.logger import Logger
from src.types import Cell


class Hands:
    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger

    def click(self, x: int, y: int) -> None:
        self.logger.info("CLICK:", x, y)
        pyautogui.click(x, y)

    def click_cell(self, cell: Cell) -> None:
        cx = cell.x + self.config.cell_w // 2
        cy = cell.y + self.config.cell_h // 2
        self.logger.info("CLICK_CELL:", cell)
        pyautogui.click(cx, cy)
