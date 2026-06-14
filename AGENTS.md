# Tic-Tac-Toe auto bot

Tic-Tac-Toe bot using OpenCV template matching + screen capture. Detects a 3×3 grid on screen, reads X/O marks via image templates, and clicks the next empty cell.

## Commands

```bash
make run          # python3 main.py
```

No tests, linter, formatter, typechecker, or CI configured.

## Dependencies

- `mss`, `opencv-python`, `numpy`, `pyautogui`, `pynput`
- No `requirements.txt` or `pyproject.toml` — install manually or use `.venv`

## Structure

| Path | Purpose |
|---|---|
| `main.py` | Entrypoint: screen capture, grid detection, clicking |
| `src/AI.py` | AI logic — currently picks first empty cell (stub) |
| `src/Image.py` | Empty / unused |
| `resources/` | Template images for grid, X, O, OK button, difficulty buttons |
| `screen_shots/` | Runtime cell captures (gitignored) |

## Conventions

- Commits must follow [Conventional Commits](https://www.conventionalcommits.org/) format (e.g. `feat:`, `fix:`, `refactor:`, `chore:`, `docs:`).

## Quirks

- `make run` requires a display (X11/Wayland) — will fail headless
- Grid is 3×3 hardcoded; cell size hardcoded at 63×63 px
- `src/AI.py` and `src/Image.py` are the places to extend for smarter play or image utilities
- No virtual environment tracked in repo; `.venv/` is gitignored
