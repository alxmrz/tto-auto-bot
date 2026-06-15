from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    grid_template_path: str = "resources/template_grid.png"
    template_o_path: str = "resources/template_o.png"
    template_x_path: str = "resources/template_x.png"
    template_ok_button_path: str = "resources/ok_button.png"
    template_easy_level_path: str = "resources/easy_difficult.png"
    template_hard_level_path: str = "resources/hard_difficult.png"
    rows: int = 3
    cols: int = 3
    cell_w: int = 63
    cell_h: int = 63
    threshold: float = 0.8
    debug: bool = True

    def __post_init__(self) -> None:
        load_dotenv()
        self.grid_template_path = os.getenv("GRID_TEMPLATE_PATH", self.grid_template_path)
        self.template_o_path = os.getenv("TEMPLATE_O_PATH", self.template_o_path)
        self.template_x_path = os.getenv("TEMPLATE_X_PATH", self.template_x_path)
        self.template_ok_button_path = os.getenv("TEMPLATE_OK_BUTTON_PATH", self.template_ok_button_path)
        self.template_easy_level_path = os.getenv("TEMPLATE_EASY_LEVEL_PATH", self.template_easy_level_path)
        self.template_hard_level_path = os.getenv("TEMPLATE_HARD_LEVEL_PATH", self.template_hard_level_path)
        self.rows = int(os.getenv("ROWS", str(self.rows)))
        self.cols = int(os.getenv("COLS", str(self.cols)))
        self.cell_w = int(os.getenv("CELL_W", str(self.cell_w)))
        self.cell_h = int(os.getenv("CELL_H", str(self.cell_h)))
        self.threshold = float(os.getenv("THRESHOLD", str(self.threshold)))
        debug_raw = os.getenv("DEBUG", str(self.debug))
        self.debug = debug_raw.lower() in ("true", "1", "yes")
