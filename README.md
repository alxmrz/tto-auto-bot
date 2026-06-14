# Tic-Tac-Toe auto bot

Bot that plays Tic-Tac-Toe on screen using OpenCV template matching. Detects a 3×3 grid, reads X/O marks, and clicks the next empty cell.

## Quick start

```bash
make install
make run
```

Requires a display (X11/Wayland). Press **Esc** to exit.

## How it works

- Captures the screen and locates the game grid via template matching
- Scans each cell to detect X or O marks
- Picks the first empty cell and clicks it
- After a game ends, clicks "OK", sets difficulty, and starts a new round

## Project structure

| Path | Purpose |
|---|---|
| `main.py` | Entrypoint with keyboard listener and game loop |
| `src/bot.py` | Orchestrator: finish_game, run |
| `src/brain.py` | EasyBrain — picks first empty cell |
| `src/eyes.py` | Screen detection via template matching |
| `src/hands.py` | Click helpers |
| `src/config.py` | Dataclass with paths and grid dimensions |
| `src/image.py` | Low-level `find_template` and `capture_region` |
| `src/logger.py` | Conditional logging |
| `resources/` | Template images (grid, X, O, buttons) |
