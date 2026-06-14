class EasyBrain:
    def __init__(self, logger):
        self.logger = logger

    def compute(self, cells):
        self.logger.info("CELLS: ", cells)

        for cells_row in cells:
            for cell in cells_row:
                self.logger.info(cell)
                if cell[2] == 'N':
                    return cell

        return None
