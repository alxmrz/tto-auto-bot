# Tic-Tac-Toe auto bot

Bot that plays Tic-Tac-Toe on screen using OpenCV template matching. Detects a 3×3 grid, reads X/O marks, and clicks the next empty cell.

## Quick start

```bash
make install
make test
make run
```

Requires a display (X11/Wayland). Press **Esc** to exit.

## How it works

- Captures the screen and locates the game grid via template matching
- Scans each cell to detect X or O marks
- Picks the first empty cell and clicks it
- After a game ends, clicks "OK", sets difficulty, and starts a new round

## Custom templates

The bot detects the grid and marks via template matching. If you want to use a different visual style of tic-tac-toe, add your own screenshots to `resources/custom/` and override the paths in `.env`:

```env
GRID_TEMPLATE_PATH=resources/custom/my_grid.png
TEMPLATE_O_PATH=resources/custom/my_o.png
TEMPLATE_X_PATH=resources/custom/my_x.png
TEMPLATE_OK_BUTTON_PATH=resources/custom/my_ok.png
TEMPLATE_EASY_LEVEL_PATH=resources/custom/my_easy.png
TEMPLATE_HARD_LEVEL_PATH=resources/custom/my_hard.png
```

## Project structure

| Path | Purpose |
|---|---|
| `main.py` | Entrypoint with keyboard listener and game loop |
| `src/bot.py` | Orchestrator: finish_game, run |
| `src/brain.py` | EasyBrain / MediumBrain — move selection logic |
| `src/eyes.py` | Screen detection via template matching |
| `src/hands.py` | Click helpers |
| `src/config.py` | Dataclass with paths and grid dimensions |
| `src/debug.py` | Qt overlay for visual debugging (`GUI_ENABLED=true`) |
| `src/image.py` | Low-level `find_template` and `capture_region` |
| `src/logger.py` | Conditional logging |
| `src/types.py` | `Cell` NamedTuple — x, y, value |
| `resources/` | Template images (grid, X, O, buttons) |
| `resources/custom/` | Drop your own templates here |
