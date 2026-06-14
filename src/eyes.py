import cv2
import numpy as np

from src.config import Config
from src.image import Image
from src.logger import Logger
from src.types import Cell


class Eyes:
    def __init__(self, config: Config, image: Image, logger: Logger):
        self.config = config
        self.image = image
        self.logger = logger
        self.template_grid = self._load_template(config.grid_template_path)
        self.template_o = self._load_template(config.template_o_path)
        self.template_x = self._load_template(config.template_x_path)
        self.template_button = self._load_template(config.template_ok_button_path)
        self.template_easy_level = self._load_template(config.template_easy_level_path)
        self.template_hard_level = self._load_template(config.template_hard_level_path)
        self.grid_pos = None

    def _load_template(self, path: str) -> np.ndarray:
        template = cv2.imread(path, 0)
        if template is None:
            raise FileNotFoundError(f"Template not found: {path}")
        return template

    def find_grid_on_screen(self) -> tuple[int, int] | None:
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

    def get_all_cell_coords(self) -> list[list[tuple[int, int]]] | None:
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

    def get_cells(self) -> list[list[Cell]] | None:
        cell_coords = self.get_all_cell_coords()
        if cell_coords is None:
            return None

        for row_index, row in enumerate(cell_coords):
            for cell_index, cell in enumerate(row):
                cx, cy = cell
                cell_image = self.image.capture_region(cx, cy, self.config.cell_w, self.config.cell_h)

                if self.config.debug:
                    file_name = f"screen_shots/row_{row_index}_cell_{cell_index}.png"
                    cv2.imwrite(file_name, cell_image)

                value = "N"

                if self.image.find_template(self.template_x, cell_image):
                    value = "X"
                elif self.image.find_template(self.template_o, cell_image):
                    value = "O"

                row[cell_index] = Cell(x=cx, y=cy, value=value)

        return cell_coords

    def find_ok_button(self) -> tuple[int, int] | None:
        return self.image.find_template(self.template_button)

    def find_easy_level(self) -> tuple[int, int] | None:
        return self.image.find_template(self.template_easy_level)

    def find_hard_level(self) -> tuple[int, int] | None:
        return self.image.find_template(self.template_hard_level)
