# Tic-Tac-Toe auto bot

Tic-Tac-Toe bot using OpenCV template matching + screen capture. Detects a 3×3 grid on screen, reads X/O marks via image templates, and clicks the next empty cell.

## Commands

```bash
make install      # pip install -e ".[dev]" (needs venv at .venv/)
make run          # python3 main.py
make test         # pytest (needs venv at .venv/)
```

## Tests

- Located in `tests/test_brain.py`
- Uses `pytest` (`make test`)
- `MediumBrain` blocking tested with `@pytest.mark.parametrize` — 24 cases (3 positions × 8 lines)
- `MediumBrain` fallback to `EasyBrain` tested with 3 cases (single O, empty board, full board)

## Dependencies

- Defined in `pyproject.toml` under `[project] dependencies`
- Requires Python ≥ 3.10 (specified via `requires-python`)
- Dev dependencies (`pytest`) under `[project.optional-dependencies] dev`

## Structure

| Path | Purpose |
|---|---|
| `main.py` | Entrypoint: listener + main loop |
| `src/bot.py` | Bot orchestrator: finish_game, run |
| `src/brain.py` | EasyBrain — picks first empty cell; MediumBrain — blocks opponent 2-in-a-row (lines: 3 rows, 3 cols, 2 diags) |
| `src/config.py` | Config dataclass — paths, grid dimensions |
| `src/eyes.py` | Eyes — screen detection via Image helpers; `_load_template` validates template files |
| `src/hands.py` | Hands — click helpers |
| `src/image.py` | `Image` class — `find_template`, `capture_region` (single `mss.MSS` instance) |
| `src/types.py` | `Cell` NamedTuple — `x`, `y`, `value` |
| `src/logger.py` | Logger — conditional console output |
| `resources/` | Template images for grid, X, O, OK button, difficulty buttons |
| `screen_shots/` | Runtime cell captures (gitignored) |

## Conventions

- Commits must follow [Conventional Commits](https://www.conventionalcommits.org/) format (e.g. `feat:`, `fix:`, `refactor:`, `chore:`, `docs:`).
- After every change add to AGENTS.md relevant important information
- Use `X | None` syntax instead of `Optional[X]` (Python 3.10+ union types)

## Quirks

- `make run` requires a display (X11/Wayland) — will fail headless
- Grid dimensions and cell size are in `Config` (defaults: 3×3, 63×63 px)
- No virtual environment tracked in repo; `.venv/` is gitignored
