from src.logger import Logger
from src.types import Cell


class EasyBrain:
    def __init__(self, logger: Logger):
        self.logger = logger

    def compute(self, cells: list[list[Cell]]) -> Cell | None:
        self.logger.info("CELLS:", cells)

        for cells_row in cells:
            for cell in cells_row:
                if cell.value == "N":
                    return cell

        return None

class MediumBrain:
    def __init__(self, easy_brain: EasyBrain, logger: Logger):
        self.easy_brain = easy_brain
        self.logger = logger

    def compute(self, cells: list[list[Cell]]) -> Cell | None:
        self.logger.info("CELLS:", cells)

        threat = self._find_blocking_move(cells)
        if threat is not None:
            return threat

        return self.easy_brain.compute(cells)

    @staticmethod
    def _find_blocking_move(cells: list[list[Cell]]) -> Cell | None:
        n = len(cells)
        lines: list[list[Cell]] = []

        for row in cells:
            lines.append(row)

        for col in range(n):
            lines.append([cells[row][col] for row in range(n)])

        lines.append([cells[i][i] for i in range(n)])
        lines.append([cells[i][n - 1 - i] for i in range(n)])

        for line in lines:
            o_cells = [c for c in line if c.value == "O"]
            n_cells = [c for c in line if c.value == "N"]
            if len(o_cells) == 2 and len(n_cells) == 1:
                return n_cells[0]

        return None