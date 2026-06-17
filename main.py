import time
import traceback

import mss
from pynput import keyboard

from src.bot import Bot
from src.brain import EasyBrain, MediumBrain
from src.config import Config
from src.eyes import Eyes
from src.hands import Hands
from src.image import Image
from src.logger import Logger

logger = Logger(enable=True)
config = Config()
running = True
sct = mss.MSS()
overlay = None

if config.gui_enabled:
    from src.debug import DebugOverlay
    from PyQt5.QtWidgets import QApplication
    import sys

    overlay = DebugOverlay(QApplication(sys.argv))


def on_press(key):
    global running
    if key == keyboard.Key.esc:
        logger.info("EXIT")
        running = False
        if overlay is not None:
            overlay.quit()


try:
    image = Image(sct, config.threshold)
    bot = Bot(MediumBrain(EasyBrain(logger), logger), Eyes(config, image, logger), Hands(config, logger), logger)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while running:
        cells = bot.run()

        if overlay is not None:
            overlay.update_cells(cells)

        time.sleep(1)

except Exception as e:
    logger.info(e)
    traceback.print_exc()
finally:
    sct.close()
