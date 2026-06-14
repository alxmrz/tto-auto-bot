import cv2

from src.image import find_template, capture_region
from src.config import Config


class Eyes:
    def __init__(self, config: Config, logger):
        self.config = config
        self.logger = logger
        self.template_grid = cv2.imread(config.grid_template_path, 0)
        self.template_o = cv2.imread(config.template_o_path, 0)
        self.template_x = cv2.imread(config.template_x_path, 0)
        self.template_h, self.template_w = self.template_grid.shape
        self.template_button = cv2.imread(config.template_ok_button_path, 0)
        self.template_easy_level = cv2.imread(config.template_easy_level_path, 0)
        self.template_hard_level = cv2.imread(config.template_hard_level_path, 0)
        self.grid_pos = None

    def find_grid_on_screen(self):
        if self.grid_pos is None:
            grid_pos = find_template(self.template_grid)

            if grid_pos:
                self.logger.info("Сетка найдена ", grid_pos)
                self.grid_pos = grid_pos
                return grid_pos
            else:
                self.logger.info("Сетка не найдена!")
                return None
        else:
            return self.grid_pos

    def get_all_cell_coords(self):
        pos = self.find_grid_on_screen()
        if not pos:
            return None

        grid_x, grid_y = pos
        cells = []

        grid_x += 2
        grid_y += 2

        for row in range(self.config.rows):
            row_cells = []
            for col in range(self.config.cols):
                if col > 0:
                    offset_x = 5 * col
                else:
                    offset_x = 0

                if row > 0:
                    offset_y = 1
                else:
                    offset_y = 0

                cell_x = grid_x + offset_x + col * self.config.cell_w
                cell_y = grid_y - offset_y + row * self.config.cell_h
                row_cells.append((cell_x, cell_y))
            cells.append(row_cells)

        return cells

    def get_cells(self):
        cell_coords = self.get_all_cell_coords()
        if cell_coords:
            for row_index, row in enumerate(cell_coords):
                for cell_index, cell in enumerate(row):
                    cell_image = capture_region(cell[0], cell[1], 63, 63)
                    file_name = "screen_shots/row_" + str(row_index) + "_cell_" + str(cell_index) + ".png"
                    cv2.imwrite(file_name, cell_image)

                    value = "N"

                    x_found = find_template(self.template_x, cell_image)
                    if x_found:
                        value = "X"
                    else:
                        o_found = find_template(self.template_o, cell_image)
                        if o_found:
                            value = "O"

                    row[cell_index] = cell + (value,)
        return cell_coords

    def find_ok_button(self):
        return find_template(self.template_button)

    def find_easy_level(self):
        return find_template(self.template_easy_level)

    def find_hard_level(self):
        return find_template(self.template_hard_level)
