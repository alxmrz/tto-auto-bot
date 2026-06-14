from typing import Optional

import cv2

from src.config import Config
from src.image import Image
from src.types import Cell


class Eyes:
    def __init__(self, config: Config, image: Image, logger):
        self.config = config
        self.image = image
        self.logger = logger
        self.template_grid = cv2.imread(config.grid_template_path, 0)
        self.template_o = cv2.imread(config.template_o_path, 0)
        self.template_x = cv2.imread(config.template_x_path, 0)
        self.template_h, self.template_w = self.template_grid.shape
        self.template_button = cv2.imread(config.template_ok_button_path, 0)
        self.template_easy_level = cv2.imread(config.template_easy_level_path, 0)
        self.template_hard_level = cv2.imread(config.template_hard_level_path, 0)
        self.grid_pos = None

    def find_grid_on_screen(self) -> Optional[tuple[int, int]]:
        if self.grid_pos is None:
            grid_pos = self.image.find_template(self.template_grid)

            if grid_pos:
                self.logger.info("Сетка найдена ", grid_pos)
                self.grid_pos = grid_pos
                return grid_pos
            else:
                self.logger.info("Сетка не найдена!")
                return None
        else:
            return self.grid_pos

    def get_all_cell_coords(self) -> Optional[list[list[tuple[int, int]]]]:
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

    def get_cells(self) -> Optional[list[list[Cell]]]:
        cell_coords = self.get_all_cell_coords()
        if cell_coords is None:
            return None

        for row_index, row in enumerate(cell_coords):
            for cell_index, cell in enumerate(row):
                cell_image = self.image.capture_region(cell[0], cell[1], 63, 63)

                if self.config.debug:
                    file_name = "screen_shots/row_" + str(row_index) + "_cell_" + str(cell_index) + ".png"
                    cv2.imwrite(file_name, cell_image)

                value = "N"

                x_found = self.image.find_template(self.template_x, cell_image)
                if x_found:
                    value = "X"
                else:
                    o_found = self.image.find_template(self.template_o, cell_image)
                    if o_found:
                        value = "O"

                row[cell_index] = Cell(x=cell[0], y=cell[1], value=value)

        return cell_coords

    def find_ok_button(self) -> Optional[tuple[int, int]]:
        return self.image.find_template(self.template_button)

    def find_easy_level(self) -> Optional[tuple[int, int]]:
        return self.image.find_template(self.template_easy_level)

    def find_hard_level(self) -> Optional[tuple[int, int]]:
        return self.image.find_template(self.template_hard_level)
