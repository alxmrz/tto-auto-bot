from dataclasses import dataclass


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
