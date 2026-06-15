import sys
import time
import traceback

import mss
from PyQt5.QtWidgets import QApplication
from pynput import keyboard

from src.bot import Bot
from src.brain import EasyBrain, MediumBrain
from src.config import Config
from src.debug import DebugOverlay
from src.eyes import Eyes
from src.hands import Hands
from src.image import Image
from src.logger import Logger

logger = Logger(enable=True)
config = Config()
running = True


def on_press(key):
    global running
    if key == keyboard.Key.esc:
        logger.info("EXIT")
        running = False
        app.quit()


sct = mss.MSS()

# 1. Сначала создаём QApplication
app = QApplication(sys.argv)

# 2. Потом создаём виджет
overlay = DebugOverlay()


try:
    image = Image(sct, config.threshold)
    bot = Bot(MediumBrain(EasyBrain(logger), logger), Eyes(config, image, logger), Hands(config, logger), logger)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while running:
        cells = bot.run()

        overlay.update_cells(cells)

        # 3. Запускаем главный цикл
        sys.exit(app.exec())

        time.sleep(1)

except Exception as e:
    logger.info(e)
    traceback.print_exc()
finally:
    sct.close()
