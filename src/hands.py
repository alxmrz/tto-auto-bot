import pyautogui

from src.types import Cell


class Hands:
    @staticmethod
    def click(x: int, y: int) -> None:
        pyautogui.click(x, y)

    @staticmethod
    def click_cell(cell: Cell) -> None:
        pyautogui.click(cell.x, cell.y)
