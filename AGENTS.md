# Tic-Tac-Toe auto bot

Tic-Tac-Toe bot using OpenCV template matching + screen capture. Detects a 3×3 grid on screen, reads X/O marks via image templates, and clicks the next empty cell.

## Commands

```bash
make init         # cp -n .env.example .env (creates .env if not exists)
make install      # pip install -r requirements.txt (needs venv at .venv/)
make run          # python3 main.py
make test         # pytest (needs venv at .venv/)
```

## Tests

- Located in `tests/test_brain.py`
- Uses `pytest` (`make test`)
- `MediumBrain` blocking tested with `@pytest.mark.parametrize` — 24 cases (3 positions × 8 lines)
- `MediumBrain` fallback to `EasyBrain` tested with 3 cases (single O, empty board, full board)

## Dependencies

- Defined in `requirements.txt`
- Requires Python ≥ 3.10
- Dev dependencies (`pytest`) in `requirements-dev.txt`
- Optional GUI dependencies (`PyQt5`) in `requirements-gui.txt`

## Structure

| Path | Purpose |
|---|---|
| `main.py` | Entrypoint: listener + main loop |
| `src/bot.py` | Bot orchestrator: finish_game, run |
| `src/brain.py` | EasyBrain — picks first empty cell; MediumBrain — blocks opponent 2-in-a-row (lines: 3 rows, 3 cols, 2 diags) |
| `src/config.py` | Config dataclass — reads params from `.env` via `python-dotenv` |
| `src/eyes.py` | Eyes — screen detection via Image helpers; `_load_template` validates template files |
| `src/hands.py` | Hands — click helpers |
| `src/image.py` | `Image` class — `find_template`, `capture_region` (single `mss.MSS` instance) |
| `src/types.py` | `Cell` NamedTuple — `x`, `y`, `value` |
| `src/logger.py` | Logger — conditional console output |
| `resources/` | Template images for grid, X, O, OK button, difficulty buttons |
| `resources/custom/` | Override templates here for other game styles |
| `screen_shots/` | Runtime cell captures (gitignored) |
| `.env.example` | Template for `.env` with all config env vars |
| `.env` | Local override for config (gitignored; created via `make init`) |

## Conventions

- Commits must follow [Conventional Commits](https://www.conventionalcommits.org/) format (e.g. `feat:`, `fix:`, `refactor:`, `chore:`, `docs:`).
- After every change add to AGENTS.md relevant important information
- Use `X | None` syntax instead of `Optional[X]` (Python 3.10+ union types)

## Quirks

- `make run` without GUI (`GUI_ENABLED=false`, default) works headless
- `GUI_ENABLED=true` requires a display (X11/Wayland) — will fail headless; Qt overlay is non-blocking via `app.processEvents()`
- Grid dimensions and cell size are in `Config` (defaults: 3×3, 63×63 px; overridable via `.env`)
- No virtual environment tracked in repo; `.venv/` is gitignored
