from typing import Optional

from src.types import Cell


class EasyBrain:
    def __init__(self, logger):
        self.logger = logger

    def compute(self, cells: list[list[Cell]]) -> Optional[Cell]:
        self.logger.info("CELLS:", cells)

        for cells_row in cells:
            for cell in cells_row:
                if cell.value == "N":
                    return cell

        return None
