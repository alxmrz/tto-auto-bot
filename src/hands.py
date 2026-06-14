import pyautogui


class Hands:
    @staticmethod
    def click(x: int, y: int):
        pyautogui.click(x, y)

    @staticmethod
    def click_cell(cell: tuple):
        x, y, _ = cell
        pyautogui.click(x, y)
