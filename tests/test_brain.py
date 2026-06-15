import pytest

from src.brain import EasyBrain, MediumBrain
from src.logger import Logger
from src.types import Cell


def make_grid(values: list[list[str]]) -> list[list[Cell]]:
    return [
        [Cell(x, y, values[y][x]) for x in range(3)]
        for y in range(3)
    ]


@pytest.mark.parametrize("grid,expected", [
    # ── Row 0 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["O", "O", "N"],
            ["N", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(2, 0, "N"),
        id="row_0_end",
    ),
    pytest.param(
        make_grid([
            ["O", "N", "O"],
            ["N", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(1, 0, "N"),
        id="row_0_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "O", "O"],
            ["N", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(0, 0, "N"),
        id="row_0_start",
    ),
    # ── Row 1 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["O", "O", "N"],
            ["N", "N", "N"],
        ]),
        Cell(2, 1, "N"),
        id="row_1_end",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["O", "N", "O"],
            ["N", "N", "N"],
        ]),
        Cell(1, 1, "N"),
        id="row_1_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "O", "O"],
            ["N", "N", "N"],
        ]),
        Cell(0, 1, "N"),
        id="row_1_start",
    ),
    # ── Row 2 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "N", "N"],
            ["O", "O", "N"],
        ]),
        Cell(2, 2, "N"),
        id="row_2_end",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "N", "N"],
            ["O", "N", "O"],
        ]),
        Cell(1, 2, "N"),
        id="row_2_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "N", "N"],
            ["N", "O", "O"],
        ]),
        Cell(0, 2, "N"),
        id="row_2_start",
    ),
    # ── Col 0 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["O", "N", "N"],
            ["O", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(0, 2, "N"),
        id="col_0_bottom",
    ),
    pytest.param(
        make_grid([
            ["O", "N", "N"],
            ["N", "N", "N"],
            ["O", "N", "N"],
        ]),
        Cell(0, 1, "N"),
        id="col_0_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["O", "N", "N"],
            ["O", "N", "N"],
        ]),
        Cell(0, 0, "N"),
        id="col_0_top",
    ),
    # ── Col 1 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["N", "O", "N"],
            ["N", "O", "N"],
            ["N", "N", "N"],
        ]),
        Cell(1, 2, "N"),
        id="col_1_bottom",
    ),
    pytest.param(
        make_grid([
            ["N", "O", "N"],
            ["N", "N", "N"],
            ["N", "O", "N"],
        ]),
        Cell(1, 1, "N"),
        id="col_1_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "O", "N"],
            ["N", "O", "N"],
        ]),
        Cell(1, 0, "N"),
        id="col_1_top",
    ),
    # ── Col 2 ──────────────────────────────────────
    pytest.param(
        make_grid([
            ["N", "N", "O"],
            ["N", "N", "O"],
            ["N", "N", "N"],
        ]),
        Cell(2, 2, "N"),
        id="col_2_bottom",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "O"],
            ["N", "N", "N"],
            ["N", "N", "O"],
        ]),
        Cell(2, 1, "N"),
        id="col_2_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "N", "O"],
            ["N", "N", "O"],
        ]),
        Cell(2, 0, "N"),
        id="col_2_top",
    ),
    # ── Diagonal main (0,0)—(1,1)—(2,2) ──────────
    pytest.param(
        make_grid([
            ["O", "N", "N"],
            ["N", "O", "N"],
            ["N", "N", "N"],
        ]),
        Cell(2, 2, "N"),
        id="diag_main_tail",
    ),
    pytest.param(
        make_grid([
            ["O", "N", "N"],
            ["N", "N", "N"],
            ["N", "N", "O"],
        ]),
        Cell(1, 1, "N"),
        id="diag_main_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "O", "N"],
            ["N", "N", "O"],
        ]),
        Cell(0, 0, "N"),
        id="diag_main_head",
    ),
    # ── Diagonal anti (2,0)—(1,1)—(0,2) ──────────
    pytest.param(
        make_grid([
            ["N", "N", "O"],
            ["N", "O", "N"],
            ["N", "N", "N"],
        ]),
        Cell(0, 2, "N"),
        id="diag_anti_tail",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "O"],
            ["N", "N", "N"],
            ["O", "N", "N"],
        ]),
        Cell(1, 1, "N"),
        id="diag_anti_mid",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "O", "N"],
            ["O", "N", "N"],
        ]),
        Cell(2, 0, "N"),
        id="diag_anti_head",
    ),
])
def test_medium_brain_blocks_two_os(grid: list[list[Cell]], expected: Cell) -> None:
    logger = Logger(enable=False)
    brain = MediumBrain(EasyBrain(logger), logger)
    result = brain.compute(grid)
    assert result == expected


@pytest.mark.parametrize("grid,expected", [
    pytest.param(
        make_grid([
            ["O", "N", "N"],
            ["N", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(1, 0, "N"),
        id="fallback_single_o",
    ),
    pytest.param(
        make_grid([
            ["N", "N", "N"],
            ["N", "N", "N"],
            ["N", "N", "N"],
        ]),
        Cell(0, 0, "N"),
        id="fallback_empty_board",
    ),
    pytest.param(
        make_grid([
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"],
        ]),
        None,
        id="fallback_full_board",
    ),
])
def test_medium_brain_fallback(grid: list[list[Cell]], expected: Cell | None) -> None:
    logger = Logger(enable=False)
    brain = MediumBrain(EasyBrain(logger), logger)
    result = brain.compute(grid)
    assert result == expected
